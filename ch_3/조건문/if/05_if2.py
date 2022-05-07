# 정수를 입력받아서 양수, 0, 음수로 구별하는 프로그램을 작성하시오.
num = int(input('정수 입력 : '))

if num < 0 :
    print('음수')
elif num == 0 :
    print('0')
else :
    print('양수')