# areacode 지역 코드 출력
# 공공데이터포탈 한국 관광 공사 지역기반 관광정보 조회

import requests
from bs4 import BeautifulSoup

endpoint="http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaCode?"
serviceKey="Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D"
numOfRows="20" #한 페이지 결과 수
pageSize="1" # 현재 페이지 수(크기)
pageNo="1" # 현재 페이지 번호
MobileOS= "ETC"
MobileApp= "AppTest" # 서비스 어플명

paramset = "serviceKey=" +serviceKey +"&"\
           +'numOfRows=' + numOfRows+"&"\
            +"pageSize=" + pageSize +"&"\
            +'pageNo=' + pageNo + "&" \
            +'MobileOS='+ MobileOS+"&" \
            +'MobileApp='+MobileApp
url= endpoint+paramset
result=requests.get(url)

bs_obj =BeautifulSoup(result.content,'html.parser')
print(bs_obj)

items = bs_obj.findAll('item')
for item in items:
    print(item.find('rnum').text, end=",")
    print(item.find('name').text)
    