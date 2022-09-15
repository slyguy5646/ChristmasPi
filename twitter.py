from collections import UserList
from email import message
from multiprocessing.connection import Client
from delete import tweetOrDelete
from light import *
from set import setColor, effectColor
from keys import creds
import tweepy
import time
from delete import tweetOrDelete, checkTweet
from lists import *


def reply(msg, usr):
   api.update_status(status = msg, in_reply_to_status_id = usr)


class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      return print('Connected!')
   
   def on_tweet(self, tweet):
      userList.clear()
      mentions = api.mentions_timeline()

      for mention in mentions:
         userList.append(mention.user.screen_name)
         userList.append(mention.id)
         
      print(str(userList[-2]) + ' ' + str(userList[-1]))

      if '!red' in tweet.text.lower():
         setColor(red)
      elif '!green' in tweet.text.lower():
         setColor(green)
      elif '!blue' in tweet.text.lower():
         setColor(blue)
      elif '!off' in tweet.text.lower():
         pass



      # print(str(userList[0]) + ' - ' + tweet.text)
      print('Color set to: ' + str(effectColor[0]))
      time.sleep(1)


      if '!on' in tweet.text.lower():
         ledOn(effectColor[0])
         pixels.show()
         print('Single led is on.')
      elif '!fullon' in tweet.text.lower():
         fullOn(effectColor[0])
         pixels.show()
         print('All leds are on.')
      elif '!off' in tweet.text.lower():
         ledOff()
         pixels.show()
         print('LEDs are off')
      else:
         tweetOrDelete(statusTweet[0], userList[-1])

         
      # currentColor = effectColorString[0]
      # currentEffect = currentEffectString[0]
      # statusTweet.append(f"@{ userList[0] } The leds are now { currentColor } and { currentEffect }")
      time.sleep(3)

stream = MyStream(bearer_token=creds['BEARER_TOKEN'])


for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

stream.filter() 
  