from flask import Flask, jsonify, render_template
from flask_cors import CORS

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT
import cx_Oracle


cx_Oracle.init_oracle_client(lib_dir=r"C:\\Oracle\\instantclient_19_19")


app = Flask(__name__)


connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
cursor = connection.cursor()




## import firebase_admin
## from firebase_admin import credentials, db
## from firebase_admin import firestore

# sqlalchemy






CORS(app, resources={r'*': {'orgins': 'http://localhost:5021'}}, supports_credentials=True) 



# 다른 포트번호에 대한 보안 제거



# cred = credentials.Certificate("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json")

# firebase_admin.initialize_app(cred)
# db = firestore.client()


################################################################
# def get_news_data():
#     news_list_ref = db.collection("article")
#     docs = news_list_ref.stream()
#     news_data = []
#     for doc in docs:
#         news_data.append(doc.to_dict())
#     return news_data
def get_news_data():
    try:
        cursor.execute("SELECT id, content FROM news")
        news_contents = cursor.fetchall()
        news_data = [
            {'id': id, 'content': content}
            for id, content in news_contents
        ]
        return news_data
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/news_list')
def news_list():
    news_data = get_news_data()
    return jsonify(news_data)






# def get_festival_data():
#     return festival_data

# def get_bestseller_data():
#     return bestseller_data
################################################################






# @app.route('/bestseller')
# def bestseller():

#     return jsonify(festival_data)

# @app.route('/festival')
# def festival():

#     return jsonify(bestseller_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5021)