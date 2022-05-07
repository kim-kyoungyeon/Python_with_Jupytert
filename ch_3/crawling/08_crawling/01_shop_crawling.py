import requests
from bs4 import BeautifulSoup
headers={'User-Agent': 'Chrome/84.0.4147.89'}
url="http://jolse.com/category/toners-mists/1019/"
result=requests.get(url,headers=headers)
# print(result) #<Response [403]>인 경우 헤더추가
bs_obj=BeautifulSoup(result.content,"html.parser")




#(1)상품명 출력
print("-----------------상품명 출력----------------")
#1 xxxx
#2 xxx
#48 xxxxx
#모든 상품명 출력
ul=bs_obj.find("ul",{"class":"prdList grid4"})
# print(ul)
boxes=ul.findAll("div",{"class":"box"})
# print(boxes)
def get_product_info(box):
    #상품명 추출
    #한개의 상품이 들어있는 <p class="name">추출
    headers = {'User-Agent': 'Chrome/84.0.4147.89'}
    result = requests.get(url, headers=headers)
    p_tag=box.find("p",{"class":"name"})
    #<p>안에 들어있는 <span>추출
    name=p_tag.find("span").text
    return name
#box개수만큼 함수를 호출
count=0
for box in boxes:
    count += 1
    product_info=get_product_info(box)
    print(count,product_info)

#(2)가격 출력
print("-----------------가격 출력----------------")
ul=bs_obj.find("ul",{"class":"prdList grid4"})
boxes=ul.findAll("div",{"class":"box"})
#가격/세일가격 : 총 5개의 <span>
#가격 : 2번째 <span>

count=0
for box in boxes:
    count += 1
    ul=box.find("ul")
    span_price=ul.findAll("span")
    #가격은 두번째 <span> :[1]
    price=span_price[1].text
    print(count,price)
#
##세일가격 : 5번쨰 <span>
#주의 : 세일 가격이 없는 상품 존재
#즉 인덱스로 접근할 떄 인덱스 에러 존재
#--->예외처리 : 세일 가격이 없는 경우 :no sale price 출력
# #(3)세일가격 출력
print("-----------------세일가격 출력----------------")
count=0
for box in boxes:
    count+=1
    ul=box.find("ul")
    span_price=ul.findAll("span")
    #예외 처리 구문
    try:
        #오류가 발생할 것 같은 문장
        sale_price=span_price[4].text
    except IndexError :
        #예외처리 구문
        sale_price ='no sale price'
    print(count,sale_price)
#
# #(4)링크 출력
print("-----------------링크 출력----------------")

count=0
for box in boxes:
    count += 1
    #링크 <a> 태그 추출
    a_tag=box.find("a")
    link=a_tag['href']
    print(count,link)