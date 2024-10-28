from flask import Flask, request, render_template, flash, request
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

# Load the JSON data at startup
with open('nuclear_explosions.json') as f:
    data = json.load(f)

@app.route("/submit", methods=["POST"])
def render_response():
    year = int(request.form['Year'].split('.')[-1])  # Extract the year from the submitted value
    
    # Count the number of tests for the specified year
    count = sum(1 for test in data if test['Date']['Year'] == year)
    
    return render_template('NTPY.html', Year2 = count, year = year)
    
    #if count > 0:
    #    return jsonify({"message": f"The year {year} had {count} nuclear tests."})
    #else:
    #    return jsonify({"message": f"The year {year} had no nuclear tests."})


@app.route("/submit", methods=["POST"])
def submit_response():
    country = request.form.get('Country')  # Use get() to avoid KeyError
    print(f"Received country: {country}")
    
    try:
        # Count tests for the selected country
        count = sum(1 for test in data if test['Location'].get('Country') == country)
        
        return render_template('NTCPC.html', CountryCount=count, country=country)
    except KeyError as ke:
        print(f"KeyError: {ke}")
        return "Country not found in data", 400
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred", 500

if __name__ == "__main__":
    app.run(debug=False)
    
