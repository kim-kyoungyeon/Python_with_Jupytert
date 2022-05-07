# 이전 검색 결과 최대 100개
# 그러면 500개 이상 어떻게 추출
#    시작 위치 값을 다르게 적어서 추출
#   101부터 100개
#   201 부터 100개
 #  ...100개 "총 500개 추출가능"
 # 시작 위치 값ㅇ르 변경하려면
 #  요청 변수 start 값 설정
 #  start = 101
import requests
from urllib.parse import urlparse
def get_api_result(keyword,display,start):
    url = 'https://openapi.naver.com/v1/search/blog?query=' \
          + keyword + "&display="\
          +str(display)+ "&start="+str(start)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    return result.json()
keyword=   '강남역'
display = 100
start= 101
json_obj=get_api_result(keyword,display,start) # 함수호출시 변수  #keyword에 추출하고싶은 단어

num = start-1
for items in json_obj["items"]:
    num +=1
    print(str(num)+":"+items['title'].replace("<b>","").replace("</b>",""),items['link'])
