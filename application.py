#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, Flask
import sys

app = Flask(__name__)

@app.route('/hello/')
def hello(ram=52, user="lul", os="lolux", hostname="oim"): 
    return render_template('index.html',ram=ram, free=100-ram, ramNb=25662, hostname=hostname, os=os, user=user) 

@app.route('/canvas/')
def canvas(): 
    return render_template('canvasjs.min.js') 

if __name__ == '__main__':
    reload(sys)
    if hasattr(sys, "setdefaultencoding"):
        sys.setdefaultencoding("utf-8")
    print "Application en écoute sur port 8517"
    app.run(host="0.0.0.0", port=int("8517"), debug=True)