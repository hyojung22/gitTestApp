#이 코드는 훈련데이터 생성을 위한 코드입니다.

#data_split
from sklearn.model_selection import train_test_split

#beautifulSoup
from bs4 import BeautifulSoup as bs


#selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys



#pandas
import pandas as pd
import requests
import time



driver = webdriver.Chrome()

#headless
#options = webdriver.ChromeOptions()
#options.add_argument('--headless=new')
#driver = webdriver.Chrome(options=options)

url = "https://www.bigkinds.or.kr/v2/news/index.do"
driver.get(url)


#필드 찾기    
input_field = driver.find_element(By.ID, "total-search-key")  # Replace "input_id" with the actual ID of the input field


#input필드
input_field.send_keys(" ")

time.sleep(1)

#엔터
input_field.send_keys(Keys.RETURN)



time.sleep(1.5)


news_title_list = []
news_body_list = []

##### 수집페이지
#1만개에서 3만개 기사 수집 목표        

for j in range(1, 10):

	time.sleep(1.5)
	
	#사이트 리프레시
	#driver.refresh
	#driver.get(url)
	
	#input_field = driver.find_element(By.ID, "total-search-key")  # Replace "input_id" with the actual ID of the input field
	#input_field.send_keys(" ")
	#input_field.send_keys(Keys.RETURN)
	#time.sleep(1.5)



	next_page = driver.find_element(By.ID, "paging_news_result")  # Replace "input_id" with the actual ID of the input field
	next_page.clear()
	next_page.send_keys(j)
	next_page.send_keys(Keys.RETURN)
	try:	
		for i in range(3):
            
			#기사 타이틀 클릭
			news_button = driver.find_elements(By.CSS_SELECTOR, "span.title-elipsis")
			news_button[i].click()
			time.sleep(1)
			#본문
			news_body = driver.find_element(By.CSS_SELECTOR, "div.news-view-body")    
			news_body_list.append(news_body.get_attribute("innerText"))
			close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer>button.btn.btn-round.btn-wh").click()  
			time.sleep(1)
	except:
    		print("파싱완료")


######수집페이지 끝

###### 데이터 프레임으로 만들어서 csv로 내보내기

#csv로 내보낼때는 labeling이 안되어있어 스스로 해줘야함

#create_train_data(df['content'], df['label'])

#df_x_train, df_x_test, df_y_train, df_y_test = train_test_split(df_x_data, df_y_data, test_size=0.3, random_state=777, stratify=df_y_data)

#news_train.csv
#news_test.csv



print(news_body_list)

#잠시주석    
dic = {'content':news_body_list}




pd.DataFrame(dic)
news = pd.DataFrame(dic)


news.to_csv('preprocessing_news_train.csv')
#news.to_csv('news_test.csv')
#news

