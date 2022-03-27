from apscheduler.schedulers.blocking import BlockingScheduler
from scrape.scrape_images import scrape_images
from posting.post_image import post_image
import os
from dotenv import load_dotenv

load_dotenv()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='*', hour=os.getenv("POSTING_TIME_UTC"))
def post_image_schedule():
    post_image()

@sched.scheduled_job('cron', day=1)
def scrape_images_schedule():
    scrape_images()

try:
    sched.start()
except KeyboardInterrupt:
    print("Scheduler interrupted")