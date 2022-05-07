# 네이;버 검색 api 예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog
import os
import sys
import urllib.request
client_id = "1abbThtI_N36a83dT9fc"
client_secret = "fvK2Z7QkHF "

encText = urllib.parse.quote("강남역")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과

# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)