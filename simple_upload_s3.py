import boto3
from youtube-crawler import search_download

s3_client = boto3.client('s3')
s3_client.upload_file('FILENAME', 'BUCKET', 'OBJECT_NAME')


def upload(username,search_str,numOf_results):
    downloaded_files = search(search_str, numOf_results)
    try:
        for a in downloaded_files[0]:
            try:
                s3_client.upload_file(a, bucket,username + "/" + a)
                print("Successfully Downloaded {} ".format(a))
            except Exception as g:
                print("Error", g)
                exit(1)

    except Exception as e:
        print("Error", e)
        exit(1)