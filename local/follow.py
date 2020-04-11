import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def follow(follower):
    if not follower.following:
        try:
            logger.info(f"Following {follower.name}")
            follower.follow()
        except Exception as e:
            # if error is not that we already requested to follow them
            return False
    return True


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        follow(follower)


def follow_new_users(api, key_phrases):
    logger.info("Finding and following new users")

    max_tweets = 500
    count = 0

    for query in key_phrases:
        logger.info(f"Seaching query: {query}")
        for tweet in tweepy.Cursor(api.search, q=query, lang="en").items(max_tweets):
            follow(tweet.user)
        logger.info(f"Finished searching query: {query}")
    logger.info("Finsished searching all key phrases")
