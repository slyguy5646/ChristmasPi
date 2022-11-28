from curses import flash
from flask import request
from Lights.light import doNothing
from Flask.set import setColor
from Lights.light import *
from Twitter.lists import *



def updateLightData(objToChagne, colorData, colorStringData, effectData, statusData):
    objToChagne["color"] = colorData
    objToChagne["colorString"] = colorStringData
    objToChagne["effect"] = effectData
    objToChagne["status"] = statusData


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
                
        elif request.form.get('LedOff') == 'ledoff':  
                ledOff()
                pixels.show()
                setStatus('OFF')
        elif request.form.get('Apply') == 'apply':
   #             if bool(effectColor) == False:
   #                 return '/colorerror'
                pixels.show()
                setStatus('ON')
                #showMe()
        elif request.form.get('RedGreen') == 'redgreen':
                redGreen()
                setStatus('ON')
