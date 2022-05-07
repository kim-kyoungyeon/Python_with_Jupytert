### 주사위 프로그램을 주사위 숫자는 컴퓨터가 난수를 발생시켜 결정하도록 수정하시오.
from random import randint #필요 패키지 및 라이브러리 등록

name1 = input('이름을 입력하세요. : ')
comnum1 = randint(1,6)
name2 = input('이름을 입력하세요. : ')
comnum2 = randint(1,6)

print('주사위 숫자 : %s님 %d, %s님 %d'%(name1, comnum1,name2, comnum2))

if comnum1 > comnum2 :
    print('%s 님 승' % name1)
elif comnum1 == comnum2 :
    print('무승부')
else :
    print('%s 님 승 ' % name2)
