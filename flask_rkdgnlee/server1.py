from flask import Flask, jsonify, render_template
from flask_cors import CORS

import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore


app = Flask(__name__)
CORS(app, 
    resources={r'*': {'orgins': 'http://localhost:5021'}}, 
    supports_credentials=True) # 다른 포트번호에 대한 보안 제거

cred = credentials.Certificate("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json")

firebase_admin.initialize_app(cred)
db = firestore.client()


################################################################
def get_news_data():
    news_list_ref = db.collection("article")
    docs = news_list_ref.stream()
    news_data = []
    for doc in docs:
        news_data.append(doc.to_dict())
    return news_data


def get_festival_data():
    return festival_data

def get_bestseller_data():
    return bestseller_data
################################################################

@app.route("/")
def hello_world():
    return render_template('index.html')
# Flask route 설정
@app.route('/news_list')
def news_list():
    # Firestore에서 users 컬렉션의 데이터 가져오기
    news_data = get_news_data()
    
    # JSON 응답으로 데이터 반환
    return jsonify(news_data)


@app.route('/bestseller')
def bestseller():

    return jsonify(festival_data)

@app.route('/festival')
def festival():

    return jsonify(bestseller_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5021)