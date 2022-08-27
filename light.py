import board
import neopixel

#initializes strip on GPIO 18 with 50 LEDs on that strip
pixels = neopixel.NeoPixel(board.D18, 50)

#COLOR DEFENITIONS GRB
off = (0, 0, 0)
blue = (0, 0, 255)
green = (255, 0, 0)
red = (0, 255, 0)

effectColor = off

#function to turn all leds off except the first which will glow green
def ledOn():
    pixels.fill((off))
    pixels[0] = (green)

#function to turn all LEDs solid green
def fullOn():
    pixels.fill((green))


#function to turn all LEDs off
def ledOff():
    pixels.fill((off))
    return 'light is off!'






