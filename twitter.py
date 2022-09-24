import tweepy
import time
from collections import UserList
from email import message
from multiprocessing.connection import Client
from Lights.light import *
from Flask.set import setColor, effectColor
from Twitter.keys import creds
import tweepy
import time
from Twitter.delete import tweetOrDelete
from Twitter.lists import *
from Lights.color import *
from Twitter.twitter_functions import *


def reply(msg, usr):
   api.update_status(status = msg, in_reply_to_status_id = usr)


class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      api.update_profile(description='Pi Lights is Online! 🎄')
      if piTweetIds[0] != 0:
         for i in piTweetIds:
            api.destroy_status(i)
      else:
         pass
      piTweetIds.clear()
      return print('Connected!')
   
   def on_tweet(self, tweet):
      #adds tweets id to tweetIdForReply in case it is needed for an error message
      setList0(tweetIdForReply, tweet.id)

      #adds tweet.text and tweet.id as key value pair to check if that tweet has already been sent 
      tweetTextId[tweet.text] = tweet.id
      userList.clear()

      #gets list of mentions
      mentions = api.mentions_timeline()

      #goes through mentions and adds their username and userid to userList
      for mention in mentions:
         userList.append(mention.user.screen_name)
         userList.append(mention.id)

      #prints user's username and user id   
      print(str(userList[-2]) + ' says: '  + tweet.text)

      if '!red' in tweet.text.lower():          #RED
         setColor(red)
      elif '!green' in tweet.text.lower():      #GREEN
         setColor(green)
      elif '!blue' in tweet.text.lower():       #BLUE
         setColor(blue)
      elif '!off' in tweet.text.lower():        #OFF
         setList0(effectColor, off)
         setList0(effectColorString, 'off')
      elif '!orange' in tweet.text.lower():     #ORANGE
         setColor(orange)
      elif '!yellow' in tweet.text.lower():     #YELLOW
         setColor(yellow)
      elif '!lightgreen' in tweet.text.lower(): #LIGHTGREEN
         setColor(lightGreen)
      elif '!powderblue' in tweet.text.lower(): #POWDERBLUE
         setColor(powderBlue)
      elif '!purple' in tweet.text.lower():     #PURPLE
         setColor(purple)
      elif '!pink' in tweet.text.lower():       #PINK
         setColor(pink)
      else:
         setColor(off)



      
      #print('Color set to: ' + str(effectColor[0]))
      time.sleep(1)

      #if a color the color is anything but off
      if effectColor[0] != off:
         #if the on command is received turn on one LED
         if '!on' in tweet.text.lower():
            ledOn(effectColor[0])
            pixels.show()
            print('Single led is on and ' + str(effectColorString[0]) + '.')
         #if the fullon command is received turn all LEDs on
         elif '!fullon' in tweet.text.lower():
            fullOn(effectColor[0])
            pixels.show()
            print('All leds are on and ' + str(effectColorString[0]) + '.')
      #if the off command is received turn all LEDs off
      elif '!off' in tweet.text.lower():
         ledOff()
         pixels.show()
         print('LEDs are off')
      
      #tweet no color error message
      else:
         tweetOrDelete(f'@{ userList[-2] } ' + statusTweet[0])

         
      # currentColor = effectColorString[0]
      # currentEffect = currentEffectString[0]
      # statusTweet.append(f"@{ userList[0] } The leds are now { currentColor } and { currentEffect }")
      time.sleep(.5)
   def on_disconnect(self):
      api.update_profile(description="Pi Lights is sleeping 💤")
      return print('Disconnected!')

#initialize stream
stream = MyStream(bearer_token=creds['BEARER_TOKEN'])
for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

#start stream
stream.filter() 
  