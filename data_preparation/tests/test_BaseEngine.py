import datetime

from data_preparation.BaseEngine import BaseEngine

be = BaseEngine()


def test_get_client():
    be.get_user_id(screen_name="ednaisfaqwASDf")
    # assert be.get_user_id(screen_name="elonmusk") == 44196397


def test_get_db():
    db = be.get_db()
    assert db.name == "TweetMining"


def test_get_col_raw_tweets():
    col = be.get_col_raw_tweets()
    assert col.name == "RawTweets"


def test_get_tweets_by_user_on_db():
    end_time = datetime.datetime(2011, 12, 3, 18, 22, 8)
    start_time = datetime.datetime(1999, 1, 1, 1, 1, 1)
    re = be.get_tweets_by_user_on_db(44196397, start_time, end_time)
    assert len(list(re)) == 5

def test_get_distinct_user_on_db():
    a = be.get_distinct_users_on_db()
    print(a)