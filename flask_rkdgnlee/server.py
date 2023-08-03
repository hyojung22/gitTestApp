<<<<<<< HEAD
from flask import Flask, jsonify

import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore

=======
from flask import Flask,render_template, request
import pickle
import pandas as pd
import numpy as np 
>>>>>>> d9837c675b855fdd648239e9e878a206461af97c

model = pickle.load(open("lda_model.pkl", "rb"))
app = Flask(__name__)
keyword_list = pd.read_csv("keyword.csv", encoding="utf-8-sig")
keyword_list = keyword_list.iloc[:, -1].to_list()
keywords = ""

<<<<<<< HEAD
cred = credentials.Certificate("flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json")

firebase_admin.initialize_app(cred)
db = firestore.client()

doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})


def get_users_data():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    user_data = []
    for doc in docs:
        user_data.append(doc.to_dict())
    return user_data

def get_news_list_data():
    return news_list_data

def get_festival_data():
    return festival_data

def get_bestseller_data():
    return bestseller_data

# Flask route 설정
@app.route('/news_list')
def news_list():
    # Firestore에서 users 컬렉션의 데이터 가져오기
    users_data = get_users_data()
    
    # JSON 응답으로 데이터 반환
    return jsonify(users_data)


@app.route('/bestseller')
def bestseller():

    return jsonify(festival_data)

@app.route('/festival')
def festival():

    return jsonify(bestseller_data)
=======
@app.route("/")
def main():
    return "Hello, World!"

@app.route("/keywords")
def show_keywords():
    return render_template("keyword_html.html", keyword_list=keyword_list)
>>>>>>> d9837c675b855fdd648239e9e878a206461af97c


if __name__ == '__main__':
    app.run(port=5000, debug = True)