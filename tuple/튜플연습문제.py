# 1
#
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable=()
#소괄호 비어있는 튜플
print(type(my_variable))

#2
#
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a' #오류발생
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
#튜플은 변경이 불가한데 원소 접근해서 변경 하려고 했음

# 3
#
# 숫자 1 이 저장된 튜플을 생성하라.
tutu=1,
t1=(1,)
t2= 1,
t3 = (1) #정수 1을 저장
print(tutu)

# 4
#
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4

t = 1, 2, 3, 4
print(type(t))
#class tuple
#원칙적으로 튜플은 괄호와 함께 데이터 정의해야하지만
#사용자 편의를 위해 괄호생략가능

# 5
#
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')
t=('A', 'b', 'c')

# 6
#
# 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
data= list(interest)
print(data)
# 7
#
# 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data= tuple(interest)
print(data)
# 8
#
# 아래 코드의 실행 결과를 예측하라
my_tuple = (1, 2, 3) # 튜플 my tuple 생성
a, b, c = my_tuple #my_tuple 의 요소를 각각 변수 a.b .c에 대입
print(a + b + c) # 6
print(a)
print(b)
print(c)



















