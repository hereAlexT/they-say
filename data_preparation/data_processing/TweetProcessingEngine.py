import config
from BaseEngine import BaseEngine
import datetime
import time
from data_processing.WordFrequencyEngine import WordFrequencyEngine
from emoji import EMOJI_DATA

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
            val = list(col_raw_tweets.find({"id": i}, projection={'id': 1, 'text': 1, '_id': -1, 'created_at': 1}))
            text = val[0]['text']
            token = self.freqEngine.spacy_tokenization(text)
            # remove emoji
            new_token = []
            for i in token:
                if i not in EMOJI_DATA:
                    new_token.append(i)
            token = new_token

            at_l, hash_l, emoji_l = self.freqEngine.get_at_n_hash(text)
            e_time = time.time()
            logger.debug(f" Processing time cost = {e_time - s_time}")

            _d = {'id': val[0]['id'],
                  'author_id': userid,
                  'created_at': val[0]['created_at'],
                  'words_list': token,
                  'at': at_l,
                  "emoji": emoji_l,
                  'hash': hash_l}

            col_processed.insert_one(_d)
            count += 1
            print(f"Progress: {count}/{total} ")

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

    def cal_freq(self, userid, start_date, end_date):
        # fetch data
        res = list(self.get_col_processed().find({'author_id': userid},
                                                 projection={'_id': 0, 'id': 1, 'words_list': 1, 'at': 1, 'emoji': 1,
                                                             'hash': 1}))
        s_time = time.time()
        freq_words_l = self._cal_freq(res, attr_name='words_list')
        freq_at_l = self._cal_freq(res, attr_name='at')
        freq_emoji_l = self._cal_freq(res, attr_name='emoji')
        freq_hash_l = self._cal_freq(res, attr_name='hash')

        e_time = time.time()
        print(f"timecost = {e_time - s_time}\n len(res)={len(res)}")

        return freq_words_l, freq_at_l, freq_emoji_l, freq_hash_l


    @staticmethod
    def _cal_freq(res, attr_name):
        freq_l = {}
        for i in res:
            for w in i[attr_name]:
                if w in freq_l:
                    freq_l[w] += 1
                else:
                    freq_l[w] = 1
        return freq_l
