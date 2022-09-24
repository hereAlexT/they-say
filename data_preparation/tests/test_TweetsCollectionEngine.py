import datetime

from data_preparation.BaseEngine import BaseEngine

from data_preparation.data_collection.TweetCollectionEngine import TweetCollectionEngine
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


def test_get_new_tweets_by_user_3():
    s_name = "elonmusk"
    userid = tce.get_user_id(screen_name=s_name)
    userid = 27260086
    res = tce.get_new_tweets_by_user(userid)
    pprint(res)


# dangerous test !!!!!!!!!!!!!!!!!!
# dangerous test !!!!!!!!!!!!!!!!!!
# dangerous test !!!!!!!!!!!!!!!!!!
# dangerous test !!!!!!!!!!!!!!!!!!
def test_insert_new_tweets_by_user():
    # time = datetime.datetime.fromisoformat("2022-09-21T17:02:32.000+00:00")
    # print(time)
    # s_name = "elonmusk"
    # userid = tce.get_user_id(screen_name=s_name)
    userid = 27260086
    res = tce.insert_new_tweets_by_user(userid)
    pprint(res)


# def test_insert_new_tweets_by_user_2():
#     s_name = "elonmusk"
#     userid = tce.get_user_id(screen_name=s_name)
#     res = tce.insert_new_tweets_by_user(userid)
#     pprint(res)


def test_user_lookup_1():
    ids = [27260086, 44196397]
    l = tce.users_lookup(ids, compare_save=True)
    assert len(l) == 2
    # print(l)
    # for i in l:
    #     print(i.data)


def test_user_lookup_2():
    ids = [27260086]
    l = tce.users_lookup(ids, compare_save=True)
    # assert len(l) == 1
    # print(l)
    # for i in l:
    #     print(i.data)


def test_user_lookup_3():
    ids = [27260086, 44196397]
    l = tce.users_lookup(ids, compare_save=True)
    # assert len(l) == 0

def test_get_distinct_user_info_from_db():
    res = tce.get_distinct_user_on_db()
    print()
    pprint(list(res))
