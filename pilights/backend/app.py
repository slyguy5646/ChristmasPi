from tkinter import Variable
from flask import Flask, render_template, request, jsonify
import re
import board
import neopixel
import time
from Lights.light import ledOn, fullOn, ledMaster, doNothing, ledOff, pixels, redGreen
from Flask.set import *
from Lights.color import *
from Flask.flask_functions import checkForColorButtonPress, checkForEffects
from Twitter.lists import *
from flask_cors import CORS
import json


#initializes flask
app = Flask(__name__)
CORS(app)

#home page with GET and POST methods for button input functionality
@app.route('/', methods=['GET', 'POST'])
#function to get the button input
def index():
    if request.method == 'POST':
        #CHECK FOR IF COLOR BUTTONS WERE PRESSED
        checkForColorButtonPress(red, 'Red', 'red')                              #RED
        checkForColorButtonPress(green, 'Green', 'green')                        #GREEN
        checkForColorButtonPress(blue, 'Blue', 'blue')                           #BLUE
        checkForColorButtonPress(orange, 'Orange', 'orange')                     #ORANGE
        checkForColorButtonPress(yellow, 'Yellow', 'yellow')                     #YELLOW
        checkForColorButtonPress(lightGreen, 'LightGreen', 'lightgreen')         #LIGHTGREEN
        checkForColorButtonPress(powderBlue, 'PowderBlue', 'powderblue')         #POWDERBLUE
        checkForColorButtonPress(purple, 'Purple', 'purple')                     #PURPLE
        checkForColorButtonPress(pink, 'Pink', 'pink')                           #PINK

        #CHECK IF EFFECT BUTTONS WERE PRESSED
        checkForEffects()
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template(
        'index.html', 
        colorString = effectColorString[0], 
        effectString = currentEffectString[0], 
        statusString = status[0]
    )

@app.route('/colorerror')
def colorError():
    return render_template('colorerror.html')



lightData = {
    "color": effectColor[0],
    "colorString": effectColorString[0],
    "effect": currentEffectString[0],
    "status": status[0]
    
}
def updateLightData():
    lightData["color"] = effectColor[0]
    lightData["colorString"] = effectColorString[0]
    lightData["effect"] = currentEffectString[0]
    lightData["status"] = status[0]


@app.route('/lightdata') #gives data on current light state
def color_data():
    
    updateLightData()
    return jsonify(lightData)

@app.route('/red')
def changecolor(): 
    setColor(red)
    print('color is red')

    updateLightData()
    print(lightData)
    return  jsonify(lightData)

@app.route('/on')
def toggle():
    if request.method == 'GET':
       
        fullOn(effectColor[0])
        print(f'lights are on and {effectColor[0]}')
        updateLightData()
        setStatus('ON')
        # print(status)
        print(lightData)
        return jsonify(lightData)
    
@app.route('/off')
def off():
    if request.method == 'GET':
        ledOff()
        updateLightData()
        return jsonify(lightData)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')