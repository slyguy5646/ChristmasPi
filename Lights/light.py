from ctypes.wintypes import RGB
import board
import neopixel
import time
import os
from Flask.set import setColor, setEffectString, setStatus
from Lights.color import *
from Twitter.lists import currentEffectString, twinkleToggle

#initializes strip on GPIO 18 with 50 LEDs on that strip
num_pixels = 50
pixels = neopixel.NeoPixel(board.D18, n=num_pixels, brightness=0.5, auto_write=False, pixel_order='RGB')
ORDER = neopixel.RGB


#function to turn all leds off except the first which will glow green
def ledOn(colorvalue):
    pixels.fill((off[0]))
    pixels[0] = (colorvalue)


#function to turn all LEDs solid green
def fullOn(colorValue):
    pixels.fill(colorValue)
    setEffectString('All LEDs are on')

#function to turn all LEDs off
def ledOff():
    pixels.fill(off)
    setColor(off)
    setEffectString('off')
    setStatus('Off')

def doNothing():
    print('I Did nothing!')

def flashPurpOrange(boolean):
    while boolean:
        pixels.fill(orange[0])
        pixels.show()
        time.sleep(1)
        pixels.fill(purple[0])
        pixels.show()
        time.sleep(1)
        if currentEffectString == 'off':
            boolean = False
    if boolean == False:
        ledOff()

#flashPurpOrange()