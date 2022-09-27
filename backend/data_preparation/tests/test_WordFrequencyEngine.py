import datetime

import pytest

from data_preparation.data_processing.TweetProcessingEngine import TweetProcessingEngine
from data_preparation.data_processing.WordFrequencyEngine import WordFrequencyEngine
import time

tpe = TweetProcessingEngine()
wfe = WordFrequencyEngine()


def test_rough_iterate_method():
    s_time = time.time()
    userid = 44196397
    res = tpe.freq_life_time(userid)
    # print(res)
    sorted_res = sorted(res.items(), key=lambda x: x[1])
    # pprint(sorted_res)
    e_time = time.time()
    print()
    print(f"Time Cost = {e_time - s_time} ")


@pytest.mark.timeout(99999999)
def test_spacy_token():
    s_time = time.time()
    userid = 44196397
    tpe.test_portal(userid, wfe.spacy_tokenization)

    e_time = time.time()
    print(f"Time Cost = {e_time - s_time} ")


def test_get_at_user():
    test_str = """
I like #nylas but I don't like to go to this apple.com?a#url. I also don't like the ### comment blocks. But #msft is cool. #really, sd 
@Hello how are @you doing @my_friend, email @000 me @ whats.up@example.com @shahmirj
🇧🇫 🇧🇮 🇰🇭 🇨🇲 🇨🇦 🇮🇨 🇨🇻 🇧🇶 🇰🇾 🇨🇫 🇹🇩 🇨🇱 🇨🇳 🇨🇽 🇨🇨
😁😛😋🤣
 🌯 🥗 🥘🥫🍝🍜🍲🍛🍣🍱 
"""
    at_l, hash_l, emoji_l = wfe.get_at_n_hash(test_str)
    assert set(emoji_l) == ("🇧🇫")
    assert set(at_l) == ("@Hello", "@you", "@my_friend", "@shahmirj")
    assert set(hash_l) == ("#nylas", "#msft", "#really")


def test_begin_process():
    userid = 1572753901698580480
    # dangerous test
    # tpe.begin_process(userid)


def test_cal_freq():
    userid = 44196397
    start_date = datetime.datetime(1999, 1, 1, 1, 1, 1)
    end_date = datetime.datetime(9999, 1, 1, 1, 1, 1)
    choice = ["at", "emoji", "hash", "word"]
    res = tpe.cal_freq(userid, start_date, end_date, choice)


def test_cal_freq_2():
    userid = 44196397
    start_date = datetime.datetime(1999, 1, 1, 1, 1, 1)
    end_date = datetime.datetime(9999, 1, 1, 1, 1, 1)
    choice = ["word"]
    res = tpe.cal_freq(userid, start_date, end_date, choice)
    print(res)
