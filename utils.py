import tweepy
import pandas as pd

# Credentials

bearer_token = "xxx"
consumer_key = "xxx"
consumer_secret = "xxx"
access_token = "xxx"
access_token_secret = "xxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def username_tweets(username,count):

    count = int(count)      
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.user_timeline,screen_name=username).items(count)

    # Pulling information from tweets iterable object
    tweets_list = [[tweet.created_at, tweet.text] for tweet in tweets]

    # Creation of dataframe from tweets list
    tweets_df = pd.DataFrame(tweets_list,columns=['Datetime', 'Text'])

    return tweets_df
