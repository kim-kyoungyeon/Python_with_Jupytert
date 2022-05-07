# 청취_xxx_리스트1

# Q. 상품을 리스트에 추가, 아무것도 안 적고(공백) 엔터키 누르면 입력 종료되고 등록된 상품 리스트 출력
# 리스트에 추가해야 하므로 빈리스트 생성
# products = []
#
# # 조건 참일 경우 무한 반복
# while True :
#     product = input('상품 등록 (엔터키 누르면 종료) : ')
#     products.append(product)
#     # 반복 수행 종료 조건
#     if product == '' :
#         break
#
# # 등록된 상품 리스트 출력
# print('등록된 상품 : ',end=' ')
# for product in products :
#     print(product,end=' ')


#=== 풀이 ===#
# 리스트에 추가해야 하므로 빈리스트 생성
item = []

while True :
    pro = input('상품 등록 (엔터키 누르면 종료) : ')
    if pro == '' :
        break
    item.append(pro)

print('등록된 상품 : ',end='')
for pro in item :
    print(pro,' ',end=' ')
