#네이버 뉴스 에서 함수로 작성하여
#5개 sub 페이지에 제목 기사 입력 날짜 및 시간 추출

#get_news_info()
    #url 전달받아서
    # 뉴스제목추출


#시간은??
# 머리기사 뽑기

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
#         link = a_tag['href'] #텍스트안 파라미터값필요시
# #한개의 기사
# def get_news_info(url):
    #url접속해서
    # 구문분석 bs_obj beatifulsoup 만들기
    #제목추출 _ id추출 가능 (위의 소속 div)
    #날짜 시간 추출
    #딕셔너리로 만들어 반환

#메인 실행 부분
# 기본 url : "https://news.naver.com/main/main.nhn?mode=LSD&mid=shm&sid1=101"
# 기사 제목의 url 추출 : a 태그에서 추출 href
# 실제 전달될 url : 기본 url + href

#반복 : 기사 제목 개수만큼(li 의 개수만큼 4개)
# for:
#   함수호출하면서 url 전달
#   반환되는 결과 출력
# for : url + href 리스트[]
# for box in boxes:
    #기사 입력날짜 및 시간
    # 딕셔너리 만들어서 반환
#접속
#뉴스 제목 링크 추출
#함수 호출하면서 링크 전달하고  서브 페이지 제목 기사 입력 날짜 및 시간 받아서 출력
# 함수 위치

#대상 사이트 첫 페이지
import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Chrome/84.0.4147.89'}
url ="https://news.naver.com/"
result=requests.get(url,headers=headers)
bs_obj=BeautifulSoup(result.content,"html.parser")



    #딕셔너리만들기
dict = {}
dict["제목"] = title.text
dict["기사 입력시간"] =  daytime.text
return dict

#기사 제목이 포함된 ul 태그 추출
ul=bs_obj.find("ul",{'class':"hdline_article_list"})
lis=ul.findAll("li")
# print(lis)

#뉴스 제목 링크 추출
hrefs=[]

for li in lis:
    hrefs.append("https://news.naver.com/"+ li.find('a')["href"]) # 첨가?
# print(hrefs)

# 함수 호출하면서 링크전달후
# 링크에 해당되는 서브 페이지의 기사 제목과 입력 날짜 및 시간 반환받아 출력
# 반복횟수는 기사 제목 개수만큼 반복
for i in range(len(lis)):
    dic_result = get_news_info(hrefs[i]) #url=hrefs
    print(dic_result)





# def 함수 > dictionary > for문통해서 반복적으로 분업> get_news_info > result값을 추출


























