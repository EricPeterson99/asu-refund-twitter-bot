import tweepy
import timeit
import time

from local import login, follow, status, mentions


def follow_back(api):
    follow.follow_followers(api)
    return


def follow_new_users(api, key_phrases):
    follow.follow_new_users(api, key_phrases)
    return


def like_related_post():
    return


def like_comments():
    return


def post_status():
    status.create_status()
    return


def like_mentions(api):
    mentions.check_mentions(api, 1)
    return


def main():
    api = login.twitter_login()

    while True:
        time_start = timeit.timeit()

        # post_status(api)
        like_mentions(api)
        follow_back(api)
        follow_new_users(
            api, ['asu refund', 'crow refund', 'Michael Crow Refund', 'arizona state refund'])

        # compute time taken and sleep for 24 hours since start
        time_elasped = timeit.timeit() - time_start
        time.sleep((60 * 60 * 24) - time_elasped)


if __name__ == "__main__":
    main()
