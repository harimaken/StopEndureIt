import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

from LocalFileAdapter import *

def upload_to_fb(screenshot):
    requests_session = requests.session()
    requests_session.mount('file://', LocalFileAdapter())

    image_url = 'file://' + screenshot

    cred = credentials.Certificate('dungeonhelperwow-firebase-adminsdk-8usyx-48bdfad707.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'dungeonhelperwow.appspot.com'
    })
    bucket = storage.bucket()

    image_data = requests_session.get(image_url).content
    blob = bucket.blob('dims.jpg')
    blob.upload_from_string(
            image_data,
            content_type='image/jpg'
        )
    print(blob.public_url)