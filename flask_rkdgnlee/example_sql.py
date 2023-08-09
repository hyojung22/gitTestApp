import cx_Oracle
from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT

connection = cx_Oracle.connect(DB_USERNAME, DB_PASSWORD, f'{DB_HOST}:{DB_PORT}/xe')
cursor = connection.cursor()

def print_news_data():
    try:
        cursor.execute("SELECT id, content FROM news")
        news_contents = cursor.fetchall()
        for id, content in news_contents:
            print(f"ID: {id}")
            print(f"Content: {content}")
            print("=" * 20)
    except cx_Oracle.Error as error:
        print("Error:", error)
    finally:
        cursor.close()
        connection.close()

print_news_data()