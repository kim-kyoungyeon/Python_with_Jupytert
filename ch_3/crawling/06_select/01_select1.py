# select()함수사용
#   필요한 부분을 css 선택자를 사용하여 추출
#   select_one() 1개의 태그 추출
#   select()여러개의 태그 추출
from bs4 import BeautifulSoup
html_str = """
<html>
    <body>
        <h1>select() 사용</h1>
        <div id="main">
            <h1>도서목록</h1>
            <div>
                <h1>프로그래밍</h1>
                <ul class="items">
                    <li>파이썬</li>
                    <li>HTML</li>
                    <li>CSS</li>
                </ul>
            <div>
            <div>
                <h1>인문학</h1>
                <ul class="items">
                    <li>사피엔스</li>
                    <li>역사의 역사</li>
                    <li>호모데우스</li>
                </ul>
            <div>
        </div>
    </body>
</html>
"""
#bs_obj = soup
soup = BeautifulSoup(html_str,"html.parser")

#id가 main 인 div 태그에 자식 태그 h1선택
h1 = soup.select_one("div#main>h1").text
print("h1: ",h1)

#동일한 표현
h1_2 = soup.select_one("#main > h1")
print("h1:",h1_2.text)
#아이디가 메인인 div 태그의 모든 자손 h1 선택
h1s= soup.select("div#main h1") # 자손은 그냥 띄어쓰기
print("모든 h1 : ")
print(h1s) # 리스트반환

#findAll() select () 함수는 리스트로 반환된다.
#결과값이 1개 라도 리스트로 반환
# 반복문을 사용해서 요소를 추출해야한다
#반복문 사용해서 리스트의 각 요소 출력
for h in h1s :
    print(h.text)

#클래스가 items인 태그의 모든 자손 li 선택 (.클래스)6개추출
lis = soup.select(".items li")
print(lis)#리스트반환
#반복을 이용해 모든 요소 출력
for li in lis:
    print(li.text)











