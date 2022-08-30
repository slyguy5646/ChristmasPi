import board
import neopixel


#initializes strip on GPIO 18 with 50 LEDs on that strip
pixels = neopixel.NeoPixel(board.D18, 50)

#COLOR DEFENITIONS GRB
off = (0, 0, 0)
blue = (0, 0, 255)
green = (255, 0, 0)
red = (0, 255, 0)

#initialize effectColor list to hold last selected color
effectColor = []

#set color to red
def setRed():
    effectColor.clear()
    effectColor.append(red)
    return effectColor

#set color to green
def setGreen():
    effectColor.clear()
    effectColor.append(green)
    return effectColor

#set color to blue
def setBlue():
    effectColor.clear()
    effectColor.append(blue)
    return effectColor

#function to turn all leds off except the first which will glow green
def ledOn(colorvalue):
    pixels.fill((off))
    pixels[0] = (colorvalue)

#function to turn all LEDs solid green
def fullOn(colorValue):
    pixels.fill((colorValue))


#function to turn all LEDs off
def ledOff():
    pixels.fill((off))
    return 'light is off!'






