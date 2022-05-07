# 1
#
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
#
#
# 이름 가격 재고
#
# 메로나 300 20
# 비비빅 400 3
# 죠스바 250 100

inventory = dict(zip(['메로나','비비빅','죠스바'],[[300,20],[400,3],[250,100]]))
# inventory = {'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}
print(inventory)


# 2
#
# 1의 inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# 실행 예시:
# 300 원

pay = inventory['메로나'] # 리스트 출력
print(pay[0],' 원') # 리스트 인덱싱

print(inventory['메로나'][0],' 원')
## 앞에는 딕셔너리(inventory['메로나']) 결과로 리스트 --- 리스트 접근 : 인덱싱[0]

# 3
#
# 1의 inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# 실행 예시:
# 20 개

print(inventory['메로나'][1],' 개')

# 4
#
# 1의 inventory 딕셔너리에 아래 데이터를 추가하라.

# 이름 가격 재고
# 월드콘 500 7

# 실행 예시:
# >> print(inventory)
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

inventory['월드콘'] = [500,7]

# 5
# 다음의 딕셔너리에서 key 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_keys = list(icecream.keys())
print(icecream_keys)

# 6
#
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_values = list(icecream.values())
print(icecream_values)

# 7
#
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# 출력 예시:
# 6700

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
tot = sum(icecream_values)
# tot = sum(list(icecream.values())) # 위 리스트 변수 참고
# tot = sum(icecream.values()) # sum() 함수가 자체 리스트로 변환
print(tot)



# 8
#
# 아래의 new_product 딕셔너리를 7번의 icecream 딕셔너리에 추가하라.
# new_product = {'팥빙수':2700, '아맛나':1000}
#
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수': 2700,  '아맛나': 1000}

new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
# ice_1={**icecream,**new_product}
# icecream['팥빙수'] = 2700
# icecream['아맛나'] = 1000

# 9
#
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
# keys = ('apple', 'pear', 'peach')
# vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

keys = ('apple', 'pear', 'peach')
vals = (300, 250, 400)
result = dict(zip(keys,vals)) # zip 함수에 튜플도 사용 가능
print(result)

# 10
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
#
# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))

## zip 함수 매개변수로 튜플이나 리스트를 사용할 수 있다!