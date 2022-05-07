import requests
from urllib.parse import urlparse
keyword='강남역'
url = 'https://openapi.naver.com/v1/search/blog?query='+keyword
result= requests.get(urlparse(url).geturl(),
                     headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                              "X-Naver-Client-Secret":'fvK2Z7QkHF'})
# print(result)
# #<Response [200]>
# print(result.json())# 보기 어려움

json_obj = result.json()
#items 를 제외한 4개 key의 value를 추출
print(json_obj['lastBuildDate'])
print(json_obj['total'])
print(json_obj['start'])
print(json_obj['display'])

#items 내용 출력
#아이템마다 줄바꿔서 출력
print("---------------------------")
# for item in json_obj["items"]:
#     print(item)
# print(json_obj['items'])
# items 안에서 title 추출
# for items in json_obj["items"]:
#     print(items['title'])
#감동했던 <b>강남역</b> 고기집 <b></b>태그 포함되어있음

#<b></b> 태그 제거 후 출력
for items in json_obj["items"]:
    print(items['title'].replace("<b>","").replace("</b>",""))
    # replace 함수 자습하기
# 제목+bloggerlink 로 추출해보기

for items in json_obj["items"]:
    print(items['title'].replace("<b>","").replace("</b>",""),items['link'])

























