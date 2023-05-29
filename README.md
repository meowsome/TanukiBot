# Daily Tanuki Twitter Bot

Scrapes Twitter and Google for Tanuki images, filters images using ML, saves to Amazon S3 bucket, pulls daily from bucket to post to Twitter.

## Installation

1. `pip install -r requirements.txt`
2. `cd google-images-download`
3. `python setup.py install`
4. `cd ..`
5.`mkdir tmp tmp/bad tmp/thumbs tmp/pending_post`
6. `python server.py`
7. Complete the auth prompts to get the server running

## If running without server:

Ensure to run tools/generate_access_token_v2.py to populate token.json before running the ipynb file.

## .env file

| Key | Description |
| --- | --- |
| AWS_ACCESS_KEY_ID | From Access Keys at https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1&skipRegion=true#/security_credentials |
| AWS_SERVER_SECRET_KEY | From Access Keys at https://us-east-1.console.aws.amazon.com/iam/home?region=us-east-1&skipRegion=true#/security_credentials |
| AWS_BUCKET_NAME | Name of your AWS bucket |
| CONSUMER_KEY | From Twitter Dev Portal > Projects & Apps > Projects > Your app > Keys and Tokens > Consumer Keys |
| CONSUMER_SECRET | From Twitter Dev Portal > Projects & Apps > Projects > Your app > Keys and Tokens > Consumer Keys |
| ACCESS_TOKEN | From [tools/generate_access_token.py](tools/generate_access_token.py) |
| ACCESS_TOKEN_SECRET | From [tools/generate_access_token.py](tools/generate_access_token.py) |
| POSTING_TIME_UTC | Integer, time in UTC to run the posting job at |
| REDIRECT_URL | From Twitter Dev Portal > Projects & Apps > Projects > Your App > User authentication settings > Edit > Callback URI |
| CLIENT_ID | From Twitter Dev Portal > Projects & Apps > Projects > Your App > Keys and Tokens > OAuth 2.0 Client ID and Client Secret |
| CLIENT_SECRET | From Twitter Dev Portal > Projects & Apps > Projects > Your App > Keys and Tokens > OAuth 2.0 Client ID and Client Secret |