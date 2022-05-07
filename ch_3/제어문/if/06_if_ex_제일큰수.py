#정수 3개를 입력받아 제일 큰수 출력
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))


if num1 > num2 and num1 > num3 : # num 1이 가장 큰가요?
    maxNum = num1
elif num2 > num3 : # num1 이 가장 큰수가 아닐때 비교
    maxNum = num2
else :
    maxNum = num3 # num1 과 2 가 가장 큰 수가 아닐때 실험
print('제일큰수 : ', maxNum)

