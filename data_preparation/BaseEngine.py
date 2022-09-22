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

    def get_tweets_by_user_on_db(self, userid, start_time, end_time):
        q = {
            'author_id': userid,
            'created_at': {
                '$gte': start_time,
                '$lt': end_time
            }
        }
        return self.col_raw_tweets.find(q)

    @staticmethod
    def convert_tweepy_object_to_dict(t):
        refer_tweets = []
        if t.referenced_tweets is not None:
            for i in t.referenced_tweets:
                refer_tweets.append(i.data)

        _d = {'author_id': t.author_id,
              'context_annotations': t.context_annotations,
              'conversation_id': t.conversation_id,
              'created_at': t.created_at,
              'entities': t.entities,
              'id': t.id,
              'in_reply_to_user_id': t.in_reply_to_user_id,
              'lang': t.lang,
              'possibly_sensitive': t.possibly_sensitive,
              'referenced_tweets': refer_tweets,
              'reply_settings': t.reply_settings,
              'source': t.source,
              'text': t.text,
              'data_from': "api"}

        return _d
