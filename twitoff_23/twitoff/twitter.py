""" Handles connection to Twitter API using Tweepy"""

import tweepy
import spacy
from os import getenv
from .models import DB, Tweet, User

TWITTER_API_KEY = getenv('TWITTER_API_KEY')

TWITER_API_KEY_SECRET = getenv('TWITER_API_KEY_SECRET')

TWITTER_AUTH = tweepy.OAuthHandler(TWITTER_API_KEY, TWITER_API_KEY_SECRET)
TWITTER = tweepy.API(TWITTER_AUTH)

nlp = spacy.load("my_model/")

def vectorize_tweet(tweet_text):
    return nlp(tweet_text).nevtor

def add_or_update_user(username):
    """ pulls a username from twitter api """
    twitter_user = TWITTER.get_user(username)
    db_user = (User.query.get(twitter_user.id)) or User(id=twitter_user.id, name=username)
    DB.session.add(db_user)

    tweets = twitter_user.timeline(
        count = 200, exclude_replies=True, include_rts=False,
        tweet_mode="extended"
    )

    for tweet in tweets:
        db_tweet = Tweet(id=tweet.id, text=tweet.full_text[:300])
        db_user.tweets.append(db_tweet)
        DB.session.add(db_tweet)
    
    DB.session.commit()