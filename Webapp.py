from flask import Flask, request, render_template, flash, request
from markupsafe import Markup

import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

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

# Load the JSON data at startup

@app.route("/submit")
def render_response():
    with open('nuclear_explosions.json') as f:
        data = json.load(f)
    year = int(request.args['Year'].split('.')[-1])  # Extract the year from the submitted value
    
    # Count the number of tests for the specified year
    count = sum(1 for test in data if test['Date']['Year'] == year)
    if count > 0:
        return render_template('NTPY.html', Year2 = count, year = year)
    else:
        return render_template('NTPY.html', Year2 = "here were no nuclear test", year = year, name = name)
  
@app.route("/response")
def submit_response():
    with open('nuclear_explosions.json') as f:
        data = json.load(f)
    country = request.args['Country']  # Use get() to avoid KeyError
    
    # Count tests for the selected country
    count = sum(1 for test in data if test['Location']['Country'] == country)
        
    return render_template('NTCPC.html', CountryCount=count, country=country)

if __name__=="__main__":
    app.run(debug=True)