
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests as req
from bs4 import BeautifulSoup as bs 
import time
import pandas as pd
import numpy as np


festival_url = "https://korean.visitkorea.or.kr/kfes/list/wntyFstvlList.do" #축제 url 
driver = wb.Chrome()
driver.get(festival_url)

# 개최중만 검색 
classify_period = driver.find_element(By.CSS_SELECTOR, "#searchDate > option:nth-child(2)")
classify_period.click()
search_btn = driver.find_element(By.CSS_SELECTOR, "#btnSearch")
search_btn.send_keys(Keys.ENTER)
time.sleep(1)
# 개최중인 축제 리스트 볼 수 있게 END키 사용
for i in range(9):
    body = driver.find_element(By.CSS_SELECTOR, "body")
    body.send_keys(Keys.END)
    time.sleep(1)
# 축제 갯수는 최대 100개
for j in range(1, 101):
    try:
        li_content = driver.find_element(By.CSS_SELECTOR, f"#fstvlList > li:nth-child({j}) > a")
        li_content.click()
        content_extract_festival()
    except:
        break