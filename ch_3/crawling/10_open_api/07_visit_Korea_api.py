# 공공데이터포탈 한국 관광 공사 지역기반 관광정보 조회

import requests
from bs4 import BeautifulSoup

endpoint="http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?"
serviceKey="Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D"
numOfRows="10" #한 페이지 결과 수
pageSize="1" # 현재 페이지 수(크기)
pageNo="1" # 현재 페이지 번호
MobileOS= "ETC" # IOS 아이폰 AND 안드로이드 WIN 윈도폰
#ETC 기타
MobileApp= "AppTest" # 서비스 어플명
arrange="A" # A는 제목순 B는 조회순  C 는 수정일순 D 생성일순
contentTypeId="15" # 관광타입 관광지/숙박등 : ID, 15 축제 공연 행사
areaCode='1' # 지역코드
sigunguCode="4" #시군구 코드
listYN="Y"      # 목록 구분 (Y :목록, N:개수)

paramset = "serviceKey=" +serviceKey +"&"\
           +'numOfRows=' + numOfRows+"&"\
            +"pageSize=" + pageSize +"&"\
            +'pageNo=' + pageNo + "&" \
            +'MobileOS='+ MobileOS+"&" \
            +'MobileApp='+MobileApp +"&" \
            +"arrange="+arrange +"&" \
            +'contentTypeId=' + contentTypeId +"&" \
            +'areaCode='+ areaCode+"&" \
            +'sigunguCode='+ sigunguCode +"&" \
            +'listYN='+listYN
url= endpoint +paramset
print(url)
result= requests.get(url)
bs_obj=BeautifulSoup(result.content,"html.parser")
#print(bs_obj)
#print(bs_obj.findAll("title"))
#모든 items 찾기
#print(bs_obj.findAll('items'))
# items = bs_obj.findAll("title")
# for item in items:
#     print(item.text)

# 제목과 주소만 출력

items=bs_obj.findAll("item")

# for item in items:
#     title=item.find('title').text
#     addr= item.find('addr1').text
#     print(title,",",addr)

for item in items:
    print(item.find("title").text,end=',')
    print(item.find("addr1").text)























































