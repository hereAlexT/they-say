import sys

import datetime

import os
import tweepy
from data_preparation.BaseEngine import BaseEngine
import data_preparation.config as config
import logging
from pprint import pprint

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
            _col.insert_one(i)
        logging.info(f"Length of updated_list: {len(_insert_list)}, insert {count} entries.")
        return _insert_list

    def users_lookup(self, userids: list, compare_save=False):
        if len(userids) == 0:
            return []
        _client = self.get_api_client()
        res = []
        for i in range(0, len(userids), 99):
            res += _client.get_users(ids=userids[i:i + 99], user_fields=config.USER_FIELDS).data
        # compare and only save the latest profile
        if compare_save is True:
            for user in res:
                udata = user
                sort = list({'created_at': -1}.items())
                user2 = list(self.get_col_users().find({'id': udata['id']}, sort=sort))
                if len(user2) == 0 or TweetCollectionEngine.user_compare(user1=udata.data, user2=user2[0]) is False:
                    _ud = {
                        'save_time': datetime.datetime.now(),
                        'created_at': udata['created_at'],
                        'username': udata['username'],
                        'location': udata['location'],
                        'profile_image_url': udata['profile_image_url'],
                        'id': udata['id'],
                        'url': udata['url'],
                        'public_metrics': udata['public_metrics'],
                        'name': udata['name'],
                        'pinned_tweet_id': udata['pinned_tweet_id'],
                        'protected': udata['protected'],
                        'verified': udata['verified'],
                        'description': udata['description'],
                        'entities': udata['entities'],
                        'withheld': udata['withheld']
                    }
                    self.get_col_users().insert_one(_ud)
        return res

    @staticmethod
    def user_compare(user1, user2):
        """
        :param user1: dict
        :param user2: dict
        :return:  Same = True, Different = False
        """

        key_to_compare = ['username', 'location', 'profile_image_url', 'name', 'protected', 'verified', 'description']
        for _k in key_to_compare:
            try:
                if user1[_k] != user2[_k]:
                    return False
            except KeyError as e:
                continue
        return True

    def get_distinct_user_profile_on_db(self):
        sort = list({'save_time': -1}.items())
        # res = self.get_col_users().distinct("id")
        res = self.get_col_users().aggregate(
            [
                # {"$match": {"available": True}},
                {"$sort": {"save_time": -1}},
                {"$group":
                    {
                        "_id": "$id",
                        "save_time": {
                            "$first": "$save_time"},
                        "o_id": {
                            "$first": "$_id"
                        }
                    }},
                # {"$project": {
                #     "o_id": 1,
                #     "save_time": 0,
                # }}
            ])
        res2 = []
        for i in list(res):
            project = {
                '_id': 0,
                'id': 1,
                'username': 1,
                'name': 1,
            }
            res2.append(list(self.get_col_users().find({"_id": i["o_id"]}, projection=project))[0])

        return list(res2)
