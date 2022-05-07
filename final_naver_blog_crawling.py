import requests as rq
import bs4
from bs4 import BeautifulSoup

# def get_page_products(url):
#     headers = {'User-Agent': 'Chrome/84.0.4147.89'}
#     result = requests.get(url, headers=headers)
#     bs_obj = BeautifulSoup(result.content, "html.parser")
#     ul = bs_obj.find("ul", {"class": "prdList grid4"})
#     boxes = ul.findAll("div", {"class": "box"})
#     span class= t11
#
#     for box in boxes:
#         ul = box.find("ul")
#         tag =
#         a_tag = box.find("a")
#         link = a_tag['href']
#
# headers={'User-Agent': 'Chrome/84.0.4147.89'}
# url ="https://news.naver.com/"
# result=requests.get(url,headers=headers)
# bs_obj=BeautifulSoup(result.content,"html.parser")
# #딕셔너리만들기
# dict = {}
# dict["제목"] = title.text
# dict["기사 입력시간"] =  daytime.text
# return dict
# #기사 제목이 포함된 ul 태그 추출
# ul=bs_obj.find("ul",{'class':"hdline_article_list"})
# lis=ul.findAll("li")
# # print(lis)
#
# #뉴스 제목 링크 추출
# hrefs=[]
#
# for li in lis:
#     hrefs.append("https://news.naver.com/"+ li.find('a')["href"]) # 첨가?
# # print(hrefs)
#
# # 함수 호출하면서 링크전달후
# # 링크에 해당되는 서브 페이지의 기사 제목과 입력 날짜 및 시간 반환받아 출력
# # 반복횟수는 기사 제목 개수만큼 반복
# for i in range(len(lis)):
#     dic_result = get_news_info(hrefs[i]) #url=hrefs
#     print(dic_result)
#

import requests
from urllib.parse import urlparse

def get_api_result(keyword,display,start):
    url = 'https://openapi.naver.com/v1/search/blog?query=' \
          + keyword + "&display="\
          +str(display)+ "&start="+str(start)\

    result = requests.get(urlparse(url).geturl(),
                          headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                                   "X-Naver-Client-Secret": 'fvK2Z7QkHF'})
    content = result.text
    # result값을 txt값으로 저장

    return result.json()
def call_and_print(keyword,display,start):
    json_obj = get_api_result(keyword, display, start)  # 함수호출시 변수  #keyword에 추출하고싶은 단어

    #num = start-1
    f = open("naver_blog.txt", 'w', encoding='utf-8')
    for items in json_obj["items"]:
     #   num += 1
        title= items['title'].replace("<b>", "").replace("</b>", "")
        print(title + '\n' )
        f.write(title + '\n')


keyword=  '밀키트'
display = 100
start= 1
# call_and_print함수를 5번 호출/ 반복문

for i in range(5):
    call_and_print(keyword,display,start)
    start+=100

#구분자 메모장에 확인후 @ 이 혹시 제목에 들어가있으면 다른 특수기호 사용할것.

