import datetime

import os
import tweepy
from data_preparation.BaseEngine import BaseEngine
import data_preparation.config as config
import logging

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")


class TweetCollectionEngine(BaseEngine):

    def __init__(self):
        super().__init__()

    def get_latest_tweet_on_db(self, userid):
        _filter = {
            'author_id': userid
        }
        _sort = list({
                         'id': -1
                     }.items())
        _limit = 1

        return list(self.get_col_raw_tweets().find(filter=_filter, sort=_sort, limit=_limit))[0]

    def get_time_latest_tweet_on_db(self, userid):
        """
        This is used to query new tweets by API.
        :param userid: the id of user
        :return: the time of the latest tweet on database.
        """
        _filter = {
            'author_id': userid
        }
        _project = {
            'created_at': 1
        }
        _sort = list({
                         'id': -1
                     }.items())
        _limit = 1

        res = list(self.get_col_raw_tweets().find(filter=_filter, sort=_sort, limit=_limit))

        if len(res) > 0:
            return res[0]['created_at']
        else:
            return None

    def get_new_tweets_by_user(self, userid, _start_time=None):
        """
        :param userid:
        :param _start_time:
        :return: [<tweet1>, <tweet2>]
        """
        totally_new_flag = False
        _client = self.get_api_client()
        if _start_time is None:
            _start_time = self.get_time_latest_tweet_on_db(userid)
            print(_start_time)
            if _start_time is None:
                # grab the latest 3200 tweets
                _start_time = datetime.datetime(2011, 11, 6, 1, 1, 1)
                totally_new_flag = True
        _tweets_list = []
        for status in tweepy.Paginator(_client.get_users_tweets, id=userid, max_results=5, limit=1,
                                       tweet_fields=config.TWEET_FIELDS, start_time=_start_time):
            if status.data is not None:
                for i in status.data:
                    _tweets_list.append(i)
        if totally_new_flag is True:
            return _tweets_list
        else:
            return _tweets_list[:-1]

    def insert_new_tweets_by_user(self, userid, _start_time=None):
        logging.info(f"Insert New Tweets [userid = {userid}]")
        _insert_list = self.get_new_tweets_by_user(userid, _start_time)
        _col = self.get_col_raw_tweets()
        count = 0
        for i in _insert_list:
            i = BaseEngine.convert_tweepy_object_to_dict(i)
            print(i)
            count += 1
            _col.insert_one(i)
        logging.info(f"Length of updated_list: {len(_insert_list)}, insert {count} entries.")
        return _insert_list
