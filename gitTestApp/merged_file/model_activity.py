# -*- coding: utf-8 -*-

import pandas as pd

from joblib import load
from sklearn.feature_extraction.text import CountVectorizer
from tqdm import tqdm
from sklearn.decomposition import LatentDirichletAllocation


model = load('model.joblib')
lda_model = load('lda.joblib')

vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
daily_all_commu = pd.read_csv("230801_daily_commu.csv", encoding= 'utf-8-sig')
daily_all_commu = daily_all_commu.loc[:, "content"].to_list()

stopwords = ['-', 'manhwa', 'jpg', 'ㅋ', '[ㅇㅎ]', "gif", '스압', 'ㅇㅎ', 'ㄷ', "ㅎ", ';', 'twt', 'blind', 'pann', 'gisa', '★', '☆', 'ㅠ', 'ㅜ', "manhwa", "mp4", "후방", "레전드", "주의", "JPG", 'webp', "boja"]

filtered_list = []

for item in daily_all_commu:
    for stopword in stopwords:
        item = item.replace(stopword, '')
    filtered_list.append(item.strip())

#print(predict([""]))
X = vectorizer.fit_transform(filtered_list)
#LDA 모델 학습
num_topics = 4 # 원하는 토픽의 수 설정
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
lda_model.fit(X)

def display_topic_words(lda_model, feature_names, num_top_words):
    for topic_idx, topic in enumerate(lda_model.components_):
        print("\nTopic #", topic_idx+1)
        # Topic별로 1000개의 단어들(features)중에서 높은 값 순으로 정렬 후 index를 반환해줌
        # argsort()는 default가 오름차순(1, 2, 3,..) 그래서[::,-1]로 내림차순으로 바꾸기
        topic_word_idx = topic.argsort()[::-1]
        top_idx = topic_word_idx[:num_top_words]
        
        # CountVectorizer 함수 할당시킨 객체에 get_feature_names()로 벡터화시킨 feature(단어들) 볼 수 있음.
        # 이 벡터화시킨 단어들(features)은 숫자-알파벳순으로 정렬되며, 단어들 순서는 fit_transform시키고 난 이후에도 동일! 
        # "문자열".join함수로 특정 문자열 사이에 끼고 문자열 합쳐줄 수 있음
        feature_concat = " ".join([str(feature_names[i])+" "for i in top_idx[:4]])
        
        print(feature_concat)
feature_names = vectorizer.get_feature_names_out()
display_topic_words(lda_model, feature_names, 15)



