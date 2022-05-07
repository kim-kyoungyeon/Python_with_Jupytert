#news 기자 keyword,dispaly start 지정
#해서 추출
file= open('naver_api_result.txt','w',encoding='utf-8')# 쓰기모드= 저장모드

import requests
from urllib.parse import urlparse
def get_api_result(keyword,display,start):
    default_url = "https://openapi.naver.com/v1/search/news.json?"
    # default_url = "https://openapi.naver.com/v1/search/cafearticle.json?"

#ordre sim이나 date 순으로
    display ="&display=" +str(display)
    start= str(display)+ "&start="+str(start)
    query= '&query=' + keyword

    full_url = default_url+ display + start+query

    result = requests.get(urlparse(full_url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    return result.json()

def call_and_print(keyword,display,start):
    json_obj = get_api_result(keyword, display, start)  # 함수호출시 변수  #keyword에 추출하고싶은 단어
    print(json_obj)
    num = start - 1
    for items in json_obj["items"]:
        num += 1
        print(str(num) + ":" + items['title'].replace("<b>", "").replace("</b>", ""),
              items['description'].replace("<b>", "").replace("</b>", ""),items['originallink'])

# 검색어 출력수 시작숫자입력받고
#결과출력하는 함수
def search_input():
    keyword=  input('검색어를 입력하세요:')
    display = int(input('출력 수를 입력하세요:'))
    start=int(input('시작 숫자를 입력하세요:'))

    call_and_print(keyword,display,start)

#함수 도출
search_input()































































































