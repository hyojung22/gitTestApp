# selenium, BeautifulSoup, pandas, lxml, sklearn 설치 필요 
# pip install "selenium" 설치 가능 
import selenium.webdriver as wb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd 
import time


#blockingScheduler -> background로!
from apscheduler.schedulers.background import BlockingScheduler
sched = BlockingScheduler()



#collect_news.py
from collect_news import crawling
from daily_crawling_csv_serve import module_1, save_list_as_oracle, keyword_update




########################################################################


# 데이터 수집 시작 
dc_list = []
bbomppu_list = []
fm_list = []
tq_list = []
eto_list = []
keyword_li= []
# 옵션 생성




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

    #daily_all_commu = daily_all_commu.loc[:, "content"].to_list()
    
     
    df = pd.DataFrame(daily_all_commu)
     
# saving the dataframe
    df.to_csv('2023_08_16_daily_all_commu.csv')

# @sched.scheduled_job('cron', hour='9', id='test_2')
# def main():
    # job3()


########################################################################

def job3():
    crawling()
    # time.sleep(5)
    job1()
    keyword_list, and_list = module_1()
    save_list_as_oracle(and_list) 
    keyword_update(keyword_list)

# main()
job3()


########################################################################################

