from google_images_download import google_images_download

def google_download():
    google_images_download.googleimagesdownload().download(arguments = {"keywords":"tanuki, Japanese raccoon dog, タヌキ","limit":100, "size": ">800*600", "type": "photo", "silent_mode": True, "no_numbering": True, "usage_rights": "labeled-for-reuse-with-modifications", "usage_rights": "labeled-for-reuse", "usage_rights": "labeled-for-noncommercial-reuse-with-modification", "usage_rights": "labeled-for-nocommercial-reuse", "no_directory": True, "output_directory": "tmp"})