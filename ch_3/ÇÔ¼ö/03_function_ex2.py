# Q. 다음의 함수를 포함하는 프로그램 작성(매개변수가 없는 함수)
# 방법 1) 입력 기능 포함 함수
def sum() :
    num1 = int(input('숫자 1 입력 : '))
    num2 = int(input('숫자 2 입력 : '))
    print('합 : %d' % (num1+num2))

sum()

# 방법 2) 계산 기능 포함 함수
def sum(num1,num2):
    print('합 : %d' % (num1 + num2))

num1 = int(input('숫자 1 입력 : '))
num2 = int(input('숫자 2 입력 : '))
sum(num1,num2)