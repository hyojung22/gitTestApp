import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

from tqdm import tqdm
import re
import pickle
import csv
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import os
from sklearn.decomposition import LatentDirichletAllocation
from joblib import dump

from sklearn.pipeline import make_pipeline
from sklearn.model_selection import GridSearchCV

dc_list = []
bbomppu_list = []
fm_list = []
tq_list = []
eto_list = []
# 옵션 생성
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


# 모아진 데이터 불용어 처리 
daily_all_commu = pd.concat([pd.DataFrame(dc_list), pd.DataFrame(bbomppu_list), pd.DataFrame(fm_list), pd.DataFrame(eto_list), pd.DataFrame(tq_list)])
daily_all_commu.columns = ["content"]
daily_all_commu.to_csv("230801_daily_commu.csv", encoding='utf-8-sig')
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
print(len(filtered_list))



vectorizer = CountVectorizer(max_df = 0.3, min_df = 1, stop_words="english", ngram_range=(3, 3))
X = vectorizer.fit_transform(filtered_list)
#LDA 모델 학습
num_topics = 4 # 원하는 토픽의 수 설정
lda_model = LatentDirichletAllocation(n_components=num_topics, random_state= 42)
lda_model.fit(X)


#모델 덤프
dump(lda_model, 'lda.joblib') 

