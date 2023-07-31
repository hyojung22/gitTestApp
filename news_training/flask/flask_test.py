

from flask import Flask, jsonify
import pandas as pd
import json
# model = pickle.load(open('iri.pkl', 'rb'))



news = pd.read_csv('C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\Personal_Working\\news_training\\dummy.csv')

list_news = news['content'].values.tolist()
json_data = json.dumps(list_news, ensure_ascii=False).encode('utf-8')
app = Flask(__name__)



@app.route('/')
def main():
    return  json_data


if __name__ == "__main__":
    app.run(debug=True)