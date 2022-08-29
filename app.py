from flask import Flask, render_template, request
import re
import board
import neopixel
import time
from light import *

#initializes flask
app = Flask(__name__)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    rgb_color = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
    return rgb_color

#home page with GET and POST methods for button input functionality
@app.route('/', methods=['GET', 'POST'])
#function to get the button input
def index():
    color = request.form.get('color')
    print(color)
    rgb_color = hex_to_rgb(color)
    if request.method == 'POST':
        if request.form.get('ledOn') == 'FirstON':
            ledOn(color)
        elif request.form.get('fullOn') == 'FULLON':
            fullOn(color)
        elif request.form.get('ledOff') == 'OFF':
            ledOff()
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')