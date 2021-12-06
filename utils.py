import boto3
from datetime import datetime, timezone
import time
from credentials import *

client = boto3.client('iam')


def get_user_age_seconds(username):
    response = client.get_user(UserName=username, )
    user_create_date = response['User']['CreateDate']
    if username != admin:
        print("User ' {} ' is active (sec):".format(username),
              (datetime.now(timezone.utc) - user_create_date).total_seconds())
    else:
        pass

    user_seconds = (datetime.now(timezone.utc) - user_create_date).total_seconds()
    if user_seconds > max_user_age_seconds and username != admin:
        expired_sub = True
        print("User  ' {} ' is ".format(username))

    else:
        expired_sub = False
    return expired_sub


def most_frequent_char(my_str):
    """
    returns the most frequent character in a string. If there are more than 1 frequent chars, return one of them
    'abcdddddukkk'  ->  'd' repeats 5 times
    'One day you said to me'  ->  ' ' repeats 5 times
    'aabb' -> 'a' or 'b' are both valid returned values
    """
    pass


if __name__ == '__main__':
    get_user_age_seconds("YoutubeDownloader")
