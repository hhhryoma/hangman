# -*- coding: utf-8 -*-
'''
Created on Jun 15, 2019

@author: hishidaryouba
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hell World!"

app.run(port='8000')
