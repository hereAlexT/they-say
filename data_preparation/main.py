from data_processing.TweetProcessingEngine import TweetProcessingEngine
import sys, getopt


def main(argv):
    if argv[0] == "begin_tweet_pre_processing":
        if argv[1] == 'all':
            """python3 main.py begin_tweet_pre_processing all"""
            tpe = TweetProcessingEngine()
            userid_list = tpe.get_distinct_users_on_db()
            for u in userid_list:
                tpe.begin_process(u)


if __name__ == '__main__':
    main(sys.argv[1:])
