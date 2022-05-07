# join() 함수
# 각 문자 사이에 특정 문자(열) 삽입
# 삽입될문자(열).join(대상문자)

a = 'aa'
print(a.join('bbb')) # baabaab

# 주로 문자열 사이에 구분자 삽입 시 사용
a = '-'
print(a.join('bbb')) # b-b-b

# 리스트 사이에 구분자 삽입 시 사용
sep = '-'
names = ['홍길동','이몽룡','성춘향']
print(sep.join(names)) # 홍길동-이몽룡-성춘향

# 숫자 데이터인 경우 주의!(문자형식 숫자)
sep = ','
num = ['10','20','30']
print(sep.join(num)) # 10,20,30
## 주의 !
num = [10,20,30] # join 연산자 사용 불가 --- 문자열이어야 함




