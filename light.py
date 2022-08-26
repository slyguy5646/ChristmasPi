import board
import neopixel

#initializes strip on GPIO 18 with 50 LEDs on that strip
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





