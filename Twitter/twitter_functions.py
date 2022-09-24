from Flask.set import setColor

def checkForColorTweet(colorToSet, colorMSG):
    if colorMSG in tweet.text.lower():
        setColor(colorToSet)
