# 문자열 : String으로 문자의 나열을 의미
# 생성 : 작은 따옴표나 큰 따옴표 사용해서 생성

crawling = 'Data crawling is fun'
parsing = 'Data parsing is also fun'

print(crawling)
print(parsing)

print(type(crawling))
# <class 'str'> : class 타입이므로 관련 함수 및 연산자가 있음
print(type(parsing))
# <class 'str'>

# 문자열 연결 : + 연산자 사용 --- 다른 데이터타입과 같이 사용 불가, str() 이용해서 형 변환 후 연결
print('홍길동'+'은 '+'서울 '+ str(135) +'번지에 삽니다.')

# 문자열의 곱하기 연산자 사용 가능
# 곱하는 수만큼 반복해서 문자열 생성
string = '파이썬'
result = string * 3
print(result)
# 문자열 + 연산자는 -> 연결해서 붙이기
# 문자열 * 연산자는 -> 하나의 문자열을 반복해서 붙이기





