# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 03:24:41 2021

@author: kathr
"""

from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/second")
def second():
    return render_template('second.html')

if __name__ == "__main__":
    app.run(debug=True)