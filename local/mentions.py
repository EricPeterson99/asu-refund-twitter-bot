import tweepy
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def check_mentions(api, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)

        if not tweet.user.following:
            tweet.user.follow()

        if not tweet.favorited:
            # Mark it as Liked, since we have not done it yet
            try:
                tweet.favorite()
                logger.info(f"Liking {tweet.user.name}")
            except Exception as e:
                logger.error("Error on fav", exc_info=True)

        # api.update_status(
        #     status="Please reach us via DM",
        #     in_reply_to_status_id=tweet.id,
        #     )
    return new_since_id
