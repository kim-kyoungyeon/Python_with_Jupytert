# 문자열의 접근 방법 : 인덱싱과 슬라이싱을 이용해서 접근

# 문자열 인덱싱(indexing)
# 인덱스로 문자의 위치를 나타내는 것
# 인덱스(첨자) : 문자의 위치, 0부터 시작

# string[0] #첫 번째 문자
# string[-1] #마지막 문자

# 문자열 슬라이싱
# 문자열 중에서 일부분을 추출하는 것(잘라내는 것)
# 인덱스의 일종
# string[n] : 인덱스 n번째 문자
# string[0:n] : 0부터 n-1번째까지의 문자열
# string[n:] : n부터 끝까지의 문자열
# string[:n] : 0부터 n-1까지의 문자열
# string[-1:] : 마지막 문자(마지막 문자에서 끝까지)
# string[:-1] : 처음부터 마지막 -1까지
# string[:] : 전체 문자열

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'
print(crawling) # Data crawling is fun
print(crawling[0:3]) # 0~3 : Data
print(crawling[5:16]) # 5~15 : crawling is
print(crawling[17:]) # 17~끝 : fun
print(crawling[19]) # 19번째 문자 : n
print(crawling[-1]) # 마지막 문자 : n
print(crawling[:-1]) # 처음~마지막-1 : Data crawling is fu
print(crawling[16:16+4]) # 16~19 : fun
print('---------------------------------------')
print(parsing) # Data parsing is also fun
print(parsing[5:]) # 5~끝 : parsing is also fun
print(parsing[:15]) # 처음~14 : Data parsing is
print(parsing[:]) # 전체 : Data parsing is also fun

# 주의 !
# 1) 인덱스 위치 번호는 0부터 시작
# 2) 문자열은 인덱싱 슬라이싱으로 부분 접근은 가능하지만 부분 수정은 불가능하다.