#청취_강윤진_파이썬2일차


# 다음과 같이 프로그램 작성
# 상품번호 입력 시 1, 2 이외의 숫자 입력하면 프로그램 종료
# 할인액
# 주문액이 백만원 이상 - 10%
# 백만원 미만 5십만원 이상 - 5%
# 5십만원 미만 할인 없음


print('**************상품 정보**************')
print('1 노트북 : 1,200,000 원'
      '2 디지털 카메라 : 400,000원')
print('************************************')

no = int(input('상품번호 입력 : '))
if no == 1 or no == 2 :
    quantity = int(input('주문 수량 입력 : '))
    if no == 1 :
        item = 1200000
    else :
        item = 400000
    total = item*qunatity
    if total >= 1000000:
        sale_price = 0.1
    elif total >= 500000 and total < 1000000 :
        sale_price = 0.05
    else :
        sale_price = 0
    if no == 1 :
        print('**************주문 내용**************')
        print('상품명 :        노트북')
        print('가격 :         ', format(item,','), '원')
        print('주문 수량 :     %d' % quantity)
        print('주문액 :       ', format(total,','),'원')
        print('할인액 :       ', format(int(total*sale_price), ','), '원')
        print('총 지불액 :    ', format(int(total-(total*sale_price)), ','), '원')
    else :
        print('**************주문 내용**************')
        print('상품명 :        노트북')
        print('가격 :         ', format(item, ','), '원')
        print('주문 수량 :     %d' % quantity)
        print('주문액 :       ', format(total, ','), '원')
        print('할인액 :       ', format(int(total * sale_price), ','), '원')
        print('총 지불액 :    ', format(int(total - (total * sale_price)), ','), '원')
else :
    print('잘못 입력하였습니다. 종료합니다.')

