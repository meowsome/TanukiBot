import boto3
import os
from dotenv import load_dotenv
import random

load_dotenv()

def get_image():
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SERVER_SECRET_KEY"),
    )

    s3 = session.client('s3')
    bucket = os.getenv("AWS_BUCKET_NAME")
    directory = "tmp/pending_post"

    objects = s3.list_objects_v2(
        Bucket=bucket
    )
    files = [res['Key'] for res in objects['Contents']]

    file_to_download = random.choice(files)

    s3.download_file(bucket, file_to_download, f'{directory}/{file_to_download}')

    return f"{directory}/{file_to_download}"