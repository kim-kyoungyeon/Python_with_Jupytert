# index() 함수
# 문자열 내에서 특정 문자열의 시작 위치를 반환
# 없으면 Error

crawling = 'Data crawling is fun'
print(crawling.index('fun')) # 17
print(crawling.index('f')) # 17
print(crawling.index('parsing')) # ValueError: substring not found