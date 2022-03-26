import boto3
import os
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

def upload_file(file_path, directory_to_upload, s3, bucket):
    with open(f"{directory_to_upload}/{file_path}", "rb") as f:
        s3.upload_fileobj(f, bucket, file_path)

def upload():
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SERVER_SECRET_KEY")
    )
    s3 = session.client('s3')
    bucket = os.getenv("AWS_BUCKET_NAME")

    directory_to_upload = "tmp"

    for file in tqdm(os.listdir(directory_to_upload)):
        file_path = f"{directory_to_upload}/{file}"
        if not os.path.isdir(file_path):
            upload_file(file, directory_to_upload, s3, bucket)