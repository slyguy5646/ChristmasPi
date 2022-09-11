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

class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      return print('Connected!')
   
   def on_tweet(self, tweet):
      if '!color' in tweet.text.lower():
         if '!red' in tweet.text.lower():
            effectColor.clear()
            effectColor.append(red)
            print(effectColor[0])
         elif '!green' in tweet.text.lower():
            effectColor.clear()
            effectColor.append(green)
            print(effectColor[0])
         elif '!blue' in tweet.text.lower():
            effectColor.clear()
            effectColor.append(blue)
            print(effectColor[0])
      print('Current Color: ' + str(effectColor[0]))
      time.sleep(5)


      if '!lights' in tweet.text.lower():
         if '!on' in tweet.text.lower():
            ledOn(effectColor[0])
         elif '!fullon' in tweet.text.lower():
            fullOn(effectColor[0])
         elif '!off' in tweet.text.lower():
            ledOff()
      else:
         print('TWITTER DIDNT TELL ME AN EFFECT')
         
      time.sleep(3)

stream = MyStream(bearer_token=creds['BEARER_TOKEN'])


for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

stream.filter()   