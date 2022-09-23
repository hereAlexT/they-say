import os
import tweepy
import datetime
from pymongo import MongoClient

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
print(BEARER_TOKEN)
client = tweepy.Client(bearer_token=BEARER_TOKEN)

userName = 'elonmusk'
userID = client.get_user(username=userName).data.id
# print(userID.data.id)

start_time = datetime.datetime(2022, 9, 1, 1, 1, 1).isoformat() + 'Z'
end_time = datetime.datetime(2022, 10, 20, 1, 1, 1).isoformat() + 'Z'

TWEET_FIELDS = ['attachments', 'author_id', 'context_annotations', 'conversation_id', 'created_at', 'entities', 'geo',
                'in_reply_to_user_id', 'lang', 'possibly_sensitive', 'referenced_tweets',
                'reply_settings', 'source', 'withheld']

# tweets = client.get_users_tweets(id=userID, max_results=5, tweet_fields=TWEET_FIELDS)

# trying using cursor
l = []
for status in tweepy.Paginator(client.get_users_tweets, id=userID, max_results=1, limit=1, tweet_fields=TWEET_FIELDS):
    for i in status.data:
        l.append(i)


o_l = []
for t in l:
    refer_tweets = []
    if t.referenced_tweets is not None:
        for i in t.referenced_tweets:
            refer_tweets.append(i.data)

    _d = {'author_id': t.author_id,
          'context_annotations': t.context_annotations,
          'conversation_id': t.conversation_id,
          'created_at': t.created_at,
          'entities': t.entities,
          'id': t.id,
          'in_reply_to_user_id': t.in_reply_to_user_id,
          'lang': t.lang,
          'possibly_sensitive': t.possibly_sensitive,
          'referenced_tweets': refer_tweets,
          'reply_settings': t.reply_settings,
          'source': t.source,
          'text': t.text,
          'data_from': "api"}

    o_l.append(_d)

# client = MongoClient('mongodb://localhost:27017/')
# db = client.TweetMiningTest
# col = db.RawTweets
#
# count = 0
# for i in o_l:
#     count += 1
#     col.insert_one(i)
#     print(f"{count}/{len(o_l)}")
