import pandas as pd


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer

#pipeline

########################################################################
import pickle

def remove_doublequotes(text):
    return text.replace('\"', '').replace("\'", "").replace("'", "").replace('"', '').replace("<br/>","").replace("\t","").replace("\n","")

daily_all_commu = pd.read_csv('2023_08_16_daily_all_commu.csv')

daily_all_commu = daily_all_commu.loc[:, "content"].to_list()

stopwords = ['-', 'jpg', 'ㅋ', '[ㅇㅎ]', "gif", '스압', 'ㅇㅎ', 'ㄷ', "ㅎ", ';', 'twt', 'blind', 'pann', 'gisa', '★', '☆', 'ㅠ', 'ㅜ', "manhwa", "mp4", "후방", "레전드", "주의", "JPG", 'webp', "boja"]

# 불용어가 제거된 데이터를 저장할 새로운 리스트
filtered_list = []
articles = pd.read_csv("news_list.csv")

with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\news_training\\pipeline_model.pkl","rb") as f:
    pipe_model = pickle.load(f)

for item in daily_all_commu:
    for stopword in stopwords:
        item = item.replace(stopword, '')
    filtered_list.append(item.strip())
# 총 데이터 갯수 확인
print(len(filtered_list))


def module_1():
    vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
    X = vectorizer.fit_transform(filtered_list)
    #LDA 모델 학습
    num_topics = 4 # 원하는 토픽의 수 설정
    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
    lda_model.fit(X)



#######################################################################################################

    #크롤링된 기사 로딩#모델 로드
    
    


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
    num_recommendations = 12  # 추천 기사 개수 (원하는 숫자로 조정)



# 추천 기사 뽑아내는 함수 수정
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


    unique_article_contents = set()  # set를 사용하여 중복을 자동으로 제거할 수 있는 자료구조 생성
    filtered_top_recommendations = []

    for article in top_recommendations:
        if article not in unique_article_contents:
            unique_article_contents.add(article)
            filtered_top_recommendations.append(article)

    my_list = filtered_top_recommendations

# 추천 기사 출력





# Remove quotes from each string and create a new list
    and_clean_list = [remove_doublequotes(s) for s in my_list]
    and_and_clean_list = [remove_doublequotes(s) for s in and_clean_list]




    vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
    X = vectorizer.fit_transform(filtered_list)

    num_topics = 6 # 원하는 토픽의 수 설정
    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
    lda_model.fit(X)
    # 중복제거하지 않은 토픽들 list 
    keyword_li= []
    # display 토픽 보여주기 


    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda_model.components_):

        # Topic별로 1000개의 단어들(features)중에서 높은 값 순으로 정렬 후 index를 반환해줌
        # argsort()는 default가 오름차순(1, 2, 3,..) 그래서[::,-1]로 내림차순으로 바꾸기
        topic_word_idx = topic.argsort()[::-1]
        top_idx = topic_word_idx[:15]
        
        # CountVectorizer 함수 할당시킨 객체에 get_feature_names()로 벡터화시킨 feature(단어들) 볼 수 있음.
        # 이 벡터화시킨 단어들(features)은 숫자-알파벳순으로 정렬되며, 단어들 순서는 fit_transform시키고 난 이후에도 동일! 
        # "문자열".join함수로 특정 문자열 사이에 끼고 문자열 합쳐줄 수 있음
        feature_concat = " ".join([str(feature_names[i])+""for i in top_idx[:2]])
        keyword_li.append(feature_concat)

# 중복제거한 키워드들 담을 = keyword_list
    keyword_list = []
    for lii in keyword_li: 
        uniq = list(lii.split(" "))
        senten = " ".join(q for q in list(dict.fromkeys(uniq)))
        keyword_list.append(senten)
    print(keyword_list)
    return keyword_list, and_and_clean_list



keyword_list, and_and_clean_list = module_1()


# 키워드 삽입
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
import cx_Oracle


# def keyword_insert(keyword_list):
#     connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
#     # 커서 생성
#     cursor = connection.cursor()
#     # 키워드 데이터 삽입
#     insert_query = "INSERT INTO keyword_table (id, keyword) VALUES (:1, :2)"
#     keyword_data = [(index + 1, keyword) for index, keyword in enumerate(keyword_list)]
#     cursor.executemany(insert_query, keyword_data)
#     # 커밋 및 연결 종료
#     connection.commit()
#     cursor.close()
#     connection.close()


# keyword_insert(keyword_list)

#adapter
#####################################################################################






def keyword_update(keyword_list):
    from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
    import cx_Oracle
    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
# Create a cursor
    cursor = connection.cursor()

    # Update records with id and new keyword value
    update_query = "UPDATE keyword_table SET keyword = :new_keyword WHERE id = :id"
    updated_keyword_list = [(new_keyword, id) for id, new_keyword in enumerate(keyword_list, start=1)]

    cursor.executemany(update_query, updated_keyword_list)

    # Commit and close the connection
    connection.commit()
    cursor.close()
    connection.close()

keyword_update(keyword_list)




















# from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
# import cx_Oracle

# connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
# cursor = connection.cursor()






# Create a session factory
#cx_Oracle.init_oracle_client(lib_dir=r"C:\\Oracle\\instantclient_19_19")




from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
import cx_Oracle

connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
cursor = connection.cursor()



def save_list_as_oracle(data_list):
    from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
    import cx_Oracle

    connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
    cursor = connection.cursor()
    try:
        for idx, article in enumerate(data_list):
            
            predictions = pipe_model.predict([article])
            prediction = predictions.tolist()  # Convert to a list
            insert_query = ( 
                "UPDATE news "
                "SET content = :content, prediction = :prediction "
                "WHERE id = :id"
            )
            
            
            for pred in prediction:
                cursor.execute(insert_query, id=idx, content=article, prediction=pred)
        
        connection.commit()
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()

save_list_as_oracle(and_and_clean_list)





