# 정수 3개를 입력 받아서 제일 큰 수 출력

num1 = int(input('정수 1 입력 : '))
num2 = int(input('정수 2 입력 : '))
num3 = int(input('정수 3 입력 : '))

if num1 > num2 and num1 > num3 : # num1이 가장 큰지
    maxNum = num1
elif num2 > num3 : # num1이 가장 큰수가 아닐 때 비교
    maxNum = num2
else :
    maxNum = num3 # num1과 num2가 가장 큰 수가 아닐 때 실행

print('제일 큰 수 : ', maxNum)