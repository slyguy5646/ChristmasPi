from collections import UserList
from email import message
from multiprocessing.connection import Client
from delete import tweetOrDelete
from light import *
from set import setColor, effectColor
from keys import creds
import tweepy
import time
from delete import tweetOrDelete
from lists import *


def reply(msg, usr):
   api.update_status(status = msg, in_reply_to_status_id = usr)


class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      if piTweetIds[0] != 0:
         for i in piTweetIds:
            api.destroy_status(i)
      else:
         pass
      piTweetIds.clear()
      return print('Connected!')
   
   def on_tweet(self, tweet):
      #adds tweets id to tweetIdForReply in case it is needed for an error message
      tweetIdForReply.clear()
      tweetIdForReply.append(tweet.id)

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

      if '!red' in tweet.text.lower():
         setColor(red)
      elif '!green' in tweet.text.lower():
         setColor(green)
      elif '!blue' in tweet.text.lower():
         setColor(blue)
      elif '!off' in tweet.text.lower():
         setColor(off)
      else:
         setColor(off)



      
      #print('Color set to: ' + str(effectColor[0]))
      time.sleep(1)

      #if a color is set other than nothing
      if effectColor[0] != off:
         if '!on' in tweet.text.lower():
            ledOn(effectColor[0])
            pixels.show()
            print('Single led is on and ' + effectColorString[0] + '.')
         elif '!fullon' in tweet.text.lower():
            fullOn(effectColor[0])
            pixels.show()
            print('All leds are on and ' + effectColorString[0] + '.')
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

#initialize stream
stream = MyStream(bearer_token=creds['BEARER_TOKEN'])
for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

#start stream
stream.filter() 
  