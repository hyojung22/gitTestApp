

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)


client = MongoClient('mongodb://localhost:27017')
db = client.my_database

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_data():
    if request.method == 'POST':
        data = request.get_json()
        name = data['name']
        age = data['age']

        # MongoDB에 데이터 추가
        try:
            collection = db['users']
            user_data = {"name": name, "age": age}
            collection.insert_one(user_data)
            return jsonify({"message": "Data added successfully!"}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/users')
def get_users():
   
    try:
        collection = db['document1']
        users = list(collection.find())
        return jsonify(users), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)





