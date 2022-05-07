# 함수로 묶기
#get_ api_result 함수
# #   +keyword 와 display를 전달 받아> api 결과 반환
# 함수 호출해서 결과 받아 출력
# json obj변수가 받음
#
import requests
from urllib.parse import urlparse
def get_api_result(keyword,display):
    url = 'https://openapi.naver.com/v1/search/blog?query=' + keyword + "&display="+str(display)
    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    return result.json()
keyword=   '강남역'
display = 50
json_obj=get_api_result('밥',display)
num=0
for items in json_obj["items"]:
    num +=1
    print(str(num)+":"+items['title'].replace("<b>","").replace("</b>",""),items['link'])
