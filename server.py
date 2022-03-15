import tweepy
import schedule
import time
import os
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET")) 
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

user = api.verify_credentials()

def post_image():
    image = find_image()
    print(image)

def find_image():
    return "test"

schedule.every().second.do(post_image)

while True:
    schedule.run_pending()
    time.sleep(1)