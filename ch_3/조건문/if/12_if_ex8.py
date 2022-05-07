# 다음과 같이 프로그램 작성
# num = int(input('번호 입력 (1. 현금 2. 카드) : '))
# if num == 1 or num == 2 :
#     if num == 1 :
#         money = int(input('지불액 입력 : '))
#         rate = int(input('할인율 '))
#         discount = money*rate
#         print('할인액 : %d원' % discount)
#     else :
#         money = int(input('지불액 입력 : '))
#         rate = int(input('할인율 '))
#         discount = money * rate
#         print('할인액 : %d원' % discount)
# else :
#     print('잘못 입력하였습니다. 종료합니다.')

#================== 풀이 ===================
# 사용자 입력 구문
num = int(input('번호 입력(1.현금 2.카드) : '))

# 1이나 2가 입력 되었는지 확인
if num == 1 or num == 2 :
    pay = int(input('지불액 입력 : '))
    #현금인지 카드인지에 따라 할인액 계산
    if num == 1 :
        # 현금 할인율 계산
        print('할인율 10%')
        print('할인액 : %d' % (int(pay*0.1))+'원')
    else :
        # 카드 할인율 계산
        print('할인율 5%')
        print('할인액 : %d' % (int(pay*0.05))+'원')
else :
    print('잘못 입력하였습니다. 종료합니다.')