#2개의 함수로 묶기
#함수 1 :상품 정보 추출하는 함수: get_product_info() 동일
# 함수 2 url 페이지에 접소해서 상품정보를 추출하는함수
# get_page_products()
# - url 접속해서 페이지 내용 읽어오기
#   1페이지에 전체상품 추출해서  boxes
# get_product_info() 함수를 호출하여 상품 1개씩 박스를 전달하고
#   반환된 값인 딕셔너리를 리스트로 만들어 전달 return

import requests
from bs4 import BeautifulSoup

def get_product_info(box):
#상품명추출
    p_tag = box.find("p", {"class": "name"})
# <p>안에 들어있는 <span>추출
    name = p_tag.find("span").text #span 은 태크
#가격추출
    ul=box.find("ul")
    span_price=ul.findAll("span")
    price = span_price[1].text

#세일가격 추출
    span_price=ul.findAll("span")
    try:
        # 오류가 발생할 것 같은 문장
        sale_price = span_price[4].text
    except IndexError:
        # 예외처리 구문
        sale_price = 'no sale price'
    #링크추출
        a_tag=box.find("a")
        link=a_tag['href']
    return {"name":name,"price":price,"sale price":sale_price,"link":link}


#메인 실행 부분
# 기본 url을 만들고 각 페이지 url을 get_page_product 함수에게 전달
# 반환되는 list출력  - 상품정보최종출력
def get_page_products(url):
    headers = {'User-Agent': 'Chrome/84.0.4147.89'}
    result = requests.get(url, headers=headers)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    ul = bs_obj.find("ul", {"class": "prdList grid4"})
    boxes = ul.findAll("div", {"class": "box"})
# 1개의 상품이 들어있는 div 클래스 박스 모두추출

#g3et _prodcut info() 로 box 전달후 반환되는 상품정보리스트 생성
    product_info_list = [get_product_info(box)for box in boxes]
#동일표현
# product_info_list=[]
# for box in boxes:
#     product_info_list.append(get_product_info(box))

    return product_info_list #상품 정보 리스트반환
#5개 페이지 url
# http://jolse.com/category/toners-mists/1019/?page=1
# http://jolse.com/category/toners-mists/1019/?page=2
# http://jolse.com/category/toners-mists/1019/?page=3
# http://jolse.com/category/toners-mists/1019/?page=4
# http://jolse.com/category/toners-mists/1019/?page=5
#기본 url 설정후
url = "http://jolse.com/category/toners-mists/1019/?page="
#각페이지 url을 전달하고 결과 받아서 출력
for page_num in range (1,6) :
    urls = url + str(page_num)
    page_products = get_page_products(urls)
    print(page_products)
    print(len(page_products),page_products)


######################################################################################3
# 프로그램 전체구조
# def get_product_info() # 동일
#   상품정보를 추출
#   return 딕셔너리를 반환
# def get_page_products() :
#   url 접속
#   결과 = get_product_info():
#   return 리스트로 변환된 결과

#메인실행부분
#   기본 url 설정
#   모든 페이지 5개 페이지에 url 전달하고
# for 문 사용 :
#   결과 = get_page_products(페이지url)
#    결과 출력 :  for문 사용
























# span은 태그이다
# id 도 태그이다
# 태그시발