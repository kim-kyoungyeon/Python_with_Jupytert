#join 은 split한 문자를 문자 사이사이에 중간중간에 글자를 넣는다
# join = '' , 한묶음
# a = ''
# split 과 반대되는개념
# join()
# 각문자 사이에 특정 문자열 삽입
#삽입된 문자열.join(대상문자)

a= 'aa'
print(a.join('bbb'))#baabaab
#주로 문자열 사이에 구분자 삽입시 사용된다
a = '-'
print(a.join('bbb'))#b-b-b
# 리스트 사이에 구분자 삽입시 사용
sep ='-'
names = ['홍길동','이몽룡','성춘향']
print(sep.join(names))#홍길동-이몽룡-성춘향
#숫자 데이터인 경우 주의
sep = ','
num=['10','20','30'] # 문자
print(sep.join(num))#10,20,30
#주의
num=[10,20,30]# join연산자 사용 불가- 문자열 이여야 함 # 수치데이터
