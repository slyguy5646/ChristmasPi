from flask import Flask, render_template, request
import board
import neopixel
import time
from light import *

#initializes flask
app = Flask(__name__)

#home page with GET and POST methods for button input functionality
@app.route('/', methods=['GET', 'POST'])
#function to get the button input
def index():
    if request.method == 'POST':
        if request.form.get('ledOn') == 'FirstON':
            ledOn()
        elif request.form.get('fullOn') == 'FULLON':
            fullOn()
        elif request.form.get('ledOff') == 'OFF':
            ledOff()
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')