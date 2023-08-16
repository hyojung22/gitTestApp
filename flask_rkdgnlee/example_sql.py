import cx_Oracle
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT



import json



connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
cursor = connection.cursor()



# my_list = []
# def print_news_data():
#     # try:
#     cursor.execute("SELECT id, content, prediction FROM news")
#     news_contents = cursor.fetchall()
#     news_data = [
#         {'id': id, 'content': content, 'prediction': prediction}
#         for id, content, prediction in news_contents
#     ]
#     return news_data
#     # except cx_Oracle.Error as error:
#     #     print("Error:", error)
#     # finally:
#     #     cursor.close()
#     #     connection.close()


# print(print_news_data())

# json_data = json.dumps(print_news_data())

# print("JSON data:", json_data)





# update_query = """
# UPDATE news
# SET content = REPLACE(content, '"', '')
# """

# try:
#     # Execute the update query
#     cursor.execute(update_query)

#     # Commit the changes
#     connection.commit()
# except cx_Oracle.Error as error:
#     print("Error:", error)
# finally:
#     # Close the cursor and connection
#     cursor.close()
#     connection.close()






# content 컬럼의 값을 삼중쿼트로 감싸는 작업 수행
# cursor.execute("UPDATE news SET content = '''' || content || ''''")

# # 변경사항을 커밋
# cursor.close()
# connection.close()







# def drop_table(table_name):
#     try:
#         drop_query = f"DROP TABLE {table_name}"
#         cursor.execute(drop_query)
#         print(f"Table {table_name} dropped successfully.")
        
#         connection.commit()
#     except cx_Oracle.Error as error:
#         print("Error:", error)
#     finally:
#         cursor.close()
#         connection.close()

# # Replace 'news' with your actual table name
# drop_table('news')




# def create_news_table():
#     try:
#         create_query = (
            
#             "CREATE TABLE news ("
#             "id NUMBER PRIMARY KEY,"
#             "content VARCHAR2(1500 CHAR),"
#             "prediction NUMBER"
#             ")"
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







# create_table_query = """
# CREATE TABLE keyword_table (
#     id NUMBER PRIMARY KEY,
#     keyword VARCHAR2(255)
# )
# """
# cursor.execute(create_table_query)

# # 커밋 및 연결 종료
# connection.commit()
# cursor.close()
# connection.close()




# def drop_table(table_name):
#     try:
#         drop_query = f"DROP TABLE {table_name}"
#         cursor.execute(drop_query)
#         print(f"Table {table_name} dropped successfully.")
        
#         connection.commit()
#     except cx_Oracle.Error as error:
#         print("Error:", error)
#     finally:
#         cursor.close()
#         connection.close()

# # Replace 'news' with your actual table name
# drop_table('keyword_table')
