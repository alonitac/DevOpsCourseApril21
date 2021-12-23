import boto3

UserName = "YoutubeDownloader"

def create_user(username):
    iam = boto3.client("iam")
    response = iam.create_user(UserName=username)
    print(response)


s3_client = boto3.client('s3')
s3_client.upload_file('FILENAME', 'BUCKET', 'OBJECT_NAME')
iam_client = boto3.client('iam')
iam_client.create_user(iam_client)


