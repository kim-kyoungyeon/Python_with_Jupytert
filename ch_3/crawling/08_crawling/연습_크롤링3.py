import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
#url생성
#검색창에서 주소 복사
url = "http://finance.daum.net/"
with urllib.request.urlopen(url) as f:
    html = f.read().decode('utf-8')
#크롬 드라이버를 통한 접속
driver=webdriver.Chrome("C:\PythonStudy\driver\chromedriver")
driver.get(url)

result=requests.get(url)
bs_obj=BeautifulSoup(result.content,"html.parser")

driver.page_source
#금융>국내>외국인순매수 상위5개 주식 추출
all_a=driver.find_elements_by_css_selector('div.class.tableB.half.mr.mb>txt > a.txt')
a_text=[a.text for a in all_a]
for txt in a_text:
    print(txt)
driver.close

#질문 : list가 아니라 확인해보니 table 형태의 txt형태인 주식리스트는 어떻게 추출하나요?