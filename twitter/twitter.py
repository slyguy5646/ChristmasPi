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
      if tweet.referenced_tweets == None:
         if '!lights' in tweet.text.lower():
            if '!on' in tweet.text.lower():
               print('on')
            elif '!off' in tweet.text.lower():
               print('off')
         else:
            print('TWITTER DIDNT TELL ME AN EFFECT')
         if '!color' in tweet.text.lower():
            if '!red' in tweet.text.lower():
               print('red')
            elif '!green' in tweet.text.lower():
               print('green')
            elif '!blue' in tweet.text.lower():
               print('blue')
      time.sleep(3)

stream = MyStream(bearer_token=creds['BEARER_TOKEN'])


for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

stream.filter()   