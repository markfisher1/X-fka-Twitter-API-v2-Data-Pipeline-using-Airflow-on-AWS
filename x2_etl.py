import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

# Replace with your actual Bearer Token (from Twitter Developer Portal)
bearer_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Initialize Tweepy Client (API v2)
client = tweepy.Client(bearer_token=bearer_token)

# Get user ID from username
user = client.get_user(username="fisherwayy")
user_id = user.data.id

# Fetch recent tweets (max 100 at a time)
tweets = client.get_users_tweets(id=user_id, max_results=100)

# Convert tweets to a DataFrame
#if tweets.data:
#    df = pd.DataFrame([tweet.text for tweet in tweets.data], columns=["Tweet"])
#    print(df)
#else:
#    print("No tweets found.")


tweet_list = []
for tweet in tweets.data:
    tweet_list.append(tweet.text)

    refined_tweet = {"user": tweet.user.screen_name, 'text' : text, 'favorite_count' : tweet.favorite_count,'retweet_count' : tweet.retweet_count, "tweet": tweet.text, "created_at": tweet.created_at}

    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list, columns=["Tweet"])
df.to_csv("tweets.csv", index=False)