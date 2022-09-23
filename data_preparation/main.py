import os
import sys
from pathlib import Path

curPath = Path(os.path.abspath(os.path.dirname(__file__)))
print(str(curPath.parent.absolute()))
sys.path.append(str(curPath.parent.absolute()))

from data_preparation.BaseEngine import BaseEngine
from data_preparation.data_processing.TweetProcessingEngine import TweetProcessingEngine
from data_preparation.data_collection.TweetCollectionEngine import TweetCollectionEngine


def main(argv):
    if argv[0] == "begin_tweet_pre_processing":
        tpe = TweetProcessingEngine()
        if argv[1] == 'all':
            """python3 main.py begin_tweet_pre_processing all"""
            userid_list = tpe.get_distinct_users_on_db()
            for u in userid_list:
                tpe.begin_process(u)
        else:
            """python3 main.py begin_tweet_pre_processing [user_id]"""
            userid = int(argv[1])
            input(f"Are you sure to begin_tweet_pre_processing for this user-> {userid}")
            tpe.begin_process(userid)

    elif argv[0] == "update_tweets":
        tce = TweetCollectionEngine()
        if argv[1] == 'all':
            """python3 main.py update_tweets all"""
            userid_list = tce.get_distinct_users_on_db()
            for u in userid_list:
                tce.insert_new_tweets_by_user(u)
        else:
            userid = argv[1]
            input(f'Your Request userid is {userid}, are you sure to continue?')
            tce.insert_new_tweets_by_user(int(userid))

    elif argv[0] == "get_user_id":
        be = BaseEngine()
        print(be.get_user_id(argv[1]))


if __name__ == '__main__':
    main(sys.argv[1:])
