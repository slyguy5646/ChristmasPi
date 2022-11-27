from Lights.color import *
from Twitter.lists import *


#function to set status list for use in flask app
def setStatus(statusArg):
    status.clear()
    status.append(statusArg)

#function to set the currentEffectString list for use in flask app
def setEffectString(effectString):
   currentEffectString.clear()
   currentEffectString.append(effectString)

#function to be called to set the color and all of the lists corresponding to color
def setColor(colorList):
   list = colorList
   effectColor.clear()
   effectColor.append(list[0])
   effectColorString.clear()
   effectColorString.append(list[1])