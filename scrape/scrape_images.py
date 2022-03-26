from .google_search import google_download
from .scrape_twitter import scrape_twitter
from .upload_to_s3 import upload
from .image_classification import classify

def scrape_images():
    print("Start scrape Twitter")
    scrape_twitter()  
    
    print("Start scrape Google")
    google_download()

    print("Start classification filtering")
    classify()

    print("Start upload")
    upload()

    print("Finished scrape")