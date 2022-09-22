import os
import tweepy
import config
import datetime
from pymongo import MongoClient

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


class BaseEngine:
    def __init__(self):
        self.db_client = MongoClient('mongodb://localhost:27017/')
        self.db = self.db_client[config.DB]
        self.col_raw_tweets = self.db['RawTweets']
        self.api_client = tweepy.Client(bearer_token=BEARER_TOKEN)

    def get_db_client(self):
        return self.db_client

    def get_db(self):
        return self.db

    def get_col_raw_tweets(self):
        return self.col_raw_tweets

    def get_api_client(self):
        return self.api_client

    def get_user_id(self, screen_name):
        return self.api_client.get_user(username=screen_name).data.id
