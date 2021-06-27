'''
MIT License

Copyright (c) 2021 Albino Cianciotti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute,
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from flask import Flask, request, render_template, Markup, send_from_directory, session, flash

import os
import mysql.connector
import plotly
from plotly.graph_objs import Scatter, Layout
import logging
from datetime import datetime, timedelta
import pytz

app = Flask(__name__)
app.secret_key = "<g\x93E\xf3\xc6\xb8\xc4\x87\xff\xf6\x0fxD\x91\x13\x9e\xfe1+%\xa3\x83\xb6"

def connectToMySql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        # password="yourpassword",
        database="weatherstation"
    )

    return mydb

def saveWeatherData(temp, hum, pres, date):
    result = False
    mydb = connectToMySql()
    try:
        mycursor = mydb.cursor()
        sql = "INSERT INTO `indoorweatherdata`(`Date`, `Temperature`, `Humidity`, `Pressure`) VALUES (%s,%s,%s,%s)"
        val = (date, temp, hum, pres)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        if mycursor.rowcount > 0:
            result = True
        mydb.close()
    except:
        mydb.close()
    return result

def getLatestWeatherData():
    mydb = connectToMySql()
    try:
        mycursor = mydb.cursor()
        query = "SELECT * FROM `indoorweatherdata` WHERE 1 ORDER BY Date DESC LIMIT 1"
        mycursor.execute(query)
        result = mycursor.fetchall()
        mydb.close()
    except:
        mydb.close()
        result = False
    return result

def checkSystemOn():
    systemOn = False
    IST = pytz.timezone('Europe/Rome')
    datetime_utc = datetime.now(IST)
    #print("Date & Time in UTC : ", datetime_utc.strftime('%Y:%m:%d %H:%M:%S'))
    latestData = getLatestWeatherData()
    lastDate = latestData[0][0]
    #print("Latest Date : ", lastDate.strftime('%Y:%m:%d %H:%M:%S'))
    currentDateTime = datetime_utc.replace(tzinfo=None)
    lastDateTime = lastDate.replace(tzinfo=None)
    diffBetweenDates = currentDateTime-lastDateTime
    #print("Difference: ", diffBetweenDates)
    if diffBetweenDates > timedelta(minutes=15):
        systemOn = False
    else:
        systemOn = True
    return systemOn

def getSpecificData(dataToSelect):
    mydb = connectToMySql()
    mycursor = mydb.cursor()
    query = "SELECT Date ,"+dataToSelect+" FROM `indoorweatherdata`"
    mycursor.execute(query)
    result = mycursor.fetchall()
    mydb.close()
    print(result)
    return result

def createPlot(datas, dataType):
    if dataType == 'Temperature':
        plotColor = '#ff9900'
        plotTitle = 'Temperatures'
    elif dataType == 'Humidity':
        plotColor = '#029400'
        plotTitle = 'Humidity'
    else:
        plotColor = '#70bfff'
        plotTitle ='Pressure'

    dataDictionary = {
        "X": [],
        "Y": []
    }
    for x in datas:
        dataDictionary["X"].append(x[0])
        dataDictionary["Y"].append(x[1])
    plot = plotly.offline.plot({
        "data": [Scatter(x=dataDictionary["X"], y=dataDictionary["Y"], line=dict(color=plotColor, width=2))],
        "layout": Layout(title=plotTitle, height=1000, margin=dict(
            l=50,
            r=50,
            b=100,
            t=100,
            pad=4
        ))
    }, output_type='div'
    )

    return plot

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def homePage():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        #get latest sensor datas
        latestData = getLatestWeatherData()
        lastDataTime = latestData[0][0]
        lastTemperature = latestData[0][1]
        lastHumidity = latestData[0][2]
        lastPressure = latestData[0][3]
        #get data to build temperatures plot
        temperatures = getSpecificData("Temperature")
        temperaturesPlot = createPlot(temperatures, "Temperature")
        temperaturesPlotHtml = Markup(temperaturesPlot)
        #get data to build humidity plot
        humidity = getSpecificData("Humidity")
        humidityPlot = createPlot(humidity, "Humidity")
        humidityPlotHtml = Markup(humidityPlot)
        #get data to build atmospheric pressure plot
        pressure = getSpecificData("Pressure")
        pressurePlot = createPlot(pressure, "Pressure")
        pressurePlotHtml = Markup(pressurePlot)

        systemOn = checkSystemOn()

        return render_template("home.html", lastDataTime=lastDataTime, lastTemperature=lastTemperature, lastHumidity=lastHumidity, lastPressure=lastPressure, temperaturePlot=temperaturesPlotHtml, humidityPlot=humidityPlotHtml, pressurePlot=pressurePlotHtml, systemOn=systemOn)

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'esp8266' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Wrong username or password!')
    return homePage()

@app.route("/logout", methods=['POST'])
def logout():
    session['logged_in'] = False
    return homePage()

#example query: /postWeatherData?Temp=26.3&Hum=23.7&Pres=3455.8&Date=2021-05-05&Time=12:39
@app.route('/postWeatherData', methods=['GET', 'POST'])
def postWeatherData():
    if request.method == 'GET':
        temperature = request.args.get('Temp')
        humidity = request.args.get('Hum')
        pressure = request.args.get('Pres')
        date = request.args.get('Date')
        time = request.args.get('Time')
        print("New Weather Data. T:" + temperature + " H:" + humidity + " P:" + pressure + " Date:" + date + " Time:" + time)
        datetime = date + " " + time
        if float(temperature) > -14 and float(temperature) < 46 and float(humidity) >4 and float(humidity) < 71:
            insertResult = saveWeatherData(temperature, humidity, pressure, datetime)
            print("postWeatherData result: " + str(insertResult))
        else:
            logging.info("Weather data values out of range (esp temperature sensor error). Weather Data received:  T:" + temperature + " H:" + humidity + " P:" + pressure + " Date:" + date + " Time:" + time )
        # return redirect('/')
    return 'ok'

if __name__ == '__main__':
    app.env = "debug"
    app.debug = True
    app.run()