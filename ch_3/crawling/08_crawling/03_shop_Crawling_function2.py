#함수로 묶기

#1개의 상품에서 정보추출
#상품명 상품가격 세일가격 링크 4가지를 추출
# 4개를 추출해서 딕셔너리 반환

# def get_product_info(box):
# 상품명추출
#가격 추출
# 세일가격추출
# 링크 추출
# 상품명 가격 세일가격 링크 딕셔너리 반환

import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Chrome/84.0.4147.89'}
url="http://jolse.com/category/toners-mists/1019/"
result=requests.get(url,headers=headers)
# print(result) #<Response [403]>인 경우 헤더추가
bs_obj=BeautifulSoup(result.content,"html.parser")

ul=bs_obj.find("ul",{"class":"prdList grid4"})
boxes=ul.findAll("div",{"class":"box"})

#1개의 상품이 들어있는 divclass= "box 모두추출
print(len(boxes))
#박스안에 들어있는 1개의 상품에서 정보추출
#딕셔너리로 반환하는함수
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
    #링크추출#
    a_tag=box.find("a")
    link=a_tag['href']

    return {"name":name,"price":price,"sale price":sale_price,"link":link} #키: 변수


# get_product_info 함수 호출하며서 box 전달하고
# 상품정보 받아서 출력
count=0
for box in boxes:
    count += 1
    #함수 호출하고 결과받기
    product_info=get_product_info(box)
    print(count, product_info)
















