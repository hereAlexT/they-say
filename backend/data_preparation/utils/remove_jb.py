from pymongo import MongoClient
import collections

client = MongoClient('mongodb://localhost:27017/')
db = client.TweetMining
col = db.RawTweets

userid = 27260086

count = 0
col.delete_many({'author_id':27260086})



