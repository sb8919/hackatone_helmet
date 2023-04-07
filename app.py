# -*- coding: utf-8 -*-
import socket
from flask import Flask, request, jsonify
from flask import render_template
import pymysql

conn = None
cur = None

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('index.html')

@app.route("/get") 
def get():
    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='ScE1234**',db='sensor_db',charset='utf8')
    cur = conn.cursor()
    sql = "SELECT * from sensor"
    cur.execute(sql)
    data = cur.fetchall()
    return jsonify({'tilt_value': data[-1][0], 'infrared_value':data[-1][1]})


@app.route("/sensor") 
def sensor():
    conn = pymysql.connect(host='127.0.0.1', port=3306,user='root', passwd='ScE1234**',db='sensor_db',charset='utf8')
    cur = conn.cursor()
    tilt_value = request.args.get('tilt_value')
    infrared_value = request.args.get('infrared_value')
    sql ="INSERT INTO sensor (tilt_value,infrared_value) VALUES("+str(tilt_value)+","+str(infrared_value)+");"
    cur.execute(sql)
    conn.commit()
    conn.close()
    return render_template('index.html' ,tilt_value= tilt_value, infrared_value = infrared_value)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
