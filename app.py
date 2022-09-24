from tkinter import Variable
from flask import Flask, render_template, request
import re
import board
import neopixel
import time
from Lights.light import *
from Flask.set import *
from Lights.color import *
from Flask.flask_functions import checkForColorButtonPress, checkForEffects


#initializes flask
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')