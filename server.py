from apscheduler.schedulers.blocking import BlockingScheduler
from posting.post_image import post_image_twitter, post_image_bsky
from posting.get_random_image import get_image
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

def create_directory():
    directory = "tmp"
    Path(directory).mkdir(parents=True, exist_ok=True)
    Path(f"{directory}/bad").mkdir(parents=True, exist_ok=True)
    Path(f"{directory}/thumbs").mkdir(parents=True, exist_ok=True)
    Path(f"{directory}/pending_post").mkdir(parents=True, exist_ok=True)

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=os.getenv("POSTING_TIME_UTC"))
def post_image_schedule():
    create_directory()

    print("Downloading random image")
    image = get_image()
    # post_image_twitter(image)
    post_image_bsky(image)

try:
    print("Starting scheduler")
    sched.start()
except KeyboardInterrupt:
    print("Scheduler interrupted")