import requests
from bs4 import BeautifulSoup
##
import requests
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Chrome/84.0.4147.89'}
url="http://jolse.com/category/toners-mists/1019/"
result=requests.get(url,headers=headers)
# print(result) #<Response [403]>인 경우 헤더추가

bs_obj=BeautifulSoup(result.content,"html.parser")

for box in boxes:
    p_tag =box.find("p",{"class":"name"})
    print(p_tag)

# <p>태그 안에 들어있는 <span>상품명/</span>추출
#for box in boxes:
p_tag = box.find("p",{"class":"name"})
#<p>안의 <span>추출
span= p_tag.find("span")
print(span.text) # 상품명 추출완료
# 함수로 묶기
#함수를 이용해 프로글매 구조 변경
# 현재 페이지뿐아니라 다른 모든 페이지에도 반복적용할수있또록 함수작성
#프로그램 구조 변경 : 리펙토링 refactoring
#get_ product_info(box) 함수


import bs4

#(1)상품명출력
print("------------------------------상품명 출력")
# 모든 상품명 출력
count = 0
for box in boxes :
    count += 1
    p_tag = box.find("p",{"clas":"name"})
    name = p_tag.find("span")
    print(count,name)
# 1 xxx
# 2 xxx
#48개 xxxx

#(2)가격 출력
print("------------------------------가격 출력")
# 가격/세일 가격 : 총 5개의 <span>
# 가격: 2번째 span
# 세일 가격은 5번째 <span>
# 주의 세일 가격 이 없는 상품존재
# 즉 인덱스로 접근시 index 에러 발생
# > 예외 처리 :
#           세일가격 없는 경우: no sale price 출력
count =0
for box in boxes :
    count += 1
    ul = box. find("ul")
    span_price = ul.findAll("span")
# 가겨은 두번째 <span> : [1]
price = span_price[1].text
print(count, price)
#(3)세일 가격 출력
# 세일 가격은 5번째 <span>
# 주의 세일 가격 이 없는 상품존재
# 즉 인덱스로 접근시 index 에러 발생
# > 예외 처리 :
#           세일가격 없는 경우: no sale price 출력
print("------------------------------세일 가격 출력")
count = 0
for box in boxes :
    count +=1
    ul = box.find("ul")
    span_price = ul.findAll("span")

    # 예외처리 구문
    try :
        # 오류가 발생 할 것 같은 문장
        sale_price = span_price[4].text
    except IndexError:
        #예외처리 구문
        sale_price = "no sale price"

    sale_price = span_price[4].text
    print(count,sale_price)

#(4)링크출력
print("------------------------------링크 출력")
count = 0
for box in boxes :
    count += 1
    #링크 <a>태그추출
    a_tag = box.find("a")
    link = a_tag["href"]
    print(count,link)














