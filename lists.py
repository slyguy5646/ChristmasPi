import tweepy
from keys import creds

# Authenticate to Twitter
client = tweepy.Client(creds['BEARER_TOKEN'], creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])
auth = tweepy.OAuth1UserHandler(creds['API_KEY'], creds['API_KEY_SECRET'], creds['ACCESS_TOKEN'], creds['ACCESS_TOKEN_SECRET'])

# Create API object
api = tweepy.API(auth)





commands = ['@pi_lights']
userList = ['fillerSoPythonDoesntYellAtMe']
statusTweet = ['Are you sure you specified an effect? Please try again', 'Are you sure you specified a color? Please try again.']
tweetList = [0]