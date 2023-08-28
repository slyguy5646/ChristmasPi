import board
import neopixel
from color import *

#initializes strip on GPIO 18 with 50 LEDs on that strip
num_pixels = 100 #number of leds on the strand
pixels = neopixel.NeoPixel(board.D18, n=num_pixels, brightness=0.5, auto_write=False, pixel_order='RGB')
ORDER = neopixel.RGB

strandStatus = "off" # "on" | "off"
strandColor = "none" # any key of colorDict
strandBrightness = 0.5 # number 0.0-0.5


def setStrandInfo(color, status, brightness=strandBrightness):
    global strandColor
    global strandStatus
    global strandBrightness
    strandColor = color
    strandStatus = status
    strandBrightness = brightness

def setBrightness(brightness):
    if strandColor == "none" or strandStatus == "off":
        return
    valueToApply = min(brightness, 0.5)
    currentColorValue = colorDict[strandColor]

    newColor = []

    for value in currentColorValue:
        newColor.append(int(float(value) * 2 * valueToApply))

    pixels.fill(tuple(newColor))
    pixels.show()
    setStrandInfo(strandColor, strandStatus, valueToApply)

    

def getStrandStatusAsDict():
    return {"color": strandColor, "status": strandStatus, "brightness": strandBrightness}

def getColorValueFromKey(colorKey):
    return colorDict[colorKey]


#function to turn all leds off except the first which will glow green
def ledOn(colorvalue):
    pixels.fill((off[0]))
    pixels[0] = (colorvalue)


#function to turn all LEDs solid green
def fullOn(colorKey):
    colorValue = getColorValueFromKey(colorKey)
    print(colorValue)
    pixels.fill(colorValue)
    pixels.show()

    if checkIfColorChangedOccured(colorValue):
        print("MADE IT")
        setStrandInfo(colorKey, "on")
        print(strandColor, strandStatus)



 

def checkIfColorChangedOccured(desiredColorValue):
    firstPixelValue = getPixelColor(0)
    lastPixelValue = getPixelColor(99)

    if tuple(firstPixelValue) == desiredColorValue and tuple(lastPixelValue) == desiredColorValue:
        return True
    else: 
        return False

def getPixelColor(index):
  return pixels._getitem(index)

#function to turn all LEDs off
def fullOff():
    pixels.fill(off)
    pixels.show()

    if checkIfColorChangedOccured(off):
        setStrandInfo("none", "off")
    

def doNothing():
    print('I Did nothing!')

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