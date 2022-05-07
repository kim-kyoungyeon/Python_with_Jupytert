#selenium 사용하기
# - webdriver api통한 웹브라우저슬ㄹ 제어하는 도구
# beautifulsoup과 함께 사용할수있어서 쉽게크롤링가능
#requests 를 통한 텍스트 추출의 경우 웹브라우저에서 소스보기를 한 것과 같이 동적인 페이지 추출
# 자바 스크립트를 통해 동적으로 변환된 문서 객체 요소(DOM)에 접근 불가
# selenium은 실제 웹 브라우저가 동작하기 때문에 자바 스크립트가 실행이 완료된 후에 동적으로 변환된 DOM에 접근가능
# 결론적으로 동적인 데이터를 추출하기 위해서는 selenium 과 같은 도구를 사용해야함

# selenium 패키지 설치
# 크롬 webdriver 다운로드 받아서
# c;\phythonstudy\driver 폴더 만들고 이안에 저장
# 주의 현재 사용중인 크롬의 버전과 일치하는 driver를 다운로드 받아야함
# 크롬버전 확인:  84.0.4147.89
# 윈도우 사용자는 chromedriver _win 32.zip 다운로드 받음

#자바스크립트로 생성된 동적 데이터 읽어오기
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# 크롬 드라이버를 통한 네이버 접속
driver = webdriver.Chrome("C:\PythonStudy\driver\chromedriver")# 상위파일 ..
driver.get("https://news.naver.com/")


#함수위치
def get_news_info(url):
    #링크페이지 불러오기
    result= requests.get(url)
    bs_obj=BeautifulSoup(result.content,"html.parser")

    #제목추출
    title= bs_obj.find(id="articleTitle")

    #기사입력 날짜와 시간추출
    date_time=bs_obj.find("span",{"class":"t11"})
    # 좋아요 수 추출 자바스크립트로동적으로 숫자출력
    driver.get(url)
    driver.page_source
    like_list= driver.find_elements_by_css_selector(
    "span.u_likeit_text._count.num")
    like_num = [like.text for like in like_list]
    # 댓글수 추출

    reply_list = driver.find_elements_by_css_selector(
      "#articleTitleCommentCount > span.lo_txt")
    reply_num=[reply.text for reply in reply_list]
    # 딕셔너리로 추출하기
    dict = {}
    dict["제목"] = title.text
    dict["기사 입력시간"] = date_time.text

    #좋아요 수와 댓글수가  없는경우가생김
    #예외처리
    try:
        dict["좋아요 수 "] = like_num[0]
        dict["댓글 수 "] = reply_num[0]
    except IndexError:
        dict["좋아요 수 "] = 0
        dict["댓글 수 "] = 0
    return dict



#뉴스 제목 링크 추출
url ="https://news.naver.com/"
headers={'User-Agent': 'Chrome/84.0.4147.89'}
result=requests.get(url,headers=headers)
bs_obj=BeautifulSoup(result.content,"html.parser")
#기사 제목이 포함된 ul 태그 추출
ul=bs_obj.find("ul",{'class':"hdline_article_list"})
lis=ul.findAll("li")

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

driver.close()
