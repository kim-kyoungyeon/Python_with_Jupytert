
import requests
import urllib.request as req
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import time, csv
output= "test_crawling.csv"#csv저장
csv_open = open(output, 'w+', encoding='utf-8')
csv_writer = csv.writer(csv_open)
csv_writer.writerow('reply')
# 크롤링 url, html 받아오기

orig_url = 'http://finance.daum.net/news/20200730170214862' # 크롤링 할 사이트
driver = webdriver.Chrome('C:\PythonStudy\driver\chromedriver') # 크롬 브라우저 선택
driver.get(orig_url) # 입력한 경로의 정보 긁어볼까요~?
pages = 0
try:
    while 1:
        driver.find_element_by_css_selector(".alex_more").click()
        time.sleep(2)
        print(pages, end=" ")
        pages += 1
except exceptions.ElementNotVisibleException as e:
    pass
except Exception as e:
    print(e)

html=driver.page_source
soup=BeautifulSoup(html,'html.parser')
dom = BeautifulSoup(html, "lxml")
comment_raw= soup.find_all('span',{"class":"desc_txt.font_size_"})
comments = [comment.text for comment in comment_raw]

comments[:10]
#comment= soup.find_all('span',{"class":"desc_txt.font_size_"})
# comments = [comment.text for comment in comments_raw]
# comments[:3]

# review_list=[]
#
# for i in range(10): # 최대10개
#     link=orig_url.format(i)
#     driver.get(link)
#     time.sleep(3)
#
#     html= driver.page_source
#     soup.BeautifulSoup(html,'html.parser')
#     comment=soup.find_all('dd',{'class':'usertext'})
#     for review in comment:
#         review_list.append(review.get_text().strip())
#
#     for a in review_list:
#         print(a+'\n')