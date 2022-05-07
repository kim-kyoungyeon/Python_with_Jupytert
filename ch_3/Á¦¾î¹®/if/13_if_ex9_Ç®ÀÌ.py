# 사용자로부터 상품 선택 데이터 입력 코드
print('******************************************')
print('1 노트북 : 1,200,000 원 ')
print('2 디지털 카메라 : 400,000 원')
print('******************************************')
num = int(input('상품번호 입력 : '))

# 1,2를 제외한 나머지에 대해서는 종료 메시지 출력
if num != 1 and num !=2 :
    print('\n잘못 입력하였습니다. 종료합니다.')
else : #상품번호 제대로 입력한 경우
    qty = int(input('주문 수량 입력 : '))

    #입력된 상품 번호에 따라서 상품명과 가격 결정
    if num == 1 :
        product = '노트북'
        price = 1200000
    else :
        product = '디지털카메라'
        price = 400000

    #주문액 계산
    amount = price * qty

    #할인액 계산
    if amount >= 1000000 :
        discount = int(amount*0.1)
    elif amount > 500000 :
        discount = int(amount*0.05)
    else :
        discount = 0

    #총 지불액 계산
    total = amount - discount

    print('\n**********주문 내용**********')
    print('상품명 : \t',product)
    print('가격 : \t',format(price,','),'원')
    print('주문수량 : \t',qty)
    print('주문액 : \t',format(amount,','),'원')
    print('할인액 : \t',format(discount,','),'원')
    print('총 지불액 : \t',format(total,','),'원')
