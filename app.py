from flask import Flask, render_template, request
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D18, 50)

#function to turn the first LED on the strip solid green
def ledOn():
    pixels[0] = (255, 0, 0)
    return 'light is on!'

#function to turn all LEDs solid green
def fullGreen():
    pixels.fill((255, 0, 0))


#function to turn all LEDs off
def ledOff():
    pixels.fill((0, 0, 0))
    return 'light is off!'


#initializes flask
app = Flask(__name__)

#home page with GET and POST methods for button input functionality
@app.route('/', methods=['GET', 'POST'])
#function to get the button input
def index():
    if request.method == 'POST':
        if request.form.get('action1') == 'ON':
            ledOn()
        elif request.form.get('action2') == 'OFF':
            ledOff()
        elif request.form.get('action3') == 'FULLGREEN':
            fullGreen()
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')