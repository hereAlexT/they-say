from data_processing.TweetProcessingEngine import TweetProcessingEngine
from data_collection.TweetCollectionEngine import TweetCollectionEngine
import sys, getopt


def main(argv):
    if argv[0] == "begin_tweet_pre_processing":
        if argv[1] == 'all':
            """python3 main.py begin_tweet_pre_processing all"""
            tpe = TweetProcessingEngine()
            userid_list = tpe.get_distinct_users_on_db()
            for u in userid_list:
                tpe.begin_process(u)
                
    elif argv[0] == "update_tweet":
        if argv[1] == 'all':
            """python3 main.py update_tweet all"""
            tce = TweetCollectionEngine()
            userid_list = tce.get_distinct_users_on_db()
            for u in userid_list:
                tce.insert_new_tweets_by_user(u)


if __name__ == '__main__':
    main(sys.argv[1:])
