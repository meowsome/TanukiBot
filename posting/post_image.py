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
    if not ".mp4" in image_path:
        # Upload image
        api.update_status_with_media(filename=image_path, status=None)
    else:
        # Upload video
        response_media_upload = api.media_upload(
            filename = image_path,
            chunked = True,
            media_category = "tweet_video"
        )

        api.update_status(
            status = None,
            media_ids = [response_media_upload.media_id]
        )

    print("Removing image")
    os.remove(image_path)