seconds = 1000
minutes = seconds // 60 # 몫
remainder = 1000 % 60 # 나머지

print('%d 분 %d 초' % (minutes,remainder))

#------------------------------------------
# 지수계산
# **연산자 사용
2**7 #128 : 2의 7승

# y = 3x2+7x+9
x = 3
y = 3*x**2 + 7*x + 9
print(y)

# 연습문제
# x=3이고, y=x**3+3x**2+7x+10일 때 y값은?
x = 3
y = x**3 + 3*x**2 + 7*x + 10
print(y)

#연산자 우선순위
#괄호-지수-곱셈/나눗셈/나머지-덧셈나눗셈-대입연산자(+=)

