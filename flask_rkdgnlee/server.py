
from flask import Flask,render_template, request
import pickle
import pandas as pd
import numpy as np 


model = pickle.load(open("lda_model.pkl", "rb"))
app = Flask(__name__)
keyword_list = pd.read_csv("keyword.csv", encoding="utf-8-sig")
keyword_list = keyword_list.iloc[:, -1].to_list()
keywords = ""


@app.route("/")
def main():
    return "Hello, World!"

@app.route("/keywords")
def show_keywords():
    return render_template("keyword_html.html", keyword_list=keyword_list)



if __name__ == '__main__':
    app.run(port=5000, debug = True)