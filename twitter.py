import tweepy
import time
from Lights.light import *
from Flask.set import effectColor
from Twitter.keys import creds
from Twitter.delete import tweetOrDelete
from Twitter.lists import *
from Lights.color import *
from Twitter.twitter_functions import setList0, checkForColorTweet, checkForEffectTweet, checkForOffTweet


def reply(msg, usr):
   api.update_status(status = msg, in_reply_to_status_id = usr)


class MyStream(tweepy.StreamingClient):
   def on_connect(self):
      api.update_profile(description='Pi Lights is Online! 🎄') #change bio of @pi_lights when bot goes online
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

#########################CHECK FOR COLORS###############################
      checkForOffTweet(tweet)                                  #OFF
      checkForColorTweet(red, '!red', tweet)                   #RED
      checkForColorTweet(green, '!green', tweet)               #GREEN
      checkForColorTweet(blue, '!blue', tweet)                 #BLUE
      checkForColorTweet(orange, '!orange', tweet)             #ORANGE
      checkForColorTweet(yellow, '!yellow', tweet)             #YELLOW
      checkForColorTweet(lightGreen, '!lightgreen', tweet)     #LIGHTGREEN
      checkForColorTweet(powderBlue, '!powderblue', tweet)     #POWDERBLUE
      checkForColorTweet(purple, '!purple', tweet)             #PURPLE
      checkForColorTweet(pink, '!pink', tweet)                 #PINK
########################################################################


      
      print('Color set to: ' + str(effectColor[0]))
      time.sleep(1)

#########################CHECK FOR EFFECTS##############################
      if effectColor[0] != off: #if color is anything but off...
         checkForEffectTweet(ledOn(effectColor[0]), '!on', 'on', tweet, api)             #check for single on command
         checkForEffectTweet(fullOn(effectColor[0]), '!fullon', 'all on', tweet, api)        #check for full on command
      elif effectColor[0] == off: #if color is off...
         checkForEffectTweet(ledOff(), '!off', 'off', tweet, api)                         #check for off command
      
      elif effectColor[0] != off or effectColor[0] == off and '!off' not in tweet.text.lower():
         tweetOrDelete(f'@{ userList[-2] } ' + statusTweet[0])                #tweet no color error message
########################################################################
      time.sleep(.5)

   def on_disconnect(self):
      api.update_profile(description="Pi Lights is sleeping 💤")              #change the bio of @pi_lights when the bot is offline
      return print('Disconnected!')

#initialize stream
stream = MyStream(bearer_token=creds['BEARER_TOKEN'])

#add filter rules (in this case only look for tweets that contain the @pi_lights handle in the body of the tweet)
for command in commands:
   stream.add_rules(tweepy.StreamRule(command))

#start stream
stream.filter() 
  