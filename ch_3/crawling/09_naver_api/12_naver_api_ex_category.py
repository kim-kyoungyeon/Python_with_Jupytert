import requests
from urllib.parse import urlparse
def get_api_result(ctg_jason,keyword,display):
    default_url = "https://openapi.naver.com/v1/search/"
    # default_url = "https://openapi.naver.com/v1/search/cafearticle.json?"

#ordre sim이나 date 순으로

    sort = 'sort=sim'
    display ="&display=" +str(display)
    query= '&query=' + keyword

    full_url = default_url+ctg_jason+sort+ display +query

    result = requests.get(urlparse(full_url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    return result.json()
def print_result(json_obj_result):
    num = 0
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


# 함수 입력 api 검색 결과를 텍스 파일로 저장
def save_to_file(json_obj_result):
    file = open('naver_category_search.txt', 'w', encoding='utf-8')
    for item in json_obj_result['items']:
        file.write('-------------------------------------------------\n')
        file.write('제목 : ' + item['title'].replace("<b>", "").replace("</b>", "")
                   + '\n')
        file.write('요약내용: ' + item['description'].replace("<b>", "").replace("</b>", ""))

        if choice == '1':
            file.write('링크:' + item['originallink'].strip() +
                       '\n')
        else:
            file.write('링크:' + item['link'].strip() + '\n')

        file.write('\n')
    file.close()


#입력함수
def search_input():
    keyword = input('검색어를 입력:')
    display = input('검색 갯수를 입력(최대100개):')
    json_obj_result= get_api_result(ctg_json,keyword,display)
    print_result(json_obj_result)
    save_to_file(json_obj_result)
#메인시작부분
choice =input("검색 분류를 입력하세요 : (1-뉴스, 2- 블로그, 3-카페)")
if choice == '1' :
    ctg_json ="news.json?"
elif choice =='2':
    ctg_json = "blog.json?"
else :
    ctg_json = "cafearticle.json?"

search_input() #시작함수

