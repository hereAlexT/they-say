PROJECT_NAME = "TweetMining-Data-Preparation"
LOGGER_NAME = "TMDP"
TWEET_FIELDS = ['attachments', 'author_id', 'context_annotations', 'conversation_id', 'created_at', 'entities', 'geo',
                'in_reply_to_user_id', 'lang', 'possibly_sensitive', 'referenced_tweets',
                'reply_settings', 'source', 'withheld']
USER_FIELDS = ['id', 'name', 'username', 'created_at', 'description', 'entities', 'location', 'pinned_tweet_id',
               'profile_image_url', 'protected', 'public_metrics', 'url', 'verified', 'withheld']
DB = "TweetMining"
VALID_CHAR = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
LOWER_CASE_CHAR = "abcdefghijklmnopqrstuvwxyz"
