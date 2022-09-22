from BaseEngine import BaseEngine

be = BaseEngine()


def test_get_client():
    assert be.get_user_id(screen_name="elonmusk") == 44196397


def test_get_db():
    db = be.get_db()
    assert db.name == "TweetMining"


def test_get_col_raw_tweets():
    col = be.get_col_raw_tweets()
    assert col.name == "RawTweets"

