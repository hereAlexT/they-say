from pymongo import MongoClient
import collections

client = MongoClient('mongodb://localhost:27017/')
db = client.TweetMining
col = db.RawTweets

res = list(col.find(projection={'id': 1, '_id':0}))
new_l = [x['id'] for x in res]

dup_id = [item for item, count in collections.Counter(new_l).items() if count > 1]

count = 0
for i in dup_id:
    res = list(col.find({"id": i}))
    if len(res) > 1:
        col.delete_one({"_id":res[1]["_id"]})
        print(res[0]["_id"])
        count+= 1
        print(f"{count}/{len(dup_id)}")


