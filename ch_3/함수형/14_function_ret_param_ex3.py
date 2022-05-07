# Q. 다음과 같은 함수를 포함하는 프로그램 작성
# 함수명 : order()
# 상품 가격과 주문 수량을 전달받아서 주문액, 할인액, 지불액을 계산하여 반환
# price, qty,amount,discount,total

def order(p,q) :
    amt = p*q
    if amt >= 100000 :
        dis = int(amt*0.1)
    elif amt >= 50000 :
        dis = int(amt*0.05)
    else :
        dis = 0
    tot = amt-dis
    return amt,dis,tot


price = int(input('상품 가격 입력 : '))
qty = int(input('주문 수량 입력 : '))

amount, discount, total = order(price,qty)

print('-------------------------------')
print('주문액 : %s원' % format(amount,','))
print('할인액 : %s원' % format(discount,','))
print('총지불액 : %s원' % format(total,','))








