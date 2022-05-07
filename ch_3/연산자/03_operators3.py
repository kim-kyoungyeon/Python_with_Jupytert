#관계 연산자
result = 100 > 10 #대소비교 연산자   >, <, >=, <=
print(result)# T
x= 200
y= 200
result = y == x # 같은지 비교
print(result) # T
result  = x != y # 같지 않은지 비교
print(result)  # F
#논리연산자
# and 논리곱 (그리고) : 둘다 참인경우 참
# or 논리합 (또는) : 한쪽ㅁ나 참이여도 참
# not 부정 (아니다) : 참이면 거짓 거짓이면 참

a = 15
a >=10 and a<20 # TRUE
(a % 3 == 0) or (a%5 == 0) # 결과 T a가 3의 배수거나 5의 배수인지 확인
not(a==100) # True
































































































