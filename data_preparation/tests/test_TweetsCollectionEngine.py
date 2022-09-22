import datetime

from BaseEngine import BaseEngine

from data_collection.TweetCollectionEngine import TweetCollectionEngine
from pprint import pprint

tce = TweetCollectionEngine()


def test_get_latest_tweet_on_db():
    s_name = "elonmusk"
    userid = tce.get_user_id(screen_name=s_name)
    res = tce.get_latest_tweet_on_db(userid)
    print("-----")
    pprint(res)


def test_get_time_latest_tweet_on_db():
    s_name = "elonmusk"
    userid = tce.get_user_id(screen_name=s_name)
    res = tce.get_time_latest_tweet_on_db(userid)
    assert type(res) is datetime.datetime
    pprint(res)


def test_get_new_tweets_by_user():
    s_name = "elonmusk"
    userid = tce.get_user_id(screen_name=s_name)
    res = tce.get_new_tweets_by_user(userid)
    pprint(res)


def test_get_new_tweets_by_user_2():
    time = datetime.datetime.fromisoformat("2022-09-21T17:02:32.000+00:00")
    print(time)
    s_name = "elonmusk"
    userid = tce.get_user_id(screen_name=s_name)
    res = tce.get_new_tweets_by_user(userid, _start_time=time)
    pprint(res)

# dangerous test !!!!!!!!!!!!!!!!!!
# dangerous test !!!!!!!!!!!!!!!!!!
# dangerous test !!!!!!!!!!!!!!!!!!
# dangerous test !!!!!!!!!!!!!!!!!!
# def test_insert_new_tweets_by_user():
#     time = datetime.datetime.fromisoformat("2022-09-21T17:02:32.000+00:00")
#     print(time)
#     s_name = "elonmusk"
#     userid = tce.get_user_id(screen_name=s_name)
#     res = tce.insert_new_tweets_by_user(userid, _start_time=time)
#     pprint(res)

# def test_insert_new_tweets_by_user_2():
#     s_name = "elonmusk"
#     userid = tce.get_user_id(screen_name=s_name)
#     res = tce.insert_new_tweets_by_user(userid)
#     pprint(res)
