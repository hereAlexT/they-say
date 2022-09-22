import os
import tweepy
from BaseEngine import BaseEngine

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


class TweetsCollectionEngine(BaseEngine):

    def __init__(self):
        super().__init__()


    def get_latest_tweet_by_user(self, userid):
        # todo get the datetime of last entry in db
        # todo get from that time to now
        pass

    def get_all_tracking_user(self):
        #todo get distinct user_id from db
        pass


