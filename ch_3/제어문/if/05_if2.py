#정수를입력받아 양수 0 음수로 구별하는 프로그램을 ㅈ가성하시오
num = int(input('정수입력: '))
if num < 0 :
    print('음수')
elif num ==0 :
    print('0')
else :
    print('양수')