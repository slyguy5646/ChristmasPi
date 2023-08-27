from flask import Flask, render_template, request, make_response, jsonify
import re
import board
import neopixel
import time
from light import *
from color import * 



#initializes flask
app = Flask(__name__)


def customStatus(code, message):
    response = make_response(message, code)
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.route('/solid-color/<path:color>')
def solidColor(color):
    if color not in colorDict.keys():
        return customStatus(422, "Invalid Color")

    fullOn(color)

    return {"success": True, "data": getStrandStatusAsDict()}


@app.route('/off')
def turnOff():
    fullOff()
    return {"success": True, "data": getStrandStatusAsDict()}
    
@app.route('/get-pixel/<path:index>')
def getPixel(index):
    return {"data": getPixelColor(int(index))}


@app.route('/colorerror')
def colorError():
    return render_template('colorerror.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3003)