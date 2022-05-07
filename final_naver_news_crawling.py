#news 기자 keyword,dispaly start 지정
#해서 추출
# 과정: 기사 크롤링> 기사텍스트 >키워드 갯수세기 >키워드별 카운트>워드클라우드

import requests
from urllib.parse import urlparse
text=[]
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
f = open("naver_news.txt", 'w', encoding='utf-8')
def call_and_print(keyword,display,start):
    json_obj = get_api_result(keyword, display, start)  # 함수호출시 변수  #keyword에 추출하고싶은 단어

    num = start-1
    for items in json_obj["items"]:
        num += 1
        title= items['title'].replace("<b>", "").replace("</b>", "")
        print(str(num) + ":" + items['title'].replace("<b>", "").replace("</b>", ""),
                         items['description'].replace("<b>", "").replace("</b>", ""),items['originallink'])
        f.write(title + '\n')
keyword=  '밀키트'
display = 100
start= 1
# call_and_print함수를 5번 호출/ 반복문
for i in range(5):
    call_and_print(keyword,display,start)
    start+=100

