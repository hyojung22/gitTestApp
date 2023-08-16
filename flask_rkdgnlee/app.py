from flask import Flask, jsonify, render_template
from flask_cors import CORS



import json
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT
import cx_Oracle


cx_Oracle.init_oracle_client(lib_dir=r"C:\\Oracle\\instantclient_19_19")


app = Flask(__name__)


#connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
#cursor = connection.cursor()




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


def get_keyword_data():
    
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
    cursor = connection.cursor()
    try:
   
        cursor.execute("select keyword from keyword_table")
        keyword_contents = cursor.fetchall()
        keyword_data = [
            {'keyword' : keyword}
            for keyword in keyword_contents
        ]
        return keyword_data
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()






def get_news_data():
    
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT id, content, prediction FROM news")
        news_contents = cursor.fetchall()
        news_data = [
            {'id': id, 'content': content, 'prediction': prediction}
            for id, content, prediction in news_contents
        ]
        return news_data
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()

def get_positions_data():
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT title, contents, period, location, lat, lng, page_url FROM positions")
        positions_contents = cursor.fetchall()
        positions_data = [
            {'title': title, 'contents': contents, 'period': period, 'location': location, 'lat': lat, 'lng':lng, 'page_url':page_url}
            for title, contents, period, location, lat, lng, page_url in positions_contents
        ]
        return positions_data
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()







def get_books_data():
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT 제목,저자,가격,주소,설명 FROM BOOKS")
        books_contents = cursor.fetchall()
        books_data = [
            {'제목': title, '저자': author, '가격': price, '주소': address, '설명': description}
            for title, author, price, address, description in books_contents
        ]
        return books_data
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()



def get_fashion_data():
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT 브랜드,옷,가격,주소 FROM fashion")
        fashion_contents = cursor.fetchall()
        fashion_data = [
            {'브랜드': brand, '옷': cloth, '가격': price, '주소': address}
            for brand, cloth, price, address in fashion_contents
        ]
        return fashion_data
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

@app.route('/keyword_list')
def keywords_list():
    keyword_data = get_keyword_data()
    return jsonify(keyword_data)

@app.route('/positions_list')
def positions_list():
    positions_data = get_positions_data()
    return jsonify(positions_data)

@app.route('/books_list')
def books_list():
    books_data = get_books_data()
    return jsonify(books_data)

@app.route('/fashion_list')
def fashion_list():
    fashion_data = get_fashion_data()
    return jsonify(fashion_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5021)
