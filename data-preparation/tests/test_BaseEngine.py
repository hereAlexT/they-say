from BaseEngine import BaseEngine

be = BaseEngine()


def test_get_client():
    assert be.get_user_id(screen_name="elonmusk") == 44196397
