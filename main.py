# import tweepy
import datetime
import random

CURRENT_DATE = datetime.datetime.now()
START_DATE_OF_CORONA = datetime.datetime(2020, 3, 15)
DAYS_ELAPSED = (CURRENT_DATE - START_DATE_OF_CORONA).days

DAYS_IN_SEMESTER = 117

AVG_DORM_COST = 4492 / DAYS_IN_SEMESTER
AVG_MEAL_PLAN_COST = 3358 / DAYS_IN_SEMESTER
AVG_PARKING_COST = 495 / DAYS_IN_SEMESTER


def computeCost(type):
    if(type.lower() == 'ddorm'):
        return '${:,.2f}'.format(AVG_DORM_COST)

    elif(type.lower() == 'dmeal'):
        return '${:,.2f}'.format(AVG_MEAL_PLAN_COST)

    elif(type.lower() == 'dparking'):
        return '${:,.2f}'.format(AVG_PARKING_COST)

    elif(type.lower() == 'tdorm'):
        return '${:,.2f}'.format(AVG_DORM_COST * DAYS_ELAPSED)

    elif(type.lower() == 'tmeal'):
        return '${:,.2f}'.format(AVG_MEAL_PLAN_COST * DAYS_ELAPSED)

    elif(type.lower() == 'tparking'):
        return '${:,.2f}'.format(AVG_PARKING_COST * DAYS_ELAPSED)

    elif(type.lower() == 'ddormmeal'):
        return '${:,.2f}'.format(AVG_DORM_COST + AVG_MEAL_PLAN_COST + AVG_PARKING_COST)

    elif(type.lower() == 'dall'):
        return '${:,.2f}'.format(AVG_DORM_COST + AVG_MEAL_PLAN_COST + AVG_PARKING_COST)

    elif(type.lower() == 'tall'):
        return '${:,.2f}'.format((AVG_DORM_COST + AVG_MEAL_PLAN_COST + AVG_PARKING_COST) * DAYS_ELAPSED)

    return


def loadPost():
    f = open("messages.txt", "r")
    tweets = []

    for line in f:
        for word in line.split():
            if '{' in word and '}' in word:  # Replace field with value
                line = line.replace(word, computeCost(word[1:-1]))
        tweets.append(line[:-1])  # remove new line

    return tweets


def createPost(postIndex=-1):
    tweets = loadPost()

    if postIndex == -1:  # random
        postIndex = random.randrange(0, len(tweets) - 1)

    return tweets[postIndex]


print(createPost())


# # Authenticate to Twitter
# auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
# auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# # Create API object
# api = tweepy.API(auth)

# # Create a tweet
# api.update_status("Hello Tweepy")
