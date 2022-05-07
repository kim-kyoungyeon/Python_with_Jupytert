#검색어.출력수.시작숫자 입력받아서
# #결과출력
# 입력받는 함수 search_input()
import requests
from urllib.parse import urlparse
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

    num = start - 1
    for items in json_obj["items"]:
        num += 1
        print(str(num) + ":" + items['title'].replace("<b>", "").replace("</b>", ""), items['link'])

# 검색어 출력수 시작숫자입력받고
#결과출력하는 함수
def search_input():
    keyword=  input('검색어를 입력하세요:')
    display = int(input('출력 수를 입력하세요:'))
    start=int(input('시작 숫자를 입력하세요:'))

    call_and_print(keyword,display,start)

#함수 도출
search_input()