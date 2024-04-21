import tweepy
import os

auth = tweepy.OAuthHandler(os.environ.get('TWITTER_CONSUMER_API_KEY'), os.environ.get('TWITTER_CONSUMER_API_KEY_SECRET'))

auth.set_access_token(os.environ.get('TWITTER_AUTH_ACCESS_TOKEN'), os.environ.get('TWITTER_AUTH_ACCESS_TOKEN_SECRET'))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")