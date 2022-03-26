import schedule
import time
from scrape.scrape_images import scrape_images
from posting.post_image import post_image

# schedule.every(3).weeks.do(scrape_images)
schedule.every().day.at("13:00").do(post_image)

while True:
    schedule.run_pending()
    time.sleep(60) # sleep for this many seconds