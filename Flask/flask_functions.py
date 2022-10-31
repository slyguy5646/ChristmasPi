from curses import flash
from flask import request
from Lights.light import doNothing
from Flask.set import setColor
from Lights.light import *
from Twitter.lists import *

def checkForColorButtonPress(colorToSet, btnName, btnValue):
    if request.form.get(btnName) == btnValue:         
        setColor(colorToSet)

# def checkForEffectButtonPress(funcToRun, btnName, btnValue, secondFuncToRun=doNothing()):
#     if request.form.get(btnName) == btnValue:
#         funcToRun
#         secondFuncToRun

def checkForEffects():
        #check if ledOn button was was pressed
        
        if request.form.get('LedOn') == 'ledon':
                ledOn(effectColor[0])
        #checks if fullOn button was pressed
        elif request.form.get('FullOn') == 'fullon':
                fullOn(effectColor[0])
        #checks if ledOff button was pressed
        elif request.form.get('Twinkle') == 'twinkle':
                twinkleToggle = True
                print(twinkleToggle)
                flashPurpOrange(twinkleToggle)
                
        elif request.form.get('LedOff') == 'ledoff':  
                ledOff()
                flashPurpOrange(twinkleToggle)
                pixels.show()
                setStatus('OFF')
        elif request.form.get('Apply') == 'apply':
   #             if bool(effectColor) == False:
   #                 return '/colorerror'
                pixels.show()
                setStatus('ON')
                #showMe()
