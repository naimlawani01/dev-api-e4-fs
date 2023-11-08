import firebase_admin
from firebase_admin import credentials
import pyrebase 
from configs.firebase_config_example import firebaseConfig

from dotenv import dotenv_values

config = dotenv_values(".env")

if not firebase_admin._apps:
    cred = credentials.Certificate("configs/carpooling-cd0af-firebase-adminsdk-b6sgm-8ed1aa6f19.json")
    firebase_admin.initialize_app(cred)

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
authSession = firebase.auth()