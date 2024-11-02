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
with open('nuclear_explosions.json') as f:
    data = json.load(f)
years = [1944, 1945, 1946, 1947, 1948, 1949, 1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000]
year0 = years[0]
year1 = years[1]
year2 = years[2]
year3 = years[3]
year4 = years[4]
year5 = years[5]
year6 = years[6]
year7 = years[7]
year8 = years[8]
year9 = years[9]
year10 = years[10]
year11 = years[11]
year12 = years[12]
year13 = years[13]
year14 = years[14]
year15 = years[15]
year16 = years[16]
year17 = years[17]
year18 = years[18]
year19 = years[19]
year20 = years[20]
year21 = years[21]
year22 = years[22]
year23 = years[23]
year24 = years[24]
year25 = years[25]
year26 = years[26]
year27 = years[27]
year28 = years[28]
year29 = years[29]
year30 = years[30]
year31 = years[31]
year32 = years[32]
year33 = years[33]
year34 = years[34]
year35 = years[35]
year36 = years[36]
year37 = years[37]
year38 = years[38]
year39 = years[39]
year40 = years[40]
year41 = years[41]
year42 = years[42]
year43 = years[43]
year44 = years[44]
year45 = years[45]
year46 = years[46]
year47 = years[47]
year48 = years[48]
year49 = years[49]
year50 = years[50]
year51 = years[51]
year52 = years[52]
year53 = years[53]
year54 = years[54]
year55 = years[55]

# Count the number of tests for the specified year
count1 = sum(1 for test in data if test['Date']['Year'] == year1)
count2 = sum(1 for test in data if test['Date']['Year'] == year2)
count3 = sum(1 for test in data if test['Date']['Year'] == year3)
count4 = sum(1 for test in data if test['Date']['Year'] == year4)
count5 = sum(1 for test in data if test['Date']['Year'] == year5)
count6 = sum(1 for test in data if test['Date']['Year'] == year6)
count7 = sum(1 for test in data if test['Date']['Year'] == year7)
count8 = sum(1 for test in data if test['Date']['Year'] == year8)
count9 = sum(1 for test in data if test['Date']['Year'] == year9)
count10 = sum(1 for test in data if test['Date']['Year'] == year10)
count11 = sum(1 for test in data if test['Date']['Year'] == year11)
count12 = sum(1 for test in data if test['Date']['Year'] == year12)
count13 = sum(1 for test in data if test['Date']['Year'] == year13)
count14 = sum(1 for test in data if test['Date']['Year'] == year14)
count15 = sum(1 for test in data if test['Date']['Year'] == year15)
count16 = sum(1 for test in data if test['Date']['Year'] == year16)
count17 = sum(1 for test in data if test['Date']['Year'] == year17)
count18 = sum(1 for test in data if test['Date']['Year'] == year18)
count19 = sum(1 for test in data if test['Date']['Year'] == year19)
count20 = sum(1 for test in data if test['Date']['Year'] == year20)
count21 = sum(1 for test in data if test['Date']['Year'] == year21)
count22 = sum(1 for test in data if test['Date']['Year'] == year22)
count23 = sum(1 for test in data if test['Date']['Year'] == year23)
count24 = sum(1 for test in data if test['Date']['Year'] == year24)
count25 = sum(1 for test in data if test['Date']['Year'] == year25)
count26 = sum(1 for test in data if test['Date']['Year'] == year26)
count27 = sum(1 for test in data if test['Date']['Year'] == year27)
count28 = sum(1 for test in data if test['Date']['Year'] == year28)
count29 = sum(1 for test in data if test['Date']['Year'] == year29)
count30 = sum(1 for test in data if test['Date']['Year'] == year30)
count31 = sum(1 for test in data if test['Date']['Year'] == year31)
count32 = sum(1 for test in data if test['Date']['Year'] == year32)
count33 = sum(1 for test in data if test['Date']['Year'] == year33)
count34 = sum(1 for test in data if test['Date']['Year'] == year34)
count35 = sum(1 for test in data if test['Date']['Year'] == year35)
count36 = sum(1 for test in data if test['Date']['Year'] == year36)
count37 = sum(1 for test in data if test['Date']['Year'] == year37)
count38 = sum(1 for test in data if test['Date']['Year'] == year38)
count39 = sum(1 for test in data if test['Date']['Year'] == year39)
count40 = sum(1 for test in data if test['Date']['Year'] == year40)
count41 = sum(1 for test in data if test['Date']['Year'] == year41)
count42 = sum(1 for test in data if test['Date']['Year'] == year42)
count43 = sum(1 for test in data if test['Date']['Year'] == year43)
count44 = sum(1 for test in data if test['Date']['Year'] == year44)
count45 = sum(1 for test in data if test['Date']['Year'] == year45)
count46 = sum(1 for test in data if test['Date']['Year'] == year46)
count47 = sum(1 for test in data if test['Date']['Year'] == year47)
count48 = sum(1 for test in data if test['Date']['Year'] == year48)
count49 = sum(1 for test in data if test['Date']['Year'] == year49)
count50 = sum(1 for test in data if test['Date']['Year'] == year50)
count51 = sum(1 for test in data if test['Date']['Year'] == year51)
count52 = sum(1 for test in data if test['Date']['Year'] == year52)
count53 = sum(1 for test in data if test['Date']['Year'] == year53)
count54 = sum(1 for test in data if test['Date']['Year'] == year54)
count55 = sum(1 for test in data if test['Date']['Year'] == year55)
return render_template('IINTPY.html', 
    TO45 = count1, 
    TO46 = count2, 
    TO47 = count3, 
    TO48 = count4, 
    TO49 = count5, 
    TO50 = count6, 
    TO51 = count7, 
    TO52 = count8, 
    TO53 = count9, 
    TO54 = count10, 
    TO55 = count11, 
    TO56 = count12, 
    TO57 = count13, 
    TO58 = count14, 
    TO59 = count15, 
    TO60 = count16, 
    TO61 = count17, 
    TO62 = count18, 
    TO63 = count19, 
    TO64 = count20, 
    TO65 = count21, 
    TO66 = count22, 
    TO67 = count23, 
    TO68 = count24, 
    TO69 = count25, 
    TO70 = count26, 
    TO71 = count27, 
    TO72 = count28, 
    TO73 = count29, 
    TO74 = count30, 
    TO75 = count31, 
    TO76 = count32, 
    TO77 = count33, 
    TO78 = count34, 
    TO79 = count35, 
    TO80 = count36, 
    TO81 = count37, 
    TO82 = count38, 
    TO83 = count39, 
    TO84 = count40, 
    TO85 = count41, 
    TO86 = count42, 
    TO87 = count43, 
    TO88 = count44, 
    TO89 = count45,
    TO90 = count46,
    TO91 = count47,
    TO92 = count48
    TO93 = count49,
    TO94 = count50,
    TO95 = count51,
    TO96 = count52,
    TO97 = count53,
    TO98 = count54,
    TO99 = count55,
    TO00 = count55
)


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
    app.run(debug=False)
