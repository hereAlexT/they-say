from BaseEngine import BaseEngine
from data_processing.TweetProcessingEngine import TweetProcessingEngine
from data_collection.TweetCollectionEngine import TweetCollectionEngine
import sys, getopt


def main(argv):
    if argv[0] == "begin_tweet_pre_processing":
        tpe = TweetProcessingEngine()
        if argv[1] == 'all':
            """python3 main.py begin_tweet_pre_processing all"""
            userid_list = tpe.get_distinct_users_on_db()
            for u in userid_list:
                tpe.begin_process(u)
        elif argv[1] == "userid":
            userid = int(argv[2])
            input("Are you sure to begin_tweet_pre_processing for this user")
            tpe.begin_process(userid)

    elif argv[0] == "update_tweets":
        tce = TweetCollectionEngine()
        if argv[1] == 'all':
            """python3 main.py update_tweets all"""
            userid_list = tce.get_distinct_users_on_db()
            for u in userid_list:
                tce.insert_new_tweets_by_user(u)
        else:
            print(-111)
            userid = argv[1]
            input(f'Your Request userid is {userid}, are you sure to continue?')
            tce.insert_new_tweets_by_user(int(userid))

    elif argv[0] == "get_user_id":
        be = BaseEngine()
        print(be.get_user_id(argv[1]))

if __name__ == '__main__':
    main(sys.argv[1:])
