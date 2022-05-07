# 태그의 class 속성ㅇ르 이용하기
# - find 함수에서 class 속성을 이용하면
# 첫번째 이외의 태그 추출이 가능하다
# <ul class ='reply">
# ul = bs_obj.find("ul",{"class":"reply"})
import bs4

html_str ="""
<html>
    <body>
        <ul class ="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class ="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>         
"""
bs_obj=bs4.BeautifulSoup(html_str,"html.parser")
ul=bs_obj.find("ul",{'class':'reply'})
print(ul)

#모든 <li> 태그 추출 후
lis=ul.findAll('li')#리스트반한
print(lis)
# ok no sure 추출
for li in lis:
    print(li.text)



