import board
import neopixel
import time
import os
from set import *

#initializes strip on GPIO 18 with 50 LEDs on that strip
pixels = neopixel.NeoPixel(board.D18, 50, auto_write=False)


def setStatus(statusArg):
    status.clear()
    status.append(statusArg)


#function to turn all leds off except the first which will glow green
def ledOn(colorvalue):
    pixels.fill((off))
    pixels[0] = (colorvalue)
    currentEffectString.clear()
    currentEffectString.append('Single LED On')


#function to turn all LEDs solid green
def fullOn(colorValue):
    pixels.fill((colorValue))
    currentEffectString.clear()
    currentEffectString.append('All LEDs On')

#function to turn all LEDs off
def ledOff():
    pixels.fill((off))
    effectColorString.clear()
    effectColorString.append('Lights are off')
    effectColor.clear()
    currentEffectString.clear()
    currentEffectString.append('Lights are off')
    return effectColor, effectColorString


# def travelingPixel(colorvalue):
#     currentEffectString.clear()
#     currentEffectString.append('Pixel traveling...')
#     for i in range(1, 50):
#         pixels[i] = colorvalue
