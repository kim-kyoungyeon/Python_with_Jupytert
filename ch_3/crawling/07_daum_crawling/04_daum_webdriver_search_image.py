#다음은 자바스트립트 써서 동적으로 구성되어 있음

import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as parse

base="https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q="
quote=parse.quote("떡")
url=base+quote

#크롬 드라이버를 통한 접속
driver=webdriver.Chrome("C:\PythonStudy\driver\chromedriver")
driver.get(url)

result=requests.get(url)
bs_obj=BeautifulSoup(result.content,"html.parser")


#이미지 파일 저장할 디렉토리설정
savepath="c:\\image_down\\"
#파일 저장 시 오류 발생에 대비해서 예외 처리
try:
    if not (os.path.isdir(savepath)):
        os.mkdir(os.path.join(savepath))
except OSError as e:
    print("저장실패")


img_list=driver.find_elements_by_css_selector('div#imgList > div.wrap_thumb > a.link_thumb > img')
data_src=[img.get_attribute("data-src") for img in img_list] #데이터 소스 직접 추출

for i in range(len(data_src)):
    fullFileName = os.path.join(savepath + str(i) + '.jpg')
    req.urlretrieve(data_src[i], fullFileName)


