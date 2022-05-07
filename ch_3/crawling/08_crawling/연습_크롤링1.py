# import requests
# from bs4 import BeautifulSoup as bs
#
# url = 'https://finance.daum.net/api/search/ranks?limit=10'
# headers = {
#             'Referer': 'http://finance.daum.net',
#             'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36 OPR/58.0.3135.127'
# }
# response = requests.get(url, headers=headers)
# jsonObjs = response.json()
# dataList = jsonObjs['data']
# for data in dataList :
#   print(data['name'])
#

import requests
import json
import sys
import io
import numpy as np
import pandas as pd
import pandas as pd
from bs4 import BeautifulSoup
import requests
startnumber=1
endnumber=1000
CommerceInfor = {}
codelist = []
codenamelist = []
totalnumberlist = []
maletotallist = []
femaletotallist = []
agrade_10list = []
agrade_20list = []
agrade_30list = []
agrade_40list = []
agrade_50list = []
above_60list = []
while endnumber<=2000:
    url='http://openapi.data.go.kr/openapi/service/rest/Covid19/ getCovid19GenAgeCaseInfJson'
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    codenumber = soup.find_all('trdar_cd')
    codename = soup.find_all('trdar_cd_nm')
    totalnumber = soup.find_all('tot_flpop_co')
    maletotal = soup.find_all('ml_flpop_co')
    femaletotal = soup.find_all('fml_flpop_co')
    agrade_10 = soup.find_all('agrde_10_flpop_co')
    agrade_20 = soup.find_all('agrde_20_flpop_co')
    agrade_30 = soup.find_all('agrde_30_flpop_co')
    agrade_40 = soup.find_all('agrde_40_flpop_co')
    agrade_50 = soup.find_all('agrde_50_flpop_co')
    above_60 = soup.find_all('agrde_60_above_flpop_co')
    for code in codenumber:
        codelist.append(code.text)
    for code in codename:
        codenamelist.append(code.text)
    for code in totalnumber:
        totalnumberlist.append(code.text)
    for code in maletotal:
        maletotallist.append(code.text)
    for code in femaletotal:
        femaletotallist.append(code.text)
    for code in agrade_10:
        agrade_10list.append(code.text)
    for code in agrade_20:
        agrade_20list.append(code.text)
    for code in agrade_30:
        agrade_30list.append(code.text)
    for code in agrade_40:
        agrade_40list.append(code.text)
    for code in agrade_50:
        agrade_50list.append(code.text)
    for code in above_60:
        above_60list.append(code.text)
startnumber+=1000
endnumber+=1000
# import urllib.request as ul
# import xmltodict
#
#
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
# #아톰에디터 한글사용을 위한 구문
# url= "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson"
# request = ul.Request(url)
# # 데이터를 받을 url
#
# request = ul.Request(url)
# # url의 데이터를 요청함
#
# response = ul.urlopen(request)
# # 요청받은 데이터를 열어줌
#
# rescode = response.getcode()
# # 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
# if (rescode == 200):
#     responseData = response.read()
#     # 요청받은 데이터를 읽음
#     rD = xmltodict.parse(responseData)
#     # XML형식의 데이터를 dict형식으로 변환시켜줌
#
#     rDJ = json.dumps(rD)
#     # dict 형식의 데이터를 json형식으로 변환
#
#     rDD = json.loads(rDJ)
#     # json형식의 데이터를 dict 형식으로 변환
#
#     print(rDD)
#     # 정상적으로 데이터가 출력되는지 확인
#
#     w_data = rDD["response"]["body"]["items"]["item"]
#     # 해당 dict형식의 파일의 item을 사용하기 편하도록 w_data에 저장
#
#     print('관광지명 : ' + w_data["spotName"])
#     print('시간 : ' + w_data["tm"])
#     print('기온 : ' + w_data["th3"])
#     if (w_data["sky"] == '1'):
#         print('하늘상태 : 맑음')
#     elif (w_data["sky"] == '2'):
#         print('하늘상태 : 구름조금')
#     elif (w_data["sky"] == '3'):
#         print('하늘상태 : 구름많음')
#     elif (w_data["sky"] == '4'):
#         print('하늘상태 : 흐림')
#     elif (w_data["sky"] == '5'):
#         print('하늘상태 : 비')
#     elif (w_data["sky"] == '6' or w_data["sky"] == '7'):
#         print('하늘상태 : 눈비')
#     elif (w_data["sky"] == '8'):
#         print('하늘상태 : 눈')
#     else:
#         print('하늘상태 : ???')
#
#     print('강수확률 : ' + w_data["pop"])
# #
# client_key = 'Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D'
# client_secret = 'YmIx0GW8JG'
# # 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌
# naver_url = 'https://openapi.naver.com/v1/search/news.json?query=스마트폰'
#
# header_params = {"X-Naver-Client-Id":client_key, "X-Naver-Client-Secret":client_secret}
# # headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
# response = requests.get(naver_url, headers = header_params)
# # 별도 json.loads() 라이브러리 메서드 사용하지 않아도, reqeusts 라이브러리에 있는 json() 메서드로 간단히 처리 가능함
# # print(response.json())
# # print(response.text)
#
# # HTTP 응답 코드는 status_code 에 저장됨
# if(response.status_code == 200):
#     data = response.json()
#     print(data['items'][0]['title'])
#     print(data['items'][0]['description'])
# else:
#     print("Error Code:" + response.status_code)

# 마켓 트렌드당일기준: 20.07.29
# 상승률 상위

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time
urls_list=[]
for urls in source.find_all('a'{'class':'box_contents'}):
    new_url_content= urls["href"][-21:-4]
    new_url ="http://finance.daum.net/domestic"+new_url_content
    new_url_

driver = webdriver.Chrome('./chromedriver.exe')
html = driver.execute_script('return document.body.innerHTML')
soup = BeautifulSoup(result.content,'html.parser')

driver.get(url) #get함수 이용한 driver 생성
 #url생성
#검색창에서 주소 복사
url="http://finance.daum.net/"
contents_list=[] #수집할 주식을 위해 빈리스트
#크롬 드라이버를 통한 접속
#driver=webdriver.Chrome("C:\PythonStudy\driver\chromedriver")
result=requests.get(url)
#bs_obj=BeautifulSoup(result.content,"html.parser")
for i in range(5): #총10개의 url의 주식 정보수집예쩡
    driver.get(urls_list[i])
    print(driver.current_url)
    time.sleep(3)

    time.sleep(3)
# 중간 중간 time.sleep() 이 있는 이유는 chromedriver 가 제대로 작동하기 위함이다.
# 시간차를 주지 않으면 중간에 오류가 발생할 수 있다.

driver.page_source
all_a=driver.find_elements_by_css_selector('ul.list.boxKospi > li > a.txt')
a_text=[a.text for a in all_a]
for txt in a_text:
    print(txt)

driver.close
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://datalab.naver.com/shoppingInsight/sCategory.naver")

time.sleep(3)
tag_names = browser.find_element_by_css_selector(".rank_top1000_list").find_elements_by_tag_name("li")
for tag in tag_names:
    print(tag.text.split("\n"))
#안됩니다 왜죠?