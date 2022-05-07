#앞의 예제를 start값에 다라
#페이지 별로쉽게 출력하기위해
#출력하는 부분을 함수로 묶기
# 함수 2개
#get_api_result()\
#call_and_print()
#   get_api_result() 호출하여 json_obj 결과 받아서
#   출력


import requests
from urllib.parse import urlparse

def get_api_result(keyword,display,start):
    url = 'https://openapi.naver.com/v1/search/blog?query=' \
          + keyword + "&display="\
          +str(display)+ "&start="+str(start)\

    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    return result.json()
def call_and_print(keyword,display,start):
    json_obj = get_api_result(keyword, display, start)  # 함수호출시 변수  #keyword에 추출하고싶은 단어

    num = start - 1
    for items in json_obj["items"]:
        num += 1
        print(str(num) + ":" + items['title'].replace("<b>", "").replace("</b>", ""), items['link'])

keyword=   '강남역'
display = 100
start= 101

call_and_print(keyword,display,start)
