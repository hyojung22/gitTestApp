#이 코드는 훈련데이터 생성을 위한 코드입니다.


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


#driver = webdriver.Chrome()
def crawling():
#headless
	options = webdriver.ChromeOptions()
	options.add_argument('--headless=new')
	driver = webdriver.Chrome(options=options)
	
	url = "https://www.bigkinds.or.kr/v2/news/index.do"
	driver.get(url)


#필드 찾기    
	input_field = driver.find_element(By.ID, "total-search-key")

	time.sleep(1)

#엔터
	input_field.send_keys(" ", Keys.RETURN)



	time.sleep(1)


	news_title_list = []
	news_body_list = []

##### 수집페이지
#1만개에서 3만개 기사 수집 목표        

	for j in range(1, 5):

		next_page = driver.find_element(By.ID, "paging_news_result")  
		next_page.clear()
		next_page.send_keys(str(j), Keys.RETURN)
		time.sleep(8)
		try:	
			for i in range(10):
		
	#기사 타이틀 클릭
				title = driver.find_elements(By.CSS_SELECTOR, "span.title-elipsis")
				news_title_list.append(title[i])
				news_button = driver.find_elements(By.CSS_SELECTOR, "a.thumb.news-detail")
	#news_button[i].click()
				news_button[i].click()
				time.sleep(0.5)
	#본문		
				news_body = driver.find_element(By.CSS_SELECTOR, "div.news-view-body")    
				news_body_list.append(news_body.get_attribute("innerText"))
				time.sleep(1)
				driver.find_element(By.CSS_SELECTOR, "div.modal-footer>button.btn.btn-round.btn-wh").click()  
		except:
			print("파싱완료")


######수집페이지 끝

###### 데이터 프레임으로 만들어서 csv로 내보내기



	print(news_body_list)

#잠시주석    
	dic = {'title': news_title_list, 'content':news_body_list }




	pd.DataFrame(dic)
	news = pd.DataFrame(dic)
	news.to_csv('news_list.csv')

crawling()