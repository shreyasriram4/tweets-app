import tweepy
import pandas as pd

# Credentials

bearer_token = "AAAAAAAAAAAAAAAAAAAAAAI%2BlQEAAAAA%2BgeWj5yGpBS5fP9Ff%2BqDEfbArxE%3DPsAQJjLuyVbYe9JcZvKEjDQvqVM3MB9vnnf9OHF1hZa4IBsqrV"
consumer_key = "Zs5ub4BBK52yUODBt2hFNyuN9"
consumer_secret = "MImM3cvZLv0l0tfzV3rmXuuDRpcpuQDarNanuGmsaFeRDDFFe6"
access_token = "2286497154-IhmAkE7MSnMhOOkZBjYx0dBndWKDASkx7VGbfro"
access_token_secret = "kqndVojOr7OLQULbbdnaK4lSjzk0ULpNvQrcucuTP3FS5"

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