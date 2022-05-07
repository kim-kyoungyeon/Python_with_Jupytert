#두명의 이름과 주사위 숫자를 입력받아
#숫자가 더 높은 사람이 이기는 프로그램
# 입력 :
# 이름을 입력하세요 : 홍길동
# 주사위 숫자를 입력하세요. : 6
# 이름을 입력하세요 : 김철수
# 주사위 숫자를 입력하세요. :  5
#
# 출력 :
# 주사위 숫자 6, 5
# 홍길동 님 승

# 승패 결과의 모든 경우를 계산할 것

from random import randint

# 내가 푼 것
name1 = input('이름을 입력하세요 : ')
dice1 = int(input('주사위 숫자를 입력하세요 : '))
name2 = input('이름을 입력하세요 : ')
dice2 = int(input('주사위 숫자를 입력하세요 : '))

print('주사위 숫자 %d' % dice1,',',dice2)
if dice1 > dice2 :
    print('%s 님 승'%name1)
elif dice1 < dice2 :
    print('%s 님 승'%name2)
else :
    print('%s 님 %s 님 무승부'%(name1,name2))

#===풀이===#
name1 = input('이름을 입력하세요. : ')
num1 = int(input('주사위의 숫자를 입력하세요. : '))
name2 = input('이름을 입력하세요. : ')
num2 = int(input('주사위의 숫자를 입력하세요. : '))

print('주사위 숫자 %d, %d'%(num1,num2))

if num1 > num2 :
    print('%s 님 승'%name1)
elif num1 == num2 :
    print('무승부')
else : # num2 > num1
    print('%s 님 승 '%name2)
