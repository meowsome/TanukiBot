# Daily Tanuki Twitter Bot

Scrapes Twitter and Google for Tanuki images, filters images using ML, saves to Amazon S3 bucket, pulls daily from bucket to post to Twitter.

## Installation

1. `pip install -r requirements.txt`
2. `cd google-images-download`
3. `python setup.py install`
4. `cd ..`
5. `python server.py`
6. `mkdir tmp tmp/bad tmp/thumbs tmp/pending_post`

## .env file

| Key | Description |
| --- | --- |
| AWS_ACCESS_KEY_ID | From Access Keys at https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1&skipRegion=true#/security_credentials |
| AWS_SERVER_SECRET_KEY | From Access Keys at https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1&skipRegion=true#/security_credentials |
| AWS_BUCKET_NAME | Name of your AWS bucket |
| CONSUMER_KEY | From Twitter Dev Portal > Projects & Apps > Standalone Apps > Your app > Keys and Tokens > Consumer Keys |
| CONSUMER_SECRET | From Twitter Dev Portal > Projects & Apps > Standalone Apps > Your app > Keys and Tokens > Consumer Keys |
| ACCESS_TOKEN | From [tools/generate_access_token.py](tools/generate_access_token.py) |
| ACCESS_TOKEN_SECRET | From [tools/generate_access_token.py](tools/generate_access_token.py) |
| DEV_ENVIRONMENT_LABEL | From Twitter Dev Portal > Products > Premium > Dev Environments > Choose one |
| POSTING_TIME_UTC | Integer, time in UTC to run the posting job at |