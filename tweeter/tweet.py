import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

# TWITTER API CREDENTIALS 
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


# The app and the corresponding credentials must have the Write permission
def tweet(tweet):
    response = client.create_tweet(
        text = tweet
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")


