import board
import neopixel


#initializes strip on GPIO 18 with 50 LEDs on that strip
pixels = neopixel.NeoPixel(board.D18, 50, auto_write=False)

#COLOR DEFENITIONS GRB
off = (0, 0, 0)
blue = (0, 0, 255)
green = (255, 0, 0)
red = (0, 255, 0)

#initialize lists to hold LED status data
effectColor = [off]
effectColorString = ['off']
currentEffectString = ['off']
status = ['off']

def setStatus(statusArg):
    status.clear()
    status.append(statusArg)


#set color to red
def setRed():
    effectColor.clear()
    effectColor.append(red)
    effectColorString.clear()
    effectColorString.append('Red')
    return effectColor, effectColorString

#set color to green
def setGreen():
    effectColor.clear()
    effectColor.append(green)
    effectColorString.clear()
    effectColorString.append('Green')
    return effectColor, effectColorString

#set color to blue
def setBlue():
    effectColor.clear()
    effectColor.append(blue)
    effectColorString.clear()
    effectColorString.append('Blue')
    return effectColor, effectColorString

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






