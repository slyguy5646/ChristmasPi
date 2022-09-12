from multiprocessing.connection import Client
from light import *
from keys import creds
import tweepy
import time

# Authenticate to Twitter
client = tweepy.Client(creds['BEARER_TOKEN'], creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])
auth = tweepy.OAuth1UserHandler(creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth)

tweets = []

def appendTweet(tweet):
   tweets.append(tweet)
   return tweets


commands = ['@pi_lights']
userIdList = []

class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      return print('Connected!')
   
   def on_tweet(self, tweet):
      userIdList.clear()
      userId = api.mentions_timeline()
      for user in userId:
         userIdList.append(user.user.screen_name)
      print(str(userIdList[0]) + ' - ' + tweet.text)
      if '!red' in tweet.text.lower():
         effectColor.clear()
         effectColor.append(red)
      elif '!green' in tweet.text.lower():
         effectColor.clear()
         effectColor.append(green)
      elif '!blue' in tweet.text.lower():
         effectColor.clear()
         effectColor.append(blue)
      elif '!off' in tweet.text.lower():
         effectColor.clear()
         effectColor.append(off)
      else:
         print("Twitter didn't tell me a color")

      print('Color set to: ' + str(effectColor[0]))
      time.sleep(1)



      if '!on' in tweet.text.lower():
         if effectColor[0] != off:
            ledOn(effectColor[0])
            print('Single led is on.')
         elif effectColor == off:
            api.update_status("You didn't specify a color! Please try again.")
      elif '!fullon' in tweet.text.lower():
         fullOn(effectColor[0])
         print('All leds are on.')
      elif '!off' in tweet.text.lower():
         ledOff()
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