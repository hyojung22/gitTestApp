import pandas as pd
import numpy as np


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer

#pipeline

########################################################################
import pickle



# #파이어베이스 접속
#import firebase_admin
#from firebase_admin import credentials, firestore

#credentials
#cred = credentials.Certificate('C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json')
#firebase_admin.initialize_app(cred)

# Firestore DB 연결
#db = firestore.client()




daily_all_commu = pd.read_csv('C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\community_content\\230803_daily_commu.csv')


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
articles = pd.read_csv("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\lambda_folder\\crawling_news\\news_list.csv")

# 저장된 모델 불러오기
# with open('C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\lambda_folder\\crawling_news\\svm_model.pkl', 'rb') as f:
#     svm_model = pickle.load(f)

# with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\news_training\\rf_model.pkl", 'rb') as f:
#     rf_model = pickle.load(f)


with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\news_training\\pipeline_model.pkl","rb") as f:
    pipe_model = pickle.load(f)

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
# data_list = ["ㅁㅁㄴㅇㄻㄴㅇㄻㄴㅇ리ㅏㅓ"]

# # 각 요소를 UTF-8로 인코딩
# encoded_list = [item.encode('euc-kr') for item in data_list]


# print(encoded_list)



# doc_ref = db.collection("article").document('doc_8')  # 문서 ID를 자동 생성하려면 None 대신 None을 사용
# doc_ref.set({"article": encoded_list, "prediction": 1})

# file_path = "C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\news_training\\뉴스학습_원시데이터_14000개.xlsx"
# df = pd.read_excel(file_path)





# naver_movie_pipe= make_pipeline( CountVectorizer(), LogisticRegression())
# X_train = df['본문']
# X_test = df['본문']
# y_train = df['label']
# y_test = df['label']

# 예측 결과 확인

# model = Word2Vec(sentences=df['content'], vector_size=100, window=5, min_count=1, workers=4)

# Step 3: Convert text data into word embeddings
# embeddings = [model.wv[word] for word in filtered_list[0]]  # Example for the first sentence

# my_dict = {"content":"(서울=연합뉴스) 정아란 한지훈 기자 = 윤석열 대통령은 7일 태풍 카눈이 한반도 방향으로 북상함에 따라 2023 새만금 세계스카우트잼버리 참가자들의 안전 확보를 위한 컨틴전시 플랜(긴급 비상 계획) 점검에 들어갔다."}
# embeddings = [model.wv[my_dict]]




# # 딕셔너리를 Firestore에 저장
# def save_list_as_documents(collection_name, data_list):
# #     # utf8_encoded_list = utf8_encode(data_list)
#     for idx, article in enumerate(data_list):

          

# # Word2Vec 모델 학습
        
#         predictions = pipe_model.predict([article])
#         predictions = predictions.tolist()
        
#         doc_ref = db.collection(collection_name).document(f'doc_{idx}')  # 문서 ID를 자동 생성하려면 None 대신 None을 사용
#         doc_ref.set({"content": article, "prediction": predictions})

# # Firestore에 "article" 컬렉션에 딕셔너리 데이터 저장
# save_list_as_documents("article", my_list)


from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
import cx_Oracle

connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
cursor = connection.cursor()
# Create an engine
#engine = create_engine(f'oracle+cx_oracle://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/xe')

# Create a session factory
#cx_Oracle.init_oracle_client(lib_dir=r"C:\\Oracle\\instantclient_19_19")




def save_list_as_oracle(data_list):
    try:
        for idx, article in enumerate(data_list):
            predictions = pipe_model.predict([article])
            predictions_str = predictions.tolist()  # Convert to a list
            update_query = (
                f"UPDATE news "
                f"SET content = :content, prediction = :prediction "
                f"WHERE id = :id"
            )
            
            cursor.execute(update_query, id=idx, content=article, prediction=predictions_str[idx])
        
        connection.commit()
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()

save_list_as_oracle(my_list)





