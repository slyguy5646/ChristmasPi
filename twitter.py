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

# tweets = []

# def appendTweet(tweet):
#    tweets.append(tweet)
#    return tweets



statusTweet = f"The leds are now { effectColor[0] } and { currentEffectString }"
commands = ['@pi_lights']
userList = []

class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      return print('Connected!')
   
   def on_tweet(self, tweet):
      userList.clear()
      mentions = api.mentions_timeline()
      for mention in mentions:
         userList.append(mention.user.screen_name)
      print(str(userList[0]) + ' - ' + tweet.text)
      if '!red' in tweet.text.lower():
         setColor(red)
      elif '!green' in tweet.text.lower():
         setColor(green)
      elif '!blue' in tweet.text.lower():
         setColor(blue)
      elif '!off' in tweet.text.lower():
         setColor(off)
      else:
         print("Twitter didn't tell me a color")

      print('Color set to: ' + str(effectColor[0]))
      time.sleep(1)



      if '!on' in tweet.text.lower():
         ledOn(effectColor[0])
         pixels.show()
         print('Single led is on.')
         client.create_tweet(text=statusTweet)
      elif '!fullon' in tweet.text.lower():
         fullOn(effectColor[0])
         pixels.show()
         print('All leds are on.')
      elif '!off' in tweet.text.lower():
         ledOff()
         pixels.show()
      else:
         print('Twitter didnt tell me an effect')

         
      time.sleep(3)

stream = MyStream(bearer_token=creds['BEARER_TOKEN'])


for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

stream.filter()   

# tweet = []
# hihihi = api.mentions_timeline()

# for mention in hihihi:

#    print(mention.user.screen_name)