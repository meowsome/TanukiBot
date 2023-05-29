# https://docs.tweepy.org/en/stable/authentication.html

import tweepy
import os
from dotenv import load_dotenv
import json
from datetime import datetime
load_dotenv()

# Extend tweepy to allow refresh_token
class MyOAuth2UserHandler(tweepy.OAuth2UserHandler):
    # Kudos https://github.com/tweepy/tweepy/pull/1806

    def refresh_token(self, refresh_token): 
        new_token = super().refresh_token(
                "https://api.twitter.com/2/oauth2/token",
                refresh_token=refresh_token,
                body=f"grant_type=refresh_token&client_id={self.client_id}",
            )
        return new_token

def fetch_new_creds():
    oauth2_user_handler = tweepy.OAuth2UserHandler(
        client_id=os.getenv("CLIENT_ID"),
        redirect_uri=os.getenv("REDIRECT_URL"),
        scope=["tweet.read", "tweet.write", "users.read", "offline.access"],
        client_secret=os.getenv("CLIENT_SECRET")
    )

    print(oauth2_user_handler.get_authorization_url())

    authorization_response = input("Enter entire URL after clicking link: ")

    access_token = oauth2_user_handler.fetch_token(
        authorization_response
    )

    print(access_token)

    with open("token.json", "w+") as file:
        json.dump(access_token, file)

def fetch_client():
    with open('token.json') as file:
        access_token = json.load(file)

    # If the access token has expired, use refresh token to fetch a new one
    token_expire_date = datetime.utcfromtimestamp(access_token['expires_at'])
    datetime_now = datetime.utcnow()
    if token_expire_date < datetime_now:
        print('fetching new token')
        oauth2_user_handler = MyOAuth2UserHandler(
            client_id=os.getenv("CLIENT_ID"),
            redirect_uri=os.getenv("REDIRECT_URL"),
            scope=["tweet.read", "tweet.write", "users.read", "offline.access"],
            client_secret=os.getenv("CLIENT_SECRET")
        )
        access_token = oauth2_user_handler.refresh_token(refresh_token=access_token['refresh_token'])

        with open("token.json", "w+") as file:
            json.dump(access_token, file)

    # Get client using access token
    return tweepy.Client(access_token['access_token'])


if __name__ == "__main__":
    fetch_new_creds()