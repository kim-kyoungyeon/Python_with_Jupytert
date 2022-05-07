#검색수 제약없이 입력 받아서 결과 출력
import requests
from urllib.parse import urlparse
def get_api_result(ctg_jason,keyword,display,start):
    default_url = "https://openapi.naver.com/v1/search/"
    # default_url = "https://openapi.naver.com/v1/search/cafearticle.json?"

#ordre sim이나 date 순으로

    sort = 'sort= sim'
    display ="&display=" +str(display)
    query= '&query=' + keyword

    start = "&start=" + str(start)
    full_url = default_url+ ctg_jason+display+ sort +query + start

    result = requests.get(urlparse(full_url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})

    return result.json()
def print_result(ctg_jason,keyword,display,start):
    json_obj_result=get_api_result(ctg_jason,keyword,display,start)
    num = start-1
    for item in json_obj_result["items"]:
        num += 1
        # news = originallink
        #Blog&cafe = link
        if choice == '1':
            link = 'originallink'
        else :
            link = 'link'

        print(str(num) + ":" + item['title'].replace("<b>", "").replace("</b>", ""),
              item['description'].replace("<b>", "").replace("</b>", ""),
              item['link'])

#입력함수
def search_input():
    keyword = input('검색어를 입력:')
    input_num = int(input('검색 갯수를 입력:'))
    roop_num =input_num//100 # 반복횟수
    display = input_num%100
    start=1
    #100이상인 경우에는 display를 100으로 고정
    #반복횟수는 입력숫자를 100으로 나눈 몫
    # 320이면 3번 반복 (display=100)

    if input_num >=100 :
        for i in range(1,roop_num+1):
            print_result(ctg_json,keyword,100,start)
            start += 100
#입력숫자를 100으로 나눈 나머지를 display로 설정
    #320이면 100 3번은 if문에서 처리
    #나머지 20번은 display= 20으로 전달

    print_result(ctg_json, keyword, display, start)

    # json_obj_result= get_api_result(ctg_json,keyword,display,start)
    # print_result(json_obj_result)
#메인시작부분
choice =input("검색 분류를 입력하세요 : (1-뉴스, 2- 블로그, 3-카페)")
if choice == '1' :
    ctg_json ="news.json?"
elif choice =='2':
    ctg_json = "blog.json?"
else :
    ctg_json = "cafearticle.json?"

search_input() #시작함수