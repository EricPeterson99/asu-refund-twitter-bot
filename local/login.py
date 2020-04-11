import tweepy
from local import credentials


def twitter_login():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY,
                               credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN,
                          credentials.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    # Create API object
    return api
