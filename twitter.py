""" 
    EXT. Title: Posting to Twitter via RPi
    Author: Fin Mead, Meadeor.
    Desc:Functional test script for posting to twitter - both tweets and media (For the NXP HoverGames Competition//hackster.io)
"""
#imports
from twython import Twython
#importing Twitter API keys/tokens/secrets
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
#assigning keys/token variables
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
#upload image/text tweet
image = open('img.jpg', 'rb') #replace with own image//directory
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
message = "One of my first fire detection tests!" #replace with your own message
twitter.update_status(status=message, media_ids=media_id)
print("TWEETED: " + message)#return print
