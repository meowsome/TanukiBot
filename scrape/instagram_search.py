import instaloader
from datetime import datetime, timedelta
import os
import shutil

folder_name = "tmp"
searches = ["tanuki", "raccoondog", "japaneseraccoondog"]

# If post was made in last 30 days 
def is_post_new(post_time):
    thirty_day_ago = datetime.now() - timedelta(days=30)
    return (post_time - thirty_day_ago).days > 0

def scrape_instagram():
    L = instaloader.Instaloader()

    for search in searches:
        for post in instaloader.Hashtag.from_name(L.context, search).get_posts():
            if is_post_new(post.date_utc):
                L.download_post(post, target=folder_name)
            else:
                break

    downloads = os.listdir(folder_name)
    for item in downloads:
        if item.endswith(".txt") or item.endswith("json.xz"):
            os.remove(os.path.join(folder_name, item))

        if item.endswith(".mp4"):
            # Thumbnails are auto-downloaded, just move em to right folder
            thumb = item.split(".mp4")[0] + ".jpg"
            print(thumb)
            shutil.move(f"{folder_name}/{thumb}", f"{folder_name}/thumbs/{thumb}")