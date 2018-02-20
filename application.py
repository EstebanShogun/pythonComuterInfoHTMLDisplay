#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, Flask
import sys
import requests
import json

app = Flask(__name__)

url = "http://127.0.0.1:5000"

hostname = requests.get("%s/host/localhost" % url)
os = requests.get("%s/os/localhost" % url)
user = requests.get("%s/user/localhost" % url)
percentRam = requests.get("%s/percentRam/localhost" % url)
usedRam = requests.get("%s/usedRam/localhost" % url)


for value in hostname.json(): hostname = value
for value in os.json(): os = value
for value in user.json(): user = value
for value in percentRam.json(): percentRam = value
for value in usedRam.json(): usedRam = value
@app.route('/app')
def hello(): 
    return render_template('index.html',ram=percentRam, free=100-percentRam, ramNb=usedRam, hostname=hostname, os=os, user=user) 

@app.route('/canvas/')
def canvas(): 
    return render_template('canvasjs.min.js') 

if __name__ == '__main__':
    reload(sys)
    if hasattr(sys, "setdefaultencoding"):
        sys.setdefaultencoding("utf-8")
    print "Application en écoute sur port 8517"
    app.run(host="0.0.0.0", port=int("8517"), debug=True)