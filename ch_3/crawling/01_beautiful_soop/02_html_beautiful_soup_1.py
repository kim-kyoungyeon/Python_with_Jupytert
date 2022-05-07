# Beautiful soup을 사용해서
# html 문서에서 필요한 부분 추출하기

import bs4
html_str="<html><div>hello</div></html>"
#문자열을 파싱하고 bs 오브젝트 반환
bs_obj= bs4.BeautifulSoup(html_str,"html.parser")
print(type(bs_obj))
print(bs_obj)# html 태그로 추출
#<html><div>hello</div></html>

#파싱한 내용에서 <div>태그 추출
print(bs_obj.find("div"))
#<div>hello</div>
#<div> 태그에서 텍스트만 추출
print(bs_obj.find("div").text)
#hello









