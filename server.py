from apscheduler.schedulers.blocking import BlockingScheduler
from scrape.scrape_images import scrape_images
from posting.post_image import post_image
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

directory = "tmp"
Path(directory).mkdir(parents=True, exist_ok=True)
Path(f"{directory}/bad").mkdir(parents=True, exist_ok=True)
Path(f"{directory}/thumbs").mkdir(parents=True, exist_ok=True)
Path(f"{directory}/pending_post").mkdir(parents=True, exist_ok=True)

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=os.getenv("POSTING_TIME_UTC"))
def post_image_schedule():
    post_image()

@sched.scheduled_job('cron', day=1)
def scrape_images_schedule():
    scrape_images()

try:
    sched.start()
except KeyboardInterrupt:
    print("Scheduler interrupted")