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


def compute_Cost():
    hash = {}

    hash['{ddorm}'] = ('${:,.2f}').format(AVG_DORM_COST)

    hash['{dmeal}'] = '${:,.2f}'.format(AVG_MEAL_PLAN_COST)

    hash['{dparking}'] = '${:,.2f}'.format(AVG_PARKING_COST)

    hash['{tdorm}'] = '${:,.2f}'.format(AVG_DORM_COST * DAYS_ELAPSED)

    hash['{tmeal}'] = '${:,.2f}'.format(AVG_MEAL_PLAN_COST * DAYS_ELAPSED)

    hash['{tparking}'] = '${:,.2f}'.format(AVG_PARKING_COST * DAYS_ELAPSED)

    hash['{ddormmeal}'] = '${:,.2f}'.format(
        AVG_DORM_COST + AVG_MEAL_PLAN_COST + AVG_PARKING_COST)

    hash['{dall}'] = '${:,.2f}'.format(
        AVG_DORM_COST + AVG_MEAL_PLAN_COST + AVG_PARKING_COST)

    hash['{tall}'] = '${:,.2f}'.format(
        (AVG_DORM_COST + AVG_MEAL_PLAN_COST + AVG_PARKING_COST) * DAYS_ELAPSED)

    hash['{douttut}'] = '${:,.2f}'.format((AVG_OUT_OF_STATE_COST))

    hash['{touttut}'] = '${:,.2f}'.format(
        (AVG_OUT_OF_STATE_COST * DAYS_ELAPSED))

    hash['{dintut}'] = '${:,.2f}'.format((AVG_IN_STATE_COST))

    hash['{tintut}'] = '${:,.2f}'.format((AVG_IN_STATE_COST * DAYS_ELAPSED))

    return hash


def load_Post():
    f = open("messages.txt", "r")
    tweets = []
    keyword_dict = compute_Cost()

    for line in f:
        for word in line.split():
            if '{' in word and '}' in word:  # Replace field with value
                line = line.replace(word, keyword_dict[word.lower()])
        tweets.append(line[:-1])  # remove new line

    return tweets


def create_status(postIndex=-1):
    tweets = load_Post()

    if postIndex == -1:  # random
        postIndex = random.randrange(0, len(tweets) - 1)

    return tweets[postIndex]


print(create_status())
