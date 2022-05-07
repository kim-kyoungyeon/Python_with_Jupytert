
print('======================================상품정보=====================================\n'
               '1 노트북  : 1,200,000 원\n'
               '2 디지털카메라 : 400,000 원\n'
      '=================================================================================')
num= int(input('상품번호 입력: '))

if num == 1 or num == 2 :
    order = int(input('주문수량 입력 : '))
    #노트북 값 따로 카메라값 따로 계산
    if num == 1 :
        #노트북 가격
        name= '노트북'
        price = 1200000
        tot = int(price*order)
        if tot >= 1000000 :
            dis = tot *0.1
        elif tot >= 500000 :
            dis = tot *0.05
        else :
            dis = 0
    else :
        name = '카메라'
        price = 400000
        tot = int(price * order)
        if tot >= 1000000:
            dis = tot * 0.1
        elif tot >= 500000:
            dis = tot * 0.05
        else:
            dis = tot
    print('=============================== 주문 내용==================================================')
    print('상품명 : %s' %name )
    print('가격 :  ',format(price,','),'원')
    print('주문수량 : %d ' % order)
    print('주문액 : ',format(tot,','),'개')
    print('할인액 : ' ,format(dis,',.0f'),'원')
    tsum =int(tot - dis)
    print('총지불액 : ',format(tsum, ',.0f'), "원")
else:
    print('잘못입력 종료')
