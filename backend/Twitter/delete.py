from Twitter.lists import *

#THE CODE BELOW GETS ALL OF THE IDS FROM @PI_LIGHTS TWEETS
tweetsIds = api.user_timeline(user_id=creds['PI_LIGHTS_ID'])
for tweets in tweetsIds:
    piTweetIds.append(tweets.id)

"""
if a tweet's body matches another tweet:
    delete tweet 
else: 
    tweet message
"""



#checks if tweet that is about to be sent is a duplicate, if so, it deletes the duplicate before sending it
def tweetOrDelete(message):
    if message in tweetTextId.keys():
        tweetToDelete = tweetTextId[message]
        api.destroy_status(tweetToDelete)
        api.update_status(status=message, in_reply_to_status_id=tweetIdForReply[-1])
    else:
        api.update_status(status=message, in_reply_to_status_id=tweetIdForReply[-1])





        
        
