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
# #??????????????? ??????????????? ?????? ??????
# url= "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19GenAgeCaseInfJson"
# request = ul.Request(url)
# # ???????????? ?????? url
#
# request = ul.Request(url)
# # url??? ???????????? ?????????
#
# response = ul.urlopen(request)
# # ???????????? ???????????? ?????????
#
# rescode = response.getcode()
# # ????????? ???????????? ??????????????? ???????????? ?????? ????????? 200
# if (rescode == 200):
#     responseData = response.read()
#     # ???????????? ???????????? ??????
#     rD = xmltodict.parse(responseData)
#     # XML????????? ???????????? dict???????????? ???????????????
#
#     rDJ = json.dumps(rD)
#     # dict ????????? ???????????? json???????????? ??????
#
#     rDD = json.loads(rDJ)
#     # json????????? ???????????? dict ???????????? ??????
#
#     print(rDD)
#     # ??????????????? ???????????? ??????????????? ??????
#
#     w_data = rDD["response"]["body"]["items"]["item"]
#     # ?????? dict????????? ????????? item??? ???????????? ???????????? w_data??? ??????
#
#     print('???????????? : ' + w_data["spotName"])
#     print('?????? : ' + w_data["tm"])
#     print('?????? : ' + w_data["th3"])
#     if (w_data["sky"] == '1'):
#         print('???????????? : ??????')
#     elif (w_data["sky"] == '2'):
#         print('???????????? : ????????????')
#     elif (w_data["sky"] == '3'):
#         print('???????????? : ????????????')
#     elif (w_data["sky"] == '4'):
#         print('???????????? : ??????')
#     elif (w_data["sky"] == '5'):
#         print('???????????? : ???')
#     elif (w_data["sky"] == '6' or w_data["sky"] == '7'):
#         print('???????????? : ??????')
#     elif (w_data["sky"] == '8'):
#         print('???????????? : ???')
#     else:
#         print('???????????? : ???')
#
#     print('???????????? : ' + w_data["pop"])
# #
# client_key = 'Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D'
# client_secret = 'YmIx0GW8JG'
# # ?????? quote_plus() ???????????? ????????? ?????? ??????. requests ????????? ????????? ??????
# naver_url = 'https://openapi.naver.com/v1/search/news.json?query=????????????'
#
# header_params = {"X-Naver-Client-Id":client_key, "X-Naver-Client-Secret":client_secret}
# # headers= header_params ??? header ??????????????? ????????????, ????????? ?????????, requests.get(????????? URL) ??? ?????? ???
# response = requests.get(naver_url, headers = header_params)
# # ?????? json.loads() ??????????????? ????????? ???????????? ?????????, reqeusts ?????????????????? ?????? json() ???????????? ????????? ?????? ?????????
# # print(response.json())
# # print(response.text)
#
# # HTTP ?????? ????????? status_code ??? ?????????
# if(response.status_code == 200):
#     data = response.json()
#     print(data['items'][0]['title'])
#     print(data['items'][0]['description'])
# else:
#     print("Error Code:" + response.status_code)

# ?????? ?????????????????????: 20.07.29
# ????????? ??????

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

driver.get(url) #get?????? ????????? driver ??????
 #url??????
#??????????????? ?????? ??????
url="http://finance.daum.net/"
contents_list=[] #????????? ????????? ?????? ????????????
#?????? ??????????????? ?????? ??????
#driver=webdriver.Chrome("C:\PythonStudy\driver\chromedriver")
result=requests.get(url)
#bs_obj=BeautifulSoup(result.content,"html.parser")
for i in range(5): #???10?????? url??? ?????? ??????????????????
    driver.get(urls_list[i])
    print(driver.current_url)
    time.sleep(3)

    time.sleep(3)
# ?????? ?????? time.sleep() ??? ?????? ????????? chromedriver ??? ????????? ???????????? ????????????.
# ???????????? ?????? ????????? ????????? ????????? ????????? ??? ??????.

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
#???????????? ???????