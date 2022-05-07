# objs=[]
# for i in range() :
#     obj = input("상품 등록 (엔터키 누르면 종료):")
#     objs.append(obj)
#     if obj == " ":
#         break;
# print('등록된 상품 :%s'%obj,end=' ')
###리스트 추가해야해서 빈리스트 생성
item=[]
while True:
    pro=input("상품 등록 (엔터키 누르면 종료):")
    if pro == '':
        break
    item.append(pro)
print('등록된 상품 :',end=' ')
for pro in item :
    print(pro,'   ',end='')


























