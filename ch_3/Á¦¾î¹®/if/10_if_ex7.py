# 랜덤 숫자 생성 모듈 등록
from random import randint

# com의 난수 매핑 : 1 : 가위, 2 : 바위, 3 : 보
n = randint(1,3)

if n == 1 :
    com = '가위'
elif n == 2 :
    com = '바위'
else :
    com = '보'

you = input('you 입력 : ')

# 'com'이 이기는 모든 경우의 수
if com == '가위' and you == '보' or  com == '바위' and you == '가위' or com == '보' and you == '바위' :
    print('컴퓨터가 이겼습니다.')
elif com == you :
    print('비겼습니다.')
else :
    print('당신이 이겼습니다.')
# 컴퓨터 데이터 출력
print('컴퓨터 %s 입니다.' % com)