import os
import tweepy
from .get_random_image import get_image
from dotenv import load_dotenv
load_dotenv()

auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET")) 
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

def post_image():
    print("Downloading random image")
    image_path = get_image()

    print("Posting image")
    api.update_status_with_media(filename=image_path, status=None)

    print("Removing image")
    os.remove(image_path)