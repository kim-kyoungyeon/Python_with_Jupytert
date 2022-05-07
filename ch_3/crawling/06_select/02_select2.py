# html 팡리 읽어와서 select() 함수 사용해서 추출


from bs4 import BeautifulSoup

#html 파일 읽어오기
fp= open("food-list.html",encoding="utf-8")
bs_obj=BeautifulSoup(fp,"html.parser")
#print(bs_obj)

#select_one(): 1개의 태그 추출
#두번째 <li>추출
print("1. ", bs_obj.select_one("li:nth-of-type(2)").string)
print("1. ",bs_obj.select_one("li:nth-child(2)").string)

#id 가 fd-list인 태그의 4번째 자식 태그선택
print("2.", bs_obj.select_one("#fd-list > li:nth-of-type(4)").string)
#정식
print("2. ",bs_obj.select_one("li:nth-of-type(4)").string)
print("2. ",bs_obj.select_one("li:nth-child(4)").string)

print("---------------------------")
#select()함수로 여러개의 태그 추출

print("3. ",bs_obj.select("li:nth-of-type(4)"))
print("4.",bs_obj.select("li:nth-of-type(4)")[0].text)
print("4.",bs_obj.select("li:nth-of-type(4)")[1].text)
#삼겹살 추출하기
print("5.",bs_obj.select("li:nth-of-type(3)")[0].text)
print("5. ", bs_obj.select_one("li:nth-of-type(3)").string)
#막걸리
#id가 ac-list의 자식 li에서 data-lo가='ko'인 태그추출
print("5.",bs_obj.select("#ac-list>li[data-lo='ko']")[1].string)
#삼겹살
#id가 fd-list의 자식 li 중 클래스가 food hot 인 태그추출
print("6 ",bs_obj.select("#fd_list>li.food.hot")[1])
#막걸리& 삼겹살
print("6.",bs_obj.select("li:nth-of-type(3)").string) # 이거왜안됨?

































