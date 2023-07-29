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


#df_news 주석처리
#df_news = pd.read_csv("news.csv")



kiwi = Kiwi()


kiwi.prepare()


#morph_analysis = lambda x: kiwi.tokenize(x) if type(x) is str else None
#df['형태소분석결과'] = df['원문'].apply(morph_analysis)


#나오는지 확인
print(df_news['content'].str[:30])


#countVec_object
countVec1 = CountVectorizer()

#countVec_fit

countVec1.fit(df_news['content'])

print(countVec1.vocabulary_)
###create_training_data
### news.csv를 news_train과 news_test로 분리하고 가공하여 재작업



#logistic_regression모델
logi_model = LogisticRegression()
logi_result = cross_val_score(logi_model, X_train, y_train, cv=3)
print(logi_result)
print(logi_result.mean())
svm_model = LinearSVC()
svm_result = cross_val_score(svm_model, X_train, y_train, cv=3)
print(svm_result)
print(svm_result.mean())

#pipeline 생성(매개변수 정해야됨)
make_pipeline( CountVectorizer(), LogisticRegression())

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
#grid = GridSearchCV(, params, cv=3)
grid.fit(X_train, y_train)

