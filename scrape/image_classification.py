from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import numpy as np
import json
import pandas as pd
import ssl
from tqdm import tqdm
import magic
import os

possible_animals = json.load(open("scrape/possible_animals.json"))

def predict(model, image_path, search_path):
    img_path = f'{search_path}/{image_path}'
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    
    # Get all predictions
    predictions = model.predict(x)

    # Get top 3 predictions
    predictions_top = decode_predictions(predictions, top=5)[0]

    # Get only the classes of the predictions
    predicted_classes = [prediction[1] for prediction in predictions_top if prediction[2] > 0.02]

    if len(predicted_classes) == 0: 
        predicted_classes = [predictions_top[0][1]]

    # If the prediction is an animal, return true, otherwise false
    return pd.Series(predicted_classes).isin(possible_animals).any()

def classify():
    mime = magic.Magic(mime=True)
    ssl._create_default_https_context = ssl._create_unverified_context
    model = VGG16(weights='imagenet', include_top=True)
    search_path = "tmp"

    for media_path in tqdm(os.listdir(search_path)):
        if not os.path.isdir(f"{search_path}/{media_path}"):
            image_path = media_path

            mimetype = mime.from_file(f"{search_path}/{media_path}")

            # If is video, get thumbnail from separate folder
            if "video" in mimetype:
                image_path = "thumbs/" + media_path.split(".")[0] + ".jpg"

            elif "svg" in mimetype:
                os.rename(f"{search_path}/{media_path}", f"{search_path}/bad/{media_path}")
                continue

            # Predict image or thumbnail of video
            is_vaild_image = predict(model, image_path, search_path)

            # Move image or video to bad folder if not predicted correctly
            if not is_vaild_image:
                os.rename(f"{search_path}/{media_path}", f"{search_path}/bad/{media_path}")