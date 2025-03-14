import tweepy
import pandas as pd
import os
from datetime import datetime

# Replace with your actual Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP%2BqzwEAAAAAnMPWANQk4k%2FZW6dOaGfRuV9eFZ8%3DQ1H5wEMNBeL7QVagx0keUG3pVbsxZFgLnQUBelpfeCpwNTlCis"

# Initialize Tweepy Client (API v2)
client = tweepy.Client(bearer_token=bearer_token)

# Get user ID from username
username = "fisherwayy"
user = client.get_user(username=username, user_fields=["id", "name", "username"])

if user.data is None:
    print("❌ User not found.")
    exit()

user_id = user.data.id

# Fetch tweets with user expansion
tweets = client.get_users_tweets(
    id=user_id,
    max_results=100,
    tweet_fields=["created_at", "public_metrics"]
)

# Create output folder
output_folder = "./twitter_data/"
os.makedirs(output_folder, exist_ok=True)

# Process tweets
tweet_data = []
if tweets.data:
    for tweet in tweets.data:
        refined_tweet = {
            "user": username,
            "text": tweet.text,
            "favorite_count": tweet.public_metrics["like_count"],
            "retweet_count": tweet.public_metrics["retweet_count"],
            "created_at": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        tweet_data.append(refined_tweet)

    # Convert to DataFrame
    df = pd.DataFrame(tweet_data)

    # Define CSV file path
    csv_filename = f"{output_folder}tweets_{username}.csv"

    # Save to CSV
    df.to_csv(csv_filename, index=False)
    print(f"✅ CSV file saved at: {csv_filename}")

else:
    print("No tweets found.")
