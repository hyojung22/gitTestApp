import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# 가상의 기사 데이터 (실제 데이터를 사용해야 함)
from joblib import load

lda_model = load('merged_file\lda.joblib')

articles = pd.read_csv("merged_file\pretrain_news_train2.csv")
loaded_model = load('merged_file\model.joblib')


print(articles['content'])
max_content_length = 1000
articles['content'] = articles['content'].apply(lambda x: x[:max_content_length])

print(articles)




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
recommendations = get_top_articles(lda_model, tfidf_vectorizer, articles, num_recommendations)
print("추천 기사:")
for idx, article in enumerate(recommendations, start=1):
    print(f"{idx}. {article}")

    predictions = loaded_model.predict([article])
    print(predictions)
