import config
from BaseEngine import BaseEngine
import datetime
import time
from data_processing.WordFrequencyEngine import WordFrequencyEngine

from my_logging import logger


class TweetProcessingEngine(BaseEngine):

    def __init__(self):
        super().__init__()
        self.freqEngine = WordFrequencyEngine()

    def freq_life_time(self, userid):
        now = datetime.datetime.now()
        past = datetime.datetime(1888, 1, 1, 1, 1, 1)
        _project = {'text': 1}
        t_list = list(self.get_tweets_by_user_on_db(userid=userid, start_time=past, end_time=now, projection=_project))
        # combine them to strings
        target_s = ""
        for i in t_list:
            target_s += i['text']

        return WordFrequencyEngine.rough_tokenization(target_s)

    def begin_process(self, userid):
        col_processed = self.get_col_processed()
        col_raw_tweets = self.get_col_raw_tweets()

        project = {'id': 1, "_id": 0}
        all_id_from_cal_raw = list(col_raw_tweets.find({"author_id": userid}, projection=project))
        all_id_from_processed = list(col_processed.find({"author_id": userid}, projection=project))
        l_cal_raw = [x['id'] for x in all_id_from_cal_raw]
        l_processed = [x['id'] for x in all_id_from_processed]
        need_process = list(set(l_cal_raw) - set(l_processed))

        total = len(need_process)
        count = 0
        for i in need_process:
            s_time = time.time()
            val = list(col_raw_tweets.find({"id": i}, projection={'id': 1, 'text': 1, '_id': -1}))
            text = val[0]['text']
            token = self.freqEngine.spacy_tokenization(text)
            at_l, hash_l = self.freqEngine.get_at_n_hash(text)
            e_time = time.time()
            logger.debug(f" Processing time cost = {e_time - s_time}")

            _d = {'id': val[0]['id'],
                  'words_list': token,
                  'at': at_l,
                  'hash': hash_l}

            col_processed.insert_one(_d)
            count += 1
            print(f"Progress: {count}/{total} ")

            # todo: store

    def test_portal(self, userid, method):
        now = datetime.datetime.now()
        past = datetime.datetime(1888, 1, 1, 1, 1, 1)
        _project = {'text': 1}
        t_list = list(self.get_tweets_by_user_on_db(userid=userid, start_time=past, end_time=now, projection=_project))
        # combine them to strings
        target_s = ""
        for i in t_list:
            target_s += i['text']

        return method(target_s)
