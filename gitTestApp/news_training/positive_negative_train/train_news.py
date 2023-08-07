from sklearn.feature_extraction.text import CountVectorizer
from kiwipiepy import Kiwi
import pandas as pd


#LogisticRegression모델 임포트
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC # support vector machine
from sklearn.model_selection import cross_val_score


#pipeline import
from sklearn.pipeline import make_pipeline

#GridSearchCV import
from  sklearn.model_selection import GridSearchCV

#model saver
import pickle
from joblib import dump, load



kiwi = Kiwi()


kiwi.prepare()


text_test = pd.read_csv("news_training\\positive_negative_train\\news_test.csv")
text_train = pd.read_csv("news_training\\positive_negative_train\\news_train.csv")


#morph_analysis = lambda x: kiwi.tokenize(x) if type(x) is str else None
#df['형태소분석결과'] = df['원문'].apply(morph_analysis)

#def myTokenizer(text):
#	kiwi.tokenizer	
#	return kiwi.tokenize(text)


#countVec_object
#countVec1 = CountVectorizer(tokenizer=myTokenizer)

#countVec_fit

#countVec1.fit(df_news['content'])

#print(countVec1.vocabulary_)
###create_training_data
### news.csv를 news_train과 news_test로 분리하고 가공하여 재작업
### tokenizer가 어디에 들어가는지 살펴봐야함
### 인덱스 추가


#pipeline 생성(매개변수 정해야됨)
news_pipe = make_pipeline( CountVectorizer(), LogisticRegression())

#GridSearchCV


#df_news_train 데이터에 맞는 df이름으로 고칠것
X_train = text_train['content']
X_test = text_test['content']
y_train = text_train['label']
y_test = text_test['label']


params = {
    'countvectorizer__max_df' : [10000, 13000, 15000],
    'countvectorizer__min_df' : [3,5,7],
    'countvectorizer__ngram_range' : [(1,1),(1,2),(1,3)],
    'logisticregression__C' : [0.0001, 0.001, 0.01, 1]
}

#여기에 파이프라인 매개변수 넣으세요
grid = GridSearchCV(news_pipe, params, cv=3)
grid.fit(X_train, y_train)
best_model = grid.best_estimator_
best_model.score(X_test, y_test)
#best_model.predict(['',''])

dump(best_model, 'model.joblib')
voca = best_model[0].vocabulary_

df = pd.DataFrame([
   voca.keys(),
   voca.values()
])
df2 = df.T.sort_values(by=1)

#df2.sort_values(by = 'coef', inplace=True)

print(df2)