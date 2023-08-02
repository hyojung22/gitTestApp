import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore
cred = credentials.Certificate("flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json")

firebase_admin.initialize_app(cred)
db = firestore.client()


# Add a new doc in collection 'cities' with ID 'LA'

doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

#https://firebase.google.com/docs/firestore/quickstart?hl=ko
#word2vec autoML