#값이 변경되지 않는값
#값이 변경되지 않는 값
# #파이썬에서는 변도의 상수가 없음
# 변수와 구분하기위해 댐누자로사용
# 나중에 상수의 값을 변경해도 오류가 없음
# 프로그램 내에서 변하지 않는 값을 쓸때에는 상수로 처리하는 것이 편하다


# PI = 3.141592 #대문자로 상수처리
# r =10
# area= r *r *PI
# print(area)
INT_RATE = 0.03
deposit = 10000
interest = deposit * INT_RATE
balance: float =deposit + interest


print(balance) #q변수갑 그대로 출력
print(int(balance)) # 변수값을 정수형으로 형변환 후 출력
print(format(int(balance',')))
#변수값을 정수형으로 형 변환 한 후 천단위 구분자기호를 사용해서 출력
# format(int(balance,'.'))




