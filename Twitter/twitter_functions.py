from Flask.set import setColor
from Twitter.lists import effectColor, effectColorString, currentEffectString
from Lights.color import off
from Lights.light import pixels
from Flask.set import setEffectString

def setList0(list, item_to_add):
    list.clear()
    list.append(item_to_add)


def checkForColorTweet(colorToSet, colorCMD, tweetArg):
    if colorCMD in tweetArg.text.lower():
        setColor(colorToSet)



def checkForOffTweet(tweetArg):
    if '!off' in tweetArg.text.lower():
        setList0(effectColor, off)
        setList0(effectColorString, 'off')



def checkForEffectTweet(funcToRun, effectCMD, bioEffect, tweetArg, apiArg):
    if effectCMD in tweetArg.text.lower():
        funcToRun
        pixels.show()
        setEffectString(bioEffect)
        apiArg.update_profile(description=f'Pi Lights is online 🎄.\nThe lights are {currentEffectString[0]} and {effectColorString[0]}')
        

