import board
import neopixel
import time
import os
from set import *

#initializes strip on GPIO 18 with 50 LEDs on that strip
pixels = neopixel.NeoPixel(board.D18, 50, auto_write=False)


#function to turn all leds off except the first which will glow green
def ledOn(colorvalue):
    pixels.fill((off))
    pixels[0] = (colorvalue)
    setStatus('Single LED on')


#function to turn all LEDs solid green
def fullOn(colorValue):
    pixels.fill((colorValue))
    setEffectString('All LEDs are on')

#function to turn all LEDs off
def ledOff():
    pixels.fill(off)
    setColor(off)
    setEffectString('off')
