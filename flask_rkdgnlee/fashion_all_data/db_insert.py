
import cx_Oracle
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT
import json






connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
cursor = connection.cursor()





########################################################################
#data.json
#festival- position create_table


# def create_news_table():
#     try:
#         create_query = (
            
#       """
#     CREATE TABLE positions (
#         title VARCHAR2(255),
#         contents VARCHAR2(2000),
#         period VARCHAR2(100),
#         location VARCHAR2(255),
#         lat NUMBER,
#         lng NUMBER,
#         page_url VARCHAR2(255)
#     )
# """
            
#         )
        
#         cursor.execute(create_query)
#         print("Table news created successfully.")
        
#         connection.commit()
#     except cx_Oracle.Error as error:
#         print("Error:", error)
#     finally:
#         cursor.close()
#         connection.close()

# create_news_table()




# drop_table_sql = "DROP TABLE positions"

# # # 테이블 삭제 실행
# try:
#     cursor.execute(drop_table_sql)
#     print("Table dropped successfully.")
#     connection.commit()
# except cx_Oracle.Error as error:
#     print("Error:", error)
# finally:
#     cursor.close()
#     connection.close()










# 만들고 집어넣기


# JSON 파일 불러오기
# with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\fashion_all_data\\data.json", "r", encoding="utf-8") as json_file:
#     json_data = json.load(json_file)

# # JSON 데이터 확인
# print(json_data)


# try:
#     for position in json_data["positions"]:
#         query = """
#             INSERT INTO positions (title, contents, period, location, lat, lng, page_url)
#             VALUES (:title, :contents, :period, :location, :lat, :lng, :page_url)
#         """
#         data = {
#             "title": position["title"],
#             "contents": position['contents'],  # JSON 데이터를 문자열로 변환
#             "period": position["period"],
#             "location": position["location"],
#             "lat": position["lat"],
#             "lng": position["lng"],
#             "page_url": position["page_url"]
#         }
#         cursor.execute(query, data)

#     connection.commit()
# except cx_Oracle.Error as error:
#     print("Error:", error)
# finally:
#     cursor.close()
#     connection.close()
##########################################################################################################


#all.json


#테이블 만들기

# def create_news_table():
#     try:
#         create_table_sql = """
#         CREATE TABLE BOOKS (
#         ID NUMBER,
#         제목 VARCHAR2(255),
#         저자 VARCHAR2(50),
#         가격 VARCHAR2(50),
#         주소 VARCHAR2(1000),
#         설명 VARCHAR2(3000)
#     )
# """         
        
        
#         cursor.execute(create_table_sql)
#         print("Table news created successfully.")
        
#         connection.commit()
#     except cx_Oracle.Error as error:
#         print("Error:", error)
#     finally:
#         cursor.close()
#         connection.close()

# create_news_table()





# with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\fashion_all_data\\all.json", "r", encoding="utf-8") as json_file:
#     json_data = json.load(json_file)

# JSON 데이터 확인
# print(json_data["설명"]["0"])


# def truncate_text(text, max_length):
#     if len(text) > max_length:
#         truncated_text = text[:max_length]
#         return truncated_text
#     return text

# # 최대 길이로 문자열 자르기
# max_description_length = 1000

# insert_sql = "INSERT INTO BOOKS (제목, 저자, 가격, 주소, 설명) VALUES (:title, :author, :price, :address, :description)"

# with connection.cursor() as cursor:
#     for idx in range(len(json_data["제목"])):
#         original_description = json_data["설명"][str(idx)]
#         truncated_description = truncate_text(original_description, max_description_length)
        
#         cursor.execute(
#             insert_sql,
#             title=json_data["제목"][str(idx)],
#             author=json_data["저자"][str(idx)],
#             price=json_data["가격"][str(idx)],
#             address=json_data["주소"][str(idx)],
#             description=truncated_description  # 자른 설명 사용
#         )
#     connection.commit()

# # 연결 종료
# connection.close()










# drop_table_sql = "DROP TABLE BOOKS"

# # 테이블 삭제 실행
# try:
#     cursor.execute(drop_table_sql)
#     print("Table dropped successfully.")
#     connection.commit()
# except cx_Oracle.Error as error:
#     print("Error:", error)
# finally:
#     cursor.close()
#     connection.close()






#fashion 



# def create_news_table():
#     try:
#         create_table_sql = """
#         CREATE TABLE fashion (
#             브랜드 VARCHAR2(100),
#             옷 VARCHAR2(200),
#             가격 VARCHAR2(150),
#             주소 VARCHAR2(500)
#         )
#         """
        
        
#         cursor.execute(create_table_sql)
#         print("Table news created successfully.")
        
#         connection.commit()
#     except cx_Oracle.Error as error:
#         print("Error:", error)
#     finally:
#         cursor.close()
#         connection.close()

# create_news_table()


# # 테이블 삭제
# drop_table_sql = "DROP TABLE fashion"

# try:
#     cursor.execute(drop_table_sql)
#     print("Table dropped successfully.")
#     connection.commit()
# except cx_Oracle.Error as error:
#     print("Error:", error)
# finally:
#     cursor.close()
#     connection.close()



# with open("C:\\Users\\gjaischool1\\OneDrive - 인공지능산업융합사업단\\바탕 화면\\gitTest\\flask_rkdgnlee\\fashion_all_data\\fashion.json", "r", encoding="utf-8") as json_file:
#     json_data = json.load(json_file)

# # JSON 데이터 확인
# print(json_data["가격"]["0"])

# insert_sql = "INSERT INTO fashion (브랜드, 옷, 가격, 주소) VALUES (:brand, :cloth, :price, :address)"


# with connection.cursor() as cursor:
#     for idx in range(len(json_data["브랜드"])):
#         cursor.execute(
#             insert_sql,
#             brand=json_data["브랜드"][str(idx)],
#             cloth=json_data["옷"][str(idx)],
#             price=json_data["가격"][str(idx)],
#             address=json_data["주소"][str(idx)]
#             )
#         connection.commit()

# # 연결 종료
# connection.close()