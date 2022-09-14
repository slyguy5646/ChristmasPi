from collections import UserList
from multiprocessing.connection import Client
from light import *
from set import setColor
from keys import creds
import tweepy
import time

# Authenticate to Twitter
client = tweepy.Client(creds['BEARER_TOKEN'], creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])
auth = tweepy.OAuth1UserHandler(creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth)


commands = ['@pi_lights']
userList = ['fillerSoPythonDoesntYellAtMe']
statusTweet = ['Are you sure you specified an effect? Please try again', 'Are you sure you specified a color? Please try again.']

class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      return print('Connected!')
   
   def on_tweet(self, tweet):
      userList.clear()
      mentions = api.mentions_timeline()

      for mention in mentions:
         print(mention.text)
         userList.append(mention.user.screen_name)
         userList.append(mention.id)
      if '!red' in tweet.text.lower():
         setColor(red)
      elif '!green' in tweet.text.lower():
         setColor(green)
      elif '!blue' in tweet.text.lower():
         setColor(blue)
      elif '!off' in tweet.text.lower():
         setColor(off)
      else:
         api.update_status(status=statusTweet[1], in_reply_to_status_id=userList[1])



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
      else:
         api.update_status(status=statusTweet[0], in_reply_to_status_id=userList[1])

         
      # currentColor = effectColorString[0]
      # currentEffect = currentEffectString[0]
      # statusTweet.append(f"@{ userList[0] } The leds are now { currentColor } and { currentEffect }")
      # # api.update_status(status=statusTweet[0], in_reply_to_status_id=userList[1])
      time.sleep(3)

stream = MyStream(bearer_token=creds['BEARER_TOKEN'])


for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

stream.filter() 
  