from twython import Twython

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
image = open('img2.jpg', 'rb')
response = twitter.upload_media(media=image)
media_id = [response['media_id']]
message = "One of my first fire detection tests!"
twitter.update_status(status=message, media_ids=media_id)
print("TWEETED: " + message)