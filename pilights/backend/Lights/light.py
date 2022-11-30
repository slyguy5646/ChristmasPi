from ctypes.wintypes import RGB
import board
import neopixel
import time
import os
from Flask.set import setColor, setEffectString, setStatus
from Lights.color import *
from Twitter.lists import currentEffectString

#initializes strip on GPIO 18 with 50 LEDs on that strip
num_pixels = 100 #number of leds on the strand
pixels = neopixel.NeoPixel(board.D18, n=num_pixels, brightness=0.5, auto_write=False, pixel_order='RGB')
ORDER = neopixel.RGB


#function to turn all leds off except the first which will glow green
def ledOn(colorvalue):
    pixels.fill((off[0]))
    pixels[0] = (colorvalue)


#function to turn all LEDs solid green
def fullOn(colorValue):
    pixels.fill(colorValue)
    setEffectString('all on')
    print(f'all leds on {colorValue}')
    pixels.show()

#function to turn all LEDs off
def ledOff():
    pixels.fill(off)
    setColor(off)
    setEffectString('off')
    setStatus('off')
    pixels.show()

def doNothing():
    print('I Did nothing!')

def ledMaster(incomingObj):
    ledChanges = incomingObj
    if ledChanges['effect'] == "singleOn":
        ledOn(ledChanges['color'])
        print('single light on')
    elif ledChanges['effect'] == "fullOn":
        fullOn(ledChanges['color'])
        print(f"all lights on {ledChanges['color']}")
    

# def flashPurpOrange(boolean):
#     while boolean:
#         pixels.fill(orange[0])
#         pixels.show()
#         time.sleep(1)
#         pixels.fill(purple[0])
#         pixels.show()
#         time.sleep(1)
#         if currentEffectString == 'off':
#             boolean = False
#     if boolean == False:
#         ledOff()

#flashPurpOrange()

def redGreen():
    evens = []
    odds = []
    for i in range(0, 100):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    for j in evens:
        pixels[j] = red[0]
    for k in odds:
        pixels[k] = green[0]

    pixels.show()

# redGreen()
# pixels.fill(green[0])