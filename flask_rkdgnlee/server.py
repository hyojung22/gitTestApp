from flask import Flask

import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore
cred = credentials.Certificate("flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

data = {"name": "Los Angeles", "state": "CA", "country": "USA"}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection("cities").document("LA").set(data)

users_ref = db.collection("LA")
docs = users_ref.stream()

app = Flask(__name__)

@app.route('/')
def index():
    return docs.name


    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5021)