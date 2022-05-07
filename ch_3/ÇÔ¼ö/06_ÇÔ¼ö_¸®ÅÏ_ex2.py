# 상품가격, 주문수량을 입력받아서 주문액을 구한 후에
# 상품가격, 주문수량, 주문액을 반환하는 함수 order()를 정의하시오.

# order() 함수를 호출해서 반환된 결과로 아래 내용을 출력하시오.
# 상품가격 : 1000원
# 주문수량 : 5개
# 주문액 : 5000원

def order() :
    pr = int(input('상품가격 입력: '))
    qt = int(input('주문수량 입력: '))
    amt = pr * qt
    return pr,qt,amt

price,qty,amount = order()

print ('상품가격 : %d원' % price)
print ('주문수량 : %d개' % qty)
print ('주문액 : %d원' % amount)