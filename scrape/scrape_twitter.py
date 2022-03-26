import tweepy
import os
from dotenv import load_dotenv
import urllib.request
from urllib.parse import urlparse
from tqdm import tqdm
import ssl

load_dotenv()
ssl._create_default_https_context = ssl._create_unverified_context

def search_and_download(query, chosen_api):
    searched_tweets_pages = [page for page in tweepy.Cursor(chosen_api, label=os.getenv("DEV_ENVIRONMENT_LABEL"), query=f"{query} has:media -has:mentions",maxResults=100).pages(5)]

    urls, thumbs = scrape_pages(searched_tweets_pages)

    download_images(urls, "tmp", False)
    download_images(thumbs, "tmp/thumbs", True)
    

def scrape_pages(searched_tweets_pages):
    urls = []
    thumbs = []
    for page in searched_tweets_pages:
        for tweet in page:
            tweet = tweet._json
            if 'extended_entities' in tweet:
                tweet = tweet['extended_entities']


            if 'extended_tweet' in tweet:
                tweet = tweet['extended_tweet']['extended_entities']
            
            medias = tweet['media']

            for media in medias:
                if media['type'] == 'photo':
                    urls.append(media['media_url_https'])
                elif media['type'] == 'video':
                    # Get highest bitrate
                    mp4 = max(media['video_info']['variants'], key=lambda x:x['bitrate'] if 'bitrate' in x else False)['url']
                    urls.append(mp4)
                    thumbs.append((media['media_url_https'], mp4.split("/")[-1].split(".")[0]))
    return (urls, thumbs)

def download_images(urls, directory, thumbs):
    for url in tqdm(urls):
        destination = url

        # If video, then rename thumbnail file to same as video file 
        if thumbs:
            destination = f"{url[1]}.jpg"
            url = url[0]

        dest_path = urlparse(destination).path.split("/")[-1]
        
        r = urllib.request.urlopen(url)
        with open(f"{directory}/{dest_path}", "wb") as f:
            f.write(r.read())

def scrape_twitter():
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET")) 
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    api = tweepy.API(auth)

    queries = ["japanese raccoon dog", "#raccoondog", "#tanuki"]
    chosen_api = api.search_30_day

    for query in queries:
        search_and_download(query, chosen_api)