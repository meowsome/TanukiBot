# https://gist.github.com/hezhao/4772180?permalink_comment_id=3972371#gistcomment-3972371

import tweepy
import os
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"), "oob") 

auth_url = auth.get_authorization_url()
# Visit URL when logged into the bot account
print('Authorization URL: ' + auth_url)

# Pin is oauth_verifier
verifier = input('PIN: ').strip()

# Save these in .env file
auth.get_access_token(verifier)
print('ACCESS_KEY = "%s"' % auth.access_token)
print('ACCESS_SECRET = "%s"' % auth.access_token_secret)

# Verify it works
auth.set_access_token(auth.access_token, auth.access_token_secret)
api = tweepy.API(auth)
user = api.verify_credentials()
print('Name: ' + str(user.name))