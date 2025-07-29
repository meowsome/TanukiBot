import os
import tweepy
from tools.generate_access_token_v2 import fetch_client
from atproto import Client
from dotenv import load_dotenv
load_dotenv()

def post_image_twitter(image_path):
    print("Authenticating Twitter")
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET")) 
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)

    print('Fetching Twitter Client')
    client = fetch_client()

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

def post_image_bsky(image_path):
    print("Authenticating Bluesky")
    client = Client()
    client.login(os.getenv("BSKY_USER"), os.getenv("BSKY_PASSWORD"))

    print("Posting image")
    is_video = ".mp4" in image_path

    with open(image_path, 'rb') as f:
        media_content = f.read()

        if is_video:
            feedback = client.send_video(
                video=media_content,
                text="",
                video_alt=""
            )

            print(feedback)
        else:
            client.send_image(
                image=media_content,
                text="",
                image_alt=""
            )

    print("Removing image")
    os.remove(image_path)