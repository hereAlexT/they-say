# Data-Processing

This part of program having the following functions:
- Collect the tweets
- Analyse the tweets

## How to store keys
I suggest to using the following way to import auth keys.
This code below is referenced from [here](https://github.com/twitterdev/Twitter-API-v2-sample-code).

```
# To set your enviornment variables in your terminal run the following line:
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
```