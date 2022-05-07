#네이버 검색 open api 예제 : 블로그 검색
# requests 패키지를 사용해서 코드를 좀 더 간단하게 변경

import requests
from urllib.parse import urlparse
keyword='강남역'
url = 'https://openapi.naver.com/v1/search/blog?query='+keyword
result= requests.get(urlparse(url).geturl(),
                     headers={"X-Naver-Client-Id": "1abbThtI_N36a83dT9fc",
                              "X-Naver-Client-Secret":'fvK2Z7QkHF'})
print(result)
#<Response [200]>
print(result.json())# 보기 어려움

# 결과가 보기 어려움으로 쉽게 이해할수있는 구조 이용
#온라인 제이슨 뷰어 online json viewer 이용
#   json 구조를 트리구조로 표시 한눈에 이해할수있음
# 네이버 api 결과 기본값은 10개
# 강남역 블로그 검색겨로가 json구조

# 5개의 key (items도 6개의 키)
# -lastBuildDate :
# -total :
# -start :
# -display :
# -items
#     title :
#     link :
#     description :
#     bloggername :
#     bloggerlink :
#     postdate :
#



























