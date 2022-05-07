# 관계 연산자
result = 100 > 10 #대소 비교 연산자 >, <, >=, <=
print(result) #True

x = 200
y = 200
result = y==x #같은지 비교
print(result) #True

result = x != y #같지 않은지 비교
print(result) #False

# 논리 연산자
# and : 논리곱(그리고) : 둘다 참인 경우 참
# or : 논리합(또는) : 한쪽만 참이어도 참
# not : 부정(아니다) : 참이면 거짓, 거짓이면 참

a = 15
a >= 10 and a < 20 #True
(a % 3 == 0) or (a % 5 == 0) #True(a가 3의 배수거나 5의 배수인지 확인)
not(a==100) #True