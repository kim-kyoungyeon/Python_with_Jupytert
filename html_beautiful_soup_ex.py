# html 문자열에서 원하는 텍스트 추출
import bs4

html_str = """
<html>
   <body>
    	<div id="wrap">
        	<div id="mainMenuBox">                	
                <ul>  
                    <li><a href="#">패션잡화</a></li>    
                    <li><a href="#">주방용품</a></li>                     	          
                    <li><a href="#">생활건강</a></li>
                    <li><a href="#">DIY가구</a></li>
                </ul>
            </div>
        	<div>
            	<table>
                	<tr><td><img src="shoes1.jpg"></td>
                    	  <td><img src="shoes2.jpg"></td>
                    	  <td><img src="shoes3.jpg"></td></tr>
                    <tr id="prdName"><td>솔로이스트<br>걸리쉬 리본단화</td>
                    	  <td>맥컬린<br>그레이가보시스트랩 펌프스</td>
                          <td>맥컬린<br>섹슈얼인사이드펌프스</td></tr>
                    <tr id="price"><td>100,000원</td><td>200,000원</td><td>120,000원</td></tr>
                </table>
            </div>
            <div>
            	<div class="box">
                	<h4>공지사항</h4>
                    <hr>
                    <a href="#">[배송] : 무표배송 변경 안내 20.06.20</a><br>
                    <a href="#">[전시] : DIY 가구 전시 안내 20.07.12</a><br>
                    <a href="#">[판매] : 11월 특가 상품 안내 20.07.27</a>                               
                </div>
                <div class="box">
                	<h4>커뮤니티</h4>
                    <hr>
                    <a href="#">[레시피] : 살 안찌는 야식 만들기</a><br>
                    <a href="#">[가구] : 헌집 새집 베스트 가구</a><br>
                    <a href="#">[후기] : 배송이 잘못 됐어요 ㅠㅠ</a><br>
                 </div>
            </div>            
        </div>
    </body>
</html>"""

# 문자열 파싱하고 bs4 오브젝트 반환 (BeautifulSoup 객체)
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

print("----------------메뉴 추출-------------------")
# <ul> 태그 추출
ul = bs_obj.find("ul")
# find(ul)

# 모든 <li> 태그 추출
lis = ul.findAll("li")

# 모든 <li> 태그의 텍스트 추출
for li in lis :
    print(li.text)

## 내가 푼 것
# menu = bs_obj.find('div').find('div').find('ul')
# print(menu.text)

print("---------------상품명 추출----------------")
# 모든 <tr> 태그 추출
all_tr = bs_obj.findAll("tr")
# print(all_tr)

# 상품명은 두 번째 <tr>에 들어 있으므로
# all_tr[1]에서 찾음 : 인덱스는 0부터 시작
tr2_all_td = all_tr[1].findAll("td")
# print(tr2_all_td)

for td in tr2_all_td :
    print(td.text)

## 내가 푼 것
# product = bs_obj.find('div').findAll('tr',{"id":"prdName"})
# for products in product :
#     print(products.text)

print("---------------가격 추출----------------")
# 모든 <tr> 태그 추출
all_tr = bs_obj.findAll("tr")
# print(all_tr)

# 가격은 세 번째 <tr>에 들어 있으므로
# all_tr[2]에서 찾음
tr3_all_td = all_tr[2].findAll("td")
# print(tr3_all_td)

# <td> 태그의 텍스트 출력
for td in tr3_all_td :
    print(td.text)

## 내가 푼 것
# price = bs_obj.find('div').findAll('tr',{"id":"price"})
# for prices in price :
#     print(prices.text)

print("--------------공지사항 제목 추출--------------")
# class가 box인 <div> 추출하면 되는데 2개가 존재
# 공지사항은 첫 번째 <div>
# 첫 번째 추출할 수 있는 find() 함수 사용
box = bs_obj.find("div",{"class","box"})
# print(box)

# <box> 태그에서 <a> 태그 추출
all_a = box.findAll("a")
# print(all_a)

# <a> 태그의 텍스트 추출
for a in all_a :
    print(a.text)

## 내가 푼 것
# notice_title = bs_obj.find('div',{"class":"box"}).findAll('a')
# for notice in notice_title :
#     print(notice.text)

print("--------------커뮤니티 제목 추출--------------")
# 커뮤니티는 class가 box인 두 번째 <div>에 들어있으므로
# 모든 <div> 추출해서 두 번째[1] <div>에서 추출
boxes = bs_obj.findAll("div",{"class":"box"})
# print(boxes)

all_a = boxes[1].findAll("a")
# print(all_a)

# <a> 태그의 텍스트 추출
for a in all_a :
    print(a.text)

## 내가 푼 것
# community_title = bs_obj.findAll('div',{"class":"box"}).find('a')
# for community in community_title :
#     print(community.text)

print("----------상품명:가격 딕셔너리 만들기----------")
# 1. 상품명 리스트 추출
# 2. 가격 리스트 추출
# 3. 두 개의 리스트로 딕셔너리 생성

# 상품명 리스트 추출
# 빈 리스트 생성
prd_name = []
for td in tr2_all_td :
    prd_name.append(td.text)
# print(prd_name)

# 가격 리스트 추출
# 빈 리스트 생성
prd_price = []
for td in tr3_all_td :
    prd_price.append(td.text)
# print(prd_price)

# 상품명 리스트, 가격 리스트 생성 완료

# 두 개의 리스트로 딕셔너리 생성
product_dict = dict(zip(prd_name,prd_price))
print(product_dict)

for item in product_dict.items() :
    print(item)