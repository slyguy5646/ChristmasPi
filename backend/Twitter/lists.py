import tweepy
from Twitter.keys import creds
from Lights.color import *
# Authenticate to Twitter
client = tweepy.Client(creds['BEARER_TOKEN'], creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])
auth = tweepy.OAuth1UserHandler(creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth)


#STATUS LISTS
effectColor = [off]
effectColorString = ['off']
currentEffectString = ['off']
status = ['off']
whileEffectList = [0]

#all of the text tweets from the current session
piTweetIds = [0] 

#filter words
commands = ['@pi_lights']

#gets user screen name and id from tweet
userList = ['hi', 'hello'] 

#different error messages that can be sent
statusTweet = ['Are you sure you specified an effect? Please try again.', 'Are you sure you specified a color? Please try again.']
tweetList = [0]

#this value is assigned in the on_tweet. It is stored for use in an error message until the next tweet.
tweetIdForReply = [0] 

#tweet.text and tweet.id key value pair for use in checking if that tweet has already been sent by @PI_LIGHTS
tweetTextId = {0:0}