from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/page2')
def NTPY():
    return render_template('NTPY.html')

@app.route('/page3')
def NTCPC():
    return render_template('NTCPC.html')

@app.route('/page4')
def IINTPY():
    return render_template('IINTPY.html')
    
@app.route('/page5')
def TEOTB():
    return render_template('TEOTB.html')

if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
    
