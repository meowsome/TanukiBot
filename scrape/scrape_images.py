from .google_search import google_download
from .upload_to_s3 import upload
from .image_classification import classify

def scrape_images():    
    print("Start scrape Google")
    google_download()

    print("Start classification filtering")
    classify()

    print("Start upload")
    upload()

    print("Finished scrape")