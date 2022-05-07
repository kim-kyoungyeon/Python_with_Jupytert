# 마켓 트렌드당일기준: 20.07.29
# 상승률 상위

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
#url생성
#검색창에서 주소 복사
url="http://finance.daum.net/"

#크롬 드라이버를 통한 접속
driver=webdriver.Chrome("C:\PythonStudy\driver\chromedriver")
driver.get(url)

result=requests.get(url)
bs_obj=BeautifulSoup(result.content,"html.parser")

driver.page_source
all_a=driver.find_elements_by_css_selector('ul.list.boxKospi > li > a.txt')
a_text=[a.text for a in all_a]
for txt in a_text:
    print(txt)

driver.close