#두명의 이름과 주사위 숫자를 입력받아
#숫자가 더 높은 사람이 이기는 프로그램
# 입력 :
# 이름을 입력하세요 : 홍길동
# 주사위 숫자를 입력하세요. : 6
# 이름을 입력하세요 : 김철수
# 주사위 숫자를 입력하세요. :  5

# hong<-input("이름을 입력하세요 ")
# hdic<-int(input("주사위 숫자를 입력하세요 "))
# kim<-input("이름을 입력하세요 ")
# kdic<-int(input("주사위 숫자를 입력하세요 "))
# print('출력 :')
# print('주사위 숫자 : '% (hdic,kdic))
# print('%s 님 승')

# 출력 :
# 주사위 숫자 6, 5
# 홍길동 님 승

# 승패 결과의 모든 경우를 계산할 것

########################정답######################################
#이기고 지고 비기고
# name1 = input('이름을 입력하세여...')
# num1 =int(input('주사위의 숫자를 입력하세요'))
# name2 = input('이름을 입력하세여...')
# num2 =int(input('주사위의 숫자를 입력하세요'))
# print('주사위 숫자 %d , $d'%(num1,num2))
# if num1 > num2 :
#     print('%s 님 승'% name1)
# elif num1 == num2 :
#     print('무승부')
# else :# num2  >num1
#     print("%s 님 승" % name2 )

#위프로그램을 주사위숫자는 컴퓨터가 난수를발생시켜 결정하도록 수정
#난수처리해서 모든경우 처리하기
from random import randint
n=randint(1,6)
if n == 1:
    com = 1
elif n == 2:
    com = 2
elif n == 3:
    com = 3
elif n == 4:
    com = 4
elif n == 5:
    com = 5
else:
    com = 6
you = int(input('you 입력 : '))
#'com'이 이기는 모든 경우의 수
if com == 2 and you == 1 or\
   com == 3 and you == 2 or you == 1 or\
   com == 4 and you == 3 or you == 2 or you == 1 or\
   com == 5  and you ==4 or you == 3 or you == 2 or you == 1 or \
   com == 6 and you==5 or you == 4 or you == 3 or you == 2 or you == 1 :
    print('컴퓨터가 이겼습니다')
else:
    print('당신이 이겼습니다.')


# from random import randint #필요 패키지 및 라이브러릴 등록
# name1 = input('이름을 입력하세여...')
# num1 = randint(1,6)
# name2 = input('이름을 입력하세여...')
# num2 = randint(1,6)
# print('주사위 숫자 : %s 님 %d , %s 님 %d'%(name1,num1,name2,num2))
# if num1 > num2 :
#     print('%s 님 승'% name1)
# elif num1 == num2 :
#     print('무승부')
# else :# num2  >num1
#     print("%s 님 승" % name2 )

















