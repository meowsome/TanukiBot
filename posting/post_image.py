import os
import tweepy
from .get_random_image import get_image
from dotenv import load_dotenv
from tools.generate_access_token_v2 import fetch_client
load_dotenv()

# v1 auth
auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET")) 
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)

def post_image():
    # v2 auth
    print('fetch client')
    client = fetch_client()

    print("Downloading random image")
    image_path = get_image()

    print("Posting image")

    is_video = ".mp4" in image_path

    response_media_upload = api.media_upload(
        filename=image_path,
        chunked=is_video,
        media_category="tweet_video" if is_video else "tweet_image"
    )

    client.create_tweet(
        text=None,
        user_auth=False,
        media_ids=[response_media_upload.media_id]
    )

    print("Removing image")
    os.remove(image_path)