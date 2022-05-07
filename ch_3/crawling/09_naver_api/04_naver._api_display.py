#네이버 api 겨로가 기본값 10개
#검색 결과를 100개로 설정
#   api 요청변수
#   documents / 검색에서
#   요청변수 변경
#   요청 변수: display
#   display =100을 url에 넣고 호출시 설정값대로 결과 반환
import requests
from urllib.parse import urlparse
keyword='강남역'
display = 10
#변수값을 지정해서 값 저장 및 변경
#url = 'https://openapi.naver.com/v1/search/blog?query='+keyword + "&display=100"
url = 'https://openapi.naver.com/v1/search/blog?query='+keyword + "&display="+str(display)
result= requests.get(urlparse(url).geturl(),
                     headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                              "X-Naver-Client-Secret":'fvK2Z7QkHF'})

json_obj= result.json()
#검색결과개수확인
#요청변수 display
print(json_obj['display'])#10 (기본10개)
#시작위치확인
#요청변수 start
print(json_obj['start'])

#총 item 개수확인
print(len(json_obj["items"])) #10개
#현재 dispaly가 10으로 설정

#url 에서 display위치
#keyword 다음 "&display=100" 형태로 연결
#100개 출력확인
#제목 링크출력
num=0
for items in json_obj["items"]:
    num +=1
    print(str(num)+":"+items['title'].replace("<b>","").replace("</b>",""),items['link'])












