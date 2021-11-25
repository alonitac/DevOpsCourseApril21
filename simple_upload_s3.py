import boto3

UserName = "YoutubeDownloader"

def createUser(username):
    iam = boto3.client("iam")
    response = iam.createUser(UserName = username)
    print(response)


s3_client = boto3.client('s3')
s3_client.upload_file('FILENAME', 'BUCKET', 'OBJECT_NAME')
iam_client = boto3.client('iam')
iam_client.createUser(iam_client)


