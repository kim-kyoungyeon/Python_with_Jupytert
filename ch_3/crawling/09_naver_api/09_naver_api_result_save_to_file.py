#
import requests
from urllib.parse import urlparse
file= open('naver_api_result.txt','w',encoding='utf-8')# 쓰기모드= 저장모드
#입력부부분 함수로 도출 어떻게??
# search_input=?
def get_api_result(keyword,display,start):
    url = 'https://openapi.naver.com/v1/search/blog?query=' \
          + keyword + "&display="\
          +str(display)+ "&start="+str(start)

    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    return result.json()
def call_and_print(keyword,display,start):
    json_obj = get_api_result(keyword, display, start)  # 함수호출시 변수  #keyword에 추출하고싶은 단어

    num = start-1
    for item in json_obj["items"]:
        num += 1
        title= item['title'].replace("<b>", "").replace("</b>", "")
        #print(title + "@"+item["bloggername"]+ "@"+ item['link'])
        content=str(num)+title + "@"+item["bloggername"]+ "@"+ item['link']
        file.write(content+"\n")

keyword=  '강남역'
display = 100
start= 1
# call_and_print함수를 5번 호출/ 반복문
for i in range(5):
    call_and_print(keyword,display,start)
    start+=100