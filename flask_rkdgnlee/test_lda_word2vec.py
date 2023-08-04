import numpy as np
from kiwipiepy import Kiwi
from gensim.models import Word2Vec
from gensim.corpora import Dictionary
from gensim.models.ldamodel import LdaModel

def noun_extractor(text):
    kiwi = Kiwi()
    results = []
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
            results.append(token)
    return results

def train_word2vec_and_lda(corpus, num_topics, word2vec_dim):
    # Word2Vec 모델 훈련
    word2vec_model = Word2Vec(sentences=corpus, vector_size=word2vec_dim, window=5, min_count=1, workers=4)

    # Word2Vec 모델의 워드 벡터와 사전 생성
    word_vectors = word2vec_model.wv
    dictionary = Dictionary(corpus)

    # LDA 모델 훈련
    bow_corpus = [dictionary.doc2bow(doc) for doc in corpus]
    lda_model = LdaModel(bow_corpus, num_topics=num_topics)

    return word_vectors, dictionary, lda_model

def recommend_similar_articles(new_article, word_vectors, dictionary, lda_model):
    # 입력 기사 토큰화
    tokens = noun_extractor(new_article)

    # Word2Vec 임베딩
    word2vec_dim = word_vectors.vector_size
    word2vec_embedding = np.zeros((len(tokens), word2vec_dim))
    for i, token in enumerate(tokens):
        if token in word_vectors:
            word2vec_embedding[i] = word_vectors[token]

    # LDA 토픽 분포 생성
    bow = dictionary.doc2bow(tokens)
    lda_topics = np.zeros(lda_model.num_topics)
    for topic, prob in lda_model.get_document_topics(bow):
        lda_topics[topic] = prob

    # 입력 기사를 LDA 모델로 예측하여 유사한 기사들 추천
    X = np.hstack((word2vec_embedding, lda_topics))
    similar_articles = []
    for i, topic_prob in enumerate(lda_model[bow]):
        similar_topic = sorted(topic_prob, key=lambda x: x[1], reverse=True)[0][0]
        for doc, _ in lda_model.get_topic_terms(similar_topic):
            similar_articles.append(dictionary[doc])
    
    return similar_articles

if __name__ == '__main__':
    # 기사 데이터 (텍스트 리스트)
    articles = [
        "기사 내용 1",
        "기사 내용 2",
        "기사 내용 3",
        # 추가적인 기사들
    ]

    # 토큰화된 문서 집합 (corpus) 생성
    corpus = [noun_extractor(article) for article in articles]

    num_topics = 5
    word2vec_dim = 100  # Word2Vec 임베딩의 차원을 100으로 조정

    # Word2Vec과 LDA 모델 훈련
    word_vectors, dictionary, lda_model = train_word2vec_and_lda(corpus, num_topics, word2vec_dim)

    # 새로운 기사를 입력받아 유사한 기사 추천
    new_article = "새로운 기사 내용입니다. 기사를 분류해주세요."
    recommended_articles = recommend_similar_articles(new_article, word_vectors, dictionary, lda_model)

    # 추천된 유사한 기사 출력
    print(recommended_articles)