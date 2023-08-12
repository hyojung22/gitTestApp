# selenium, BeautifulSoup, pandas, lxml, sklearn 설치 필요 
# pip install "selenium" 설치 가능 
import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from kiwipiepy import Kiwi
import time


#blockingScheduler -> background로!
from apscheduler.schedulers.background import BlockingScheduler



#파이어베이스 접속
# import firebase_admin
# from firebase_admin import credentials, firestore

#collect_news.py
from collect_news import crawling


#credentials
# cred = credentials.Certificate('C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json')
# firebase_admin.initialize_app(cred)

# # Firestore DB 연결
# db = firestore.client()

########################################################################

import pickle
with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\news_training\\pipeline_model.pkl","rb") as f:
    pipe_model = pickle.load(f)
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
import cx_Oracle

# 데이터 수집 시작 
dc_list = []
bbomppu_list = []
fm_list = []
tq_list = []
eto_list = []
keyword_li= []
# 옵션 생성
def remove_doublequotes(text):
    return text.replace('\"', '').replace("\'", "").replace("'", "").replace('"', '').replace("<br/>","").replace("\t","").replace("\n","")




def job1():
    options = wb.ChromeOptions()
# 창 숨기는 옵션 추가
    
    options.add_argument("headless")
# driver 실행
    driver = wb.Chrome(options=options)


# dc 수집
    driver.get("https://gall.dcinside.com/board/lists/?id=dcbest")
# 100개씩 보기 
    driver.find_element(By.CSS_SELECTOR, "#container > section.left_content > article:nth-child(3) > div.list_array_option.clear > div.right_box > div > div.select_box.array_num > div > a").click()
    driver.find_element(By.CSS_SELECTOR, "#listSizeLayer > li:nth-child(3) > a").click()
    soup = bs(driver.page_source, "lxml")


    for j in range(2, 5):
        for i in range(3, 102):
            title = soup.select(f"article:nth-child(3) > div.gall_listwrap.list > table > tbody > tr:nth-child({i}) > td.gall_tit.ub-word > a:nth-child(1)")
            dc_list.append((title[0].text)[5:])

# bbomppu 수집
    driver.get("https://www.ppomppu.co.kr/hot.php?category=2")
# 그냥 바로 추출 
    soup = bs(driver.page_source, "lxml")
# 첫 1-10 까지 
    for j in range(2, 9):
        for i in range(6, 26):
            title = soup.select(f"table.board_table > tbody > tr:nth-child({i}) > td:nth-child(4) > a")
            bbomppu_list.append(title[0].text)
        driver.find_element(By.CSS_SELECTOR, f"#page_list > font > a:nth-child({j})").click()
        time.sleep(0.5)
# 다음으로 넘기기 (11page로)
    driver.find_element(By.CSS_SELECTOR, "#page_list > font > a.page_next").click()
    time.sleep(0.5)

# 11페이지 부터 추출 
    for k in range(5):
        for j in range(3, 7):
            for i in range(6, 26):
                title = soup.select(f"table.board_table > tbody > tr:nth-child({i}) > td:nth-child(4) > a")
                bbomppu_list.append(title[0].text)
            driver.find_element(By.CSS_SELECTOR, f"#page_list > font > a:nth-child({j})").click() 
            time.sleep(0.5)

# fm 수집
    driver.get("https://www.fmkorea.com/index.php?mid=best&listStyle=list&page=1")
# 8페이지까지만 가져온 후 
    for j in range(9, 16):
        for i in range(2, 22):
            soup = bs(driver.page_source, "lxml")
            title = soup.select(f"#bd_189545458_0 > div > table > tbody > tr:nth-child({i}) > td.title.hotdeal_var8 > a.hx")
            fm_list.append((title[0].text).strip("\t"))
        driver.find_element(By.CSS_SELECTOR, f"#bd_189545458_0 > div > form > fieldset > a:nth-child({j})").click()
        time.sleep(0.5)
# fm 페이지 특징: 8페이지 부터는 계속 위치 고정 
    for j in range(16, 31):
        for i in range(2, 22):
            soup = bs(driver.page_source, "lxml")
            title = soup.select(f"#bd_189545458_0 > div > table > tbody > tr:nth-child({i}) > td.title.hotdeal_var8 > a.hx")
            fm_list.append((title[0].text).strip("\t"))
        driver.find_element(By.CSS_SELECTOR, "#bd_189545458_0 > div > form > fieldset > a:nth-child(16)").click() 
        time.sleep(0.5)
    
    # the qoo 수집 
    driver.get("https://theqoo.net/hot?page=1&filter_mode=normal")
    # the qoo도 7페이지 부터 페이지 순서 고정 6까지 가져오기 
    for j in range(4, 10):
        for i in range(11, 31):
            soup = bs(driver.page_source, "lxml")
            title = soup.select(f"#bd_2842877099_0 > div > table > tbody > tr:nth-child({i}) > td.title > a:nth-child(1)")
            tq_list.append((title[0].text).strip("\t"))
        driver.find_element(By.CSS_SELECTOR, f"#bd_2842877099_0 > div > form > ul > li:nth-child({j}) > a").click()
        time.sleep(0.5)
# the qoo 페이지 특징: 8페이지 부터는 계속 위치 고정 
    for j in range(11, 14):
        for i in range(11, 31):
            soup = bs(driver.page_source, "lxml")
            title = soup.select(f"#bd_2842877099_0 > div > table > tbody > tr:nth-child({i}) > td.title > a:nth-child(1)")
            tq_list.append((title[0].text).strip("\t"))
        driver.find_element(By.CSS_SELECTOR, f"#bd_2842877099_0 > div > form > ul > li:nth-child(10) > a").click()
        time.sleep(0.5)
    
# etoland 추출 
    driver.get("https://etoland.co.kr/pages/hit.php")
# 1~2 페이지 추출 
    for j in range(2, 3):
        for i in range(5, 65):
            soup = bs(driver.page_source, "lxml")
            title = soup.select(f"body > main > section > div.board_hit_wrap > ul > li:nth-child({i}) > div.subject > a.sub_link > span.subject_txt")
            eto_list.append((title[0].text).strip("\n").strip("\t"))
        driver.find_element(By.CSS_SELECTOR, f"body > main > section > div.board_hit_wrap > div.write_pages_wrap > div.write_pages > a:nth-child(2)").click()
        time.sleep(0.5)
    

    for j in range(4, 7):
        for i in range(5, 65):
            soup = bs(driver.page_source, "lxml")
            title = soup.select(f"body > main > section > div.board_hit_wrap > ul > li:nth-child({i}) > div.subject > a.sub_link > span.subject_txt")
            eto_list.append((title[0].text).strip("\n").strip("\t"))
        driver.find_element(By.CSS_SELECTOR, f"body > main > section > div.board_hit_wrap > div.write_pages_wrap > div.write_pages > a:nth-child({j})").click()
        time.sleep(0.5)
    # driver 종료
    driver.quit()

# 모아진 데이터 리스트를 df로 변환후 합치기 columns명: content
    daily_all_commu = pd.concat([pd.DataFrame(dc_list), pd.DataFrame(bbomppu_list), pd.DataFrame(fm_list), pd.DataFrame(eto_list), pd.DataFrame(tq_list)])
    daily_all_commu.columns = ["content"]

    daily_all_commu = daily_all_commu.loc[:, "content"].to_list()

# 불용어 지정. 많으면 많을 수록 좋을 듯.. 
    stopwords = ['-', 'jpg', 'ㅋ', '[ㅇㅎ]', "gif", '스압', 'ㅇㅎ', 'ㄷ', "ㅎ", ';', 'twt', 'blind', 'pann', 'gisa', '★', '☆', 'ㅠ', 'ㅜ', "manhwa", "mp4", "후방", "레전드", "주의", "JPG", 'webp', "boja"]

# 불용어가 제거된 데이터를 저장할 새로운 리스트
    filtered_list = []

    for item in daily_all_commu:
        for stopword in stopwords:
            item = item.replace(stopword, '')
        filtered_list.append(item.strip())
    # 총 데이터 갯수 확인
    my_list = filtered_list
    # CountVectorizer를 사용하여 문서를 벡터로 변환
######################################################################################################
    and_clean_list = [remove_doublequotes(s) for s in my_list]
    and_and_clean_list = [remove_doublequotes(s) for s in and_clean_list]
    vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
    X = vectorizer.fit_transform(filtered_list)
    num_topics = 6 # 원하는 토픽의 수 설정
    lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
    lda_model.fit(X)
# 중복제거하지 않은 토픽들 list 
# display 토픽 보여주기 
    num_top_words = 9
    feature_names = vectorizer.get_feature_names_out()
    for topic_idx, topic in enumerate(lda_model.components_):

        # Topic별로 1000개의 단어들(features)중에서 높은 값 순으로 정렬 후 index를 반환해줌
        # argsort()는 default가 오름차순(1, 2, 3,..) 그래서[::,-1]로 내림차순으로 바꾸기
        topic_word_idx = topic.argsort()[::-1]
        top_idx = topic_word_idx[:num_top_words]
        
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



# 키워드 삽입
    

    

# 키워드 데이터 삽입


    

# 커밋 및 연결 종료
   





def save_list_as_oracle(data_list, keyword_list):
    try:
        connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
# 커서 생성
        cursor = connection.cursor()
        insert_query = "INSERT INTO keyword_table (keyword) VALUES (:1)"
        cursor.executemany(insert_query, [(keyword, ) for keyword in keyword_list])
        for idx, article in enumerate(data_list):
            
            predictions = pipe_model.predict([article])
            prediction = predictions.tolist()  # Convert to a list
            insert_query = (
                f"INSERT INTO news (id, content, prediction) "
                f"VALUES (:id, :content, :prediction)"
            )
            
            for pred in prediction:
                cursor.execute(insert_query, id=idx, content=article, prediction=pred)
        
        connection.commit()
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()

    



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






# from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
# import cx_Oracle

# connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
# cursor = connection.cursor()






# Create an engine
#engine = create_engine(f'oracle+cx_oracle://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/xe')

# Create a session factory
#cx_Oracle.init_oracle_client(lib_dir=r"C:\\Oracle\\instantclient_19_19")




# from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT
# import cx_Oracle

# connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
# cursor = connection.cursor()



# def save_list_as_oracle(data_list):
#     try:
#         for idx, article in enumerate(data_list):
            
#             predictions = pipe_model.predict([article])
#             prediction = predictions.tolist()  # Convert to a list
#             insert_query = (
#                 f"INSERT INTO news (id, content, prediction) "
#                 f"VALUES (:id, :content, :prediction)"
#             )
            
#             for pred in prediction:
#                 cursor.execute(insert_query, id=idx, content=article, prediction=pred)
        
#         connection.commit()
#     except cx_Oracle.Error as error:
#         print("Error:", error)
#     finally:
#         cursor.close()
#         connection.close()

# save_list_as_oracle(and_and_clean_list)


# Firestore에 "article" 컬렉션에 딕셔너리 데이터 저장

def main():
    sched = BlockingScheduler()
    sched.add_job(job3,'interval', minutes=30)
    sched.start()


########################################################################

def job3():
    crawling()
    time.sleep(5)
    keyword_list, and_and_clean_list = job1()

    # save_list_as_documents("article", my_list)
    save_list_as_oracle(and_and_clean_list, keyword_list)

main()
########################################################################################

