from lists import *

#THE CODE BELOW GETS ALL OF THE TWEET IDS FROM @PI_LIGHTS
# piTweetIds = [0]
# tweetsIds = api.user_timeline(user_id=creds['PI_LIGHTS_ID'])
#       for tweets in tweetsIds:
#          piTweetIds.append(tweets.text)

"""
if a tweet's body matches another tweet:
    delete tweet 
else: 
    tweet message
"""




def tweetOrDelete(message, user):
    if message in tweetList:
        tweetList.remove(message)
        api.update_status(status=message, in_reply_to_status_id=user)
    else:
        api.update_status(status=message, in_reply_to_status_id=user)


def checkTweet(message, user):
    if message in tweetList == message:
        pass
    else:
        api.update_status(status=message, in_reply_to_status_id=user)


        
        
