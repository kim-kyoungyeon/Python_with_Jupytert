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
name1 = input('이름을 입력하세여...')
num1 =int(input('주사위의 숫자를 입력하세요'))
name2 = input('이름을 입력하세여...')
num2 =int(input('주사위의 숫자를 입력하세요'))
print('주사위 숫자 %d , $d'%(num1,num2))
if num1 > num2 :
    print('%s 님 승'% name1)
elif num1 == num2 :
    print('무승부')
else :# num2  >num1
    print("%s 님 승" % name2 )










