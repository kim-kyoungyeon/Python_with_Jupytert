# number_in = int(input('번호입력 (1. 현금 2. 카드) :'))
# price =""
# if number_in ==1 or number_in ==2 :
#     price= int(input('지불액 입력 : '))
#     if number_in ==1 :
#         print('할인율 = 10%')
#         rate = price * 0.1
#         print('할인액 = %.f원'%rate )
#     else :
#         print('할인율 = 5%')
#         rate = price * 0.05
#         print('할인액 = %.f 원'%rate)
# else :
#     print("잘못입력함,종료합니다")
#
#------------------------정답
#사용자 입력구문
num= int(input('번호입력 (1. 현금 2.카드): '))
#1이나 2가 입력되었나요?
if num == 1 or num == 2 :
    pay = int(input('지불액 입력 : '))
    #현금이냐 카드이냐 할인액 계산
    if num == 1 :
        #현금 할인율 계산
        print('할인율 10%')
        print('할인액 : %d '% (int(pay*0.1))+'원') # 함수를 썼을때는 int 로 묶는다! #변수는 1개
        # 쉼표에 따라 인수 갯수가 다름
        # str 함수와 비교해보기
    else :
         print('할인율 5%')
         print('할인액 : %d ' % (int(pay * 0.05)) + '원')  #
                 #카드 할인율 계산
else :
    print('잘못입력 종료')