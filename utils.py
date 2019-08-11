#Bibliotheken
import nltk
nltk.download('punkt')
import tweepy
from textblob_de import TextBlobDE
from textblob import TextBlob
import numpy as np
import pandas as pd
import config

def authenticate():
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)

    api = tweepy.API(auth)
    return api

def searchTweets(string):
    public_tweets = authenticate().search(string)
    return public_tweets

def analyzeTweet(tweet):
    analysis = TextBlob(tweet.text)  
    return analysis.sentiment

def createDataFrame(searchValue):
    api = authenticate()
    public_tweets = api.search(searchValue)
    df = pd.DataFrame()
    for tweet in public_tweets:
        text = tweet.text
        analysis = analyzeTweet(tweet)
        time = tweet.created_at
        df = df.append({'Tweet': text,'Sentiment': analysis, 'Timestamp': time}, ignore_index=True)
    return df