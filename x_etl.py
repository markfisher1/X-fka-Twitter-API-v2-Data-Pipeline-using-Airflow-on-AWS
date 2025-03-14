import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = '1874219950115598336-8yPlMKWF5WqkF2oEGtvpKvYkFvEz0H'
access_secret = 'a7UCx5WEG0BL7qmr41VoMiHIrcyg4jsA2rUr0EvXFbehK'
consumer_key = 'bs5Wk0MUYhuWnuviGLSKNQOcx'
consumer_secret = 'SW4rbMoSZ0obUB5vlwWEykrLdpKer55SClYFLtVQw44IR8wo1C'

# Authenticate to the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Create API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name="fisherwayy", count=200, tweet_mode="extended")
print(tweets)