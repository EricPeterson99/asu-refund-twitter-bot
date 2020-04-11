# import tweepy
import datetime
import random

CURRENT_DATE = datetime.datetime.now()
END_DATE_OF_SEMESTER = datetime.datetime(2020, 5, 9)
START_DATE_OF_CORONA = datetime.datetime(2020, 3, 15)
DAYS_ELAPSED = (CURRENT_DATE - START_DATE_OF_CORONA).days

DAYS_IN_SEMESTER = 117
AVG_IN_STATE_COST = 5355 / DAYS_IN_SEMESTER
AVG_OUT_OF_STATE_COST = 14400 / DAYS_IN_SEMESTER
AVG_TUITION_COST = (9789.5 + 75) / DAYS_IN_SEMESTER
AVG_DORM_COST = 4492 / DAYS_IN_SEMESTER
AVG_MEAL_PLAN_COST = 3358 / DAYS_IN_SEMESTER
AVG_PARKING_COST = 495 / DAYS_IN_SEMESTER


def compute_Cost(type):
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

    elif(type.lower() == 'douttut'):
        return '${:,.2f}'.format((AVG_OUT_OF_STATE_COST))

    elif(type.lower() == 'touttut'):
        return '${:,.2f}'.format((AVG_OUT_OF_STATE_COST * DAYS_ELAPSED))

    elif(type.lower() == 'dintut'):
        return '${:,.2f}'.format((AVG_IN_STATE_COST))

    elif(type.lower() == 'tintut'):
        return '${:,.2f}'.format((AVG_IN_STATE_COST * DAYS_ELAPSED))

    return


def load_Post():
    f = open("messages.txt", "r")
    tweets = []

    for line in f:
        for word in line.split():
            if '{' in word and '}' in word:  # Replace field with value
                line = line.replace(word, computeCost(word[1:-1]))
        tweets.append(line[:-1])  # remove new line

    return tweets


def create_status(postIndex=-1):
    tweets = load_Post()

    if postIndex == -1:  # random
        postIndex = random.randrange(0, len(tweets) - 1)

    return tweets[postIndex]
