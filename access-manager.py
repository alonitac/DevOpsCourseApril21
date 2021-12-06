import boto3
from botocore.exceptions import ClientError
import time
from credentials import *
from datetime import datetime, timezone

client = boto3.client('iam')


def create_user(username):
    while True:
        try:
            response = client.create_user(UserName=username, PermissionsBoundary=permission,
                                          Tags=[{'Key': 'YoutubeAppSubscriber', 'Value': username}, ])
            time.sleep(1.2)
            print("Successfully Created User '{}'".format(username))
            break

        except ClientError as e:
            if e.response['Error']['Code'] == 'EntityAlreadyExists':
                print("User Name already exists, Please enter a different name")
                username = input("Enter Username: ")
                continue
            else:
                print("Unexpected error: %s" % e)
                username = input("Enter Username: ")
                continue


def delete_outdated_usernames(max_user_age_seconds):
    """
    Deletes users older than max_user_age_seconds
    """
    # TODO List all users
    # TODO Iterate over the users in "for" loop
    # TODO Inside the loop, use "get_user_age_seconds" from utils.py to check if the user is older than max_user_age_seconds
    # TODO Delete the user if his age is greater than max_user_age_seconds
    pass


if __name__ == '__main__':
    iam_client = boto3.client('iam')
    create_user(" ")

    # create_user('john')
    # delete_outdated_usernames(60)
