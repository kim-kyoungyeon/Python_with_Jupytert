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

    #num = start-1
    for items in json_obj["items"]:
     #   num += 1
        title= items['title'].replace("<b>", "").replace("</b>", "")
        print(title + "@"+items["bloggername"]+ "@"
                          + items['link'])

keyword=  '강남역'
display = 100
start= 1
# call_and_print함수를 5번 호출/ 반복문
for i in range(5):
    call_and_print(keyword,display,start)
    start+=100
#구분자 메모장에 확인후 @ 이 혹시 제목에 들어가있으면 다른 특수기호 사용할것.
#엑셀>데이터나누기 >구분기호로 구분됨으로