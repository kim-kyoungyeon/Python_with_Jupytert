# 상수
# 값이 변경되지 않는 값
# 파이썬에서는 별도의 상수가 없음
# 변수와 구분하기 위해 대문자로 사용
# 나중에 상수의 값을 변경해도 오류가 없음
# 프로그램 내에서 변하지 않는 값을 쓸때는 상수로 처리하는 것이 편리

PI = 3.141592 # 대문자 이름이므로 상수로 처리
r = 10
area = r*r*PI
print(area)

INT_RATE = 0.03

deposit = 10000
interest = deposit * INT_RATE
balance = deposit + interest

print(balance) # 변수값 그대로 출력
print(int(balance)) # 변수값을 정수형으로 형 변환 후 출력
print(format(int(balance),',')) # 변수값을 정수형으로 형 변환 후 천단위 구분자 기호 사용해서 출력

