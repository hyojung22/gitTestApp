import firebase_admin
from firebase_admin import credentials, db
from firebase_admin import firestore
cred = credentials.Certificate("flask_rkdgnlee\\data-base-ee338-firebase-adminsdk-f6bdn-b1c809dc33.json")

firebase_admin.initialize_app(cred)
db = firestore.client()


# Add a new doc in collection 'cities' with ID 'LA'

doc_ref = db.collection("users").document("alovelace")
doc_ref.set({"first": "Ada", "last": "Lovelace", "born": 1815})

users_ref = db.collection("users")
docs = users_ref.stream()

for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")

#https://firebase.google.com/docs/firestore/quickstart?hl=ko
#word2vec autoML
# import os
# import time
# from selenium import webdriver

# def save_crawling_result(text):
#     # 현재 시간을 이용하여 파일명 생성
#     current_time = time.strftime("%Y%m%d_%H%M%S", time.localtime())
#     file_name = f"crawling_result_{current_time}.txt"
    
#     # 파일을 열어 크롤링 결과를 저장
#     with open(file_name, 'w', encoding='utf-8') as file:
#         file.write(text)

# def crawl_website():
#     try:
#         # Selenium 코드를 이용하여 크롤링 작업 수행
#         driver = webdriver.Chrome()
#         driver.get("https://www.example.com")
#         text_to_save = driver.page_source
        
#         # 크롤링 결과를 파일로 저장
#         save_crawling_result(text_to_save)
        
#         driver.quit()
#         return {"statusCode": 200, "body": "Crawling and saving successful."}
#     except Exception as e:
#         # 크롤링 실패 시 에러 메시지와 함께 로그 출력
#         print("Crawling failed:", str(e))
#         return {"statusCode": 500, "body": "Crawling failed."}

# # 테스트용으로 crawl_website() 함수 호출
# response = crawl_website()
# print(response)

#aws 람다에서 selenium 실행하기