# Beautiful soup 을 사용하여
# html 문서에서 필요한 부분 추출하기
import bs4
html_str = """ 
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>            
"""

# 문자열을 파싱하고 bs 오브젝트 반환 (객체)
bs_obj = bs4.BeautifulSoup(html_str,"html.parser")

# <ul> 태그 추출
ul = bs_obj.find('ul')
print(ul)

print('----------------------------------------------------------------')
#모든 <li>태그 추출
lis= ul.findAll('li')
print(lis) # 리스트로 반환

#lis 리스트에서 hello, bye, welcome 추출하기
for li in lis:
    print(li.text)
# 요소의 개수 : 3
print(len(lis))

#











