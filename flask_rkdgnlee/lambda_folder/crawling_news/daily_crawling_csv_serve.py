import pandas as pd
import numpy as np
from kiwipiepy import Kiwi


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
########################################################################
from joblib import dump, load
#파이어베이스 접속
import firebase_admin
from firebase_admin import credentials, firestore

#credentials
cred = credentials.Certificate('flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json')
firebase_admin.initialize_app(cred)

# Firestore DB 연결
db = firestore.client()




daily_all_commu = pd.read_csv('flask_rkdgnlee\\community_content\\230803_daily_commu.csv')


daily_all_commu = daily_all_commu.loc[:, "content"].to_list()

stopwords = ['-', 'jpg', 'ㅋ', '[ㅇㅎ]', "gif", '스압', 'ㅇㅎ', 'ㄷ', "ㅎ", ';', 'twt', 'blind', 'pann', 'gisa', '★', '☆', 'ㅠ', 'ㅜ', "manhwa", "mp4", "후방", "레전드", "주의", "JPG", 'webp', "boja"]

# 불용어가 제거된 데이터를 저장할 새로운 리스트
filtered_list = []

for item in daily_all_commu:
    for stopword in stopwords:
        item = item.replace(stopword, '')
    filtered_list.append(item.strip())
# 총 데이터 갯수 확인
print(len(filtered_list))


vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
X = vectorizer.fit_transform(filtered_list)
#LDA 모델 학습
num_topics = 4 # 원하는 토픽의 수 설정
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
lda_model.fit(X)



#######################################################################################################

#모델 로드
articles = pd.read_csv("merged_file\pretrain_news_train2.csv")
loaded_model = load('merged_file\model.joblib')


print(articles['content'])
max_content_length = 1000
articles['content'] = articles['content'].apply(lambda x: x[:max_content_length])

print(articles)


#######################################################################################################

# TF-IDF 벡터화
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, max_features=1000, min_df=1, stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(articles['content'])

# LDA 모델 훈련
lda_model.fit(tfidf_matrix)

# 수정된 get_top_articles 함수
article_topic_probabilities = lda_model.transform(tfidf_matrix)



# 추천 기사 뽑아내는 함수 수정
def get_top_articles(lda_model, tfidf_vectorizer, articles, num_recommendations=5):
    article_contents = articles['content']
    tfidf_matrix = tfidf_vectorizer.transform(article_contents)
    article_topic_probabilities = lda_model.transform(tfidf_matrix)

    topic_article_mapping = {}
    num_topics = lda_model.n_components

    for topic_idx in range(num_topics):
        topic_article_mapping[topic_idx] = []

    for article_idx, topic_probabilities in enumerate(article_topic_probabilities):
        topic_idx = topic_probabilities.argmax()
        topic_article_mapping[topic_idx].append((article_contents[article_idx], topic_probabilities[topic_idx]))

    top_recommendations = []
    for topic_idx in range(num_topics):
        sorted_articles = sorted(topic_article_mapping[topic_idx], key=lambda x: x[1], reverse=True)
        top_recommendations.extend([article[0] for article in sorted_articles[:num_recommendations]])

    return top_recommendations

# 추천 기사 출력
num_recommendations = 3  # 추천 기사 개수 (원하는 숫자로 조정)
my_list = get_top_articles(lda_model, tfidf_vectorizer, articles, num_recommendations)




#adapter
#####################################################################################
def utf8_encode(data):
    if isinstance(data, str):
        return data.encode('utf-8')
    elif isinstance(data, list):
        return [utf8_encode(item) for item in data]
    elif isinstance(data, dict):
        return {key: utf8_encode(value) for key, value in data.items()}
    else:
        return data
# 딕셔너리를 Firestore에 저장
def save_list_as_documents(collection_name, data_list):
    utf8_encoded_list = utf8_encode(data_list)
    for idx, article in enumerate(utf8_encoded_list):
        predictions = loaded_model.predict([article])
        predictions.tolist()
        doc_ref = db.collection(collection_name).document(f'doc_{idx}')  # 문서 ID를 자동 생성하려면 None 대신 None을 사용
        doc_ref.set({"article": article, "prediction": predictions})


# Firestore에 "article" 컬렉션에 딕셔너리 데이터 저장
save_list_as_documents("article", my_list)

