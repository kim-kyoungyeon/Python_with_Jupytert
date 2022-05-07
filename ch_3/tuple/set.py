# 집합(set)
# 수학의 집합
# 중복되지 않은 항목들이 모인 것
# 집합 = {항목1,항목2,...,항목n}

# 특징
# 순서가 없다.
# 입력되는 순서와 출력되는 순서가 다를 수 있다.
# 동일한 요소(값)이 중복될 수 없다.
# 인덱스 사용 불가 : 이미 포함되어 있는 요소값을 변경할 수 없다.
# 요소 추가/삭제는 가능
# 집합 안에 변경 가능한 항목 포함할 수 없음 : 리스트는 포함 불가/튜플은 포함 가능(튜플은 변경 불가)

# 집합 만들기
s = {1,2,3,4,5}
print(s)
print(type(s)) # <class 'set'>

# set() 함수로 집합 생성
s1 = set([10,20,30]) #리스트를 형 변환시켜 집합 생성
print(s1) #집합형태로 변환됨
print(type(s1)) # <class 'set'>

s2 = set((100,200,300)) #튜플을 집합으로 형 변환
print(s2) # {200, 100, 300}

# 동일한 요소가 중복될 수 없다.
s3 = [1,2,3,4,5]
print(s3) # [1, 2, 3, 4, 5] --- 동일요소가 두 번 입력되어 있으면 한 개 남기고 모두 삭제

# 튜플을 요소로 갖는 집합 생성
s4 = {1,2,3,(5,6)}
print(s4) # {1, 2, 3, (5, 6)} --- 튜플은 set요소로 가능


# 리스트를 요소로 갖는 집합 생성
# s5 = {1,2,[3,4]}
# TypeError: unhashable type: 'list'
# print(s5)

# 인덱스 사용 불가
# print(s4[0])
# TypeError: 'set' object is not subscriptable

# 집합에 요소 추가
# add() : 1개 추가시, update() : 여러개 추가시
s = {1,2,3}
s.add(4)
print(s) # {1, 2, 3, 4}

# s.update(5,6)
# TypeError: 'int' object is not iterable

# 여러개의 요소를 추가할 때는 list 형태로 전달
s.update([5,6])
print(s) # {1, 2, 3, 4, 5, 6}

# 집합 요소 제거
# remove(값) ---- 없는 값 제거 시 에러 발생
# discard(값) --- 없는 값 제거 시 에러 없음
s.remove(3)
print(s)

s.discard(4)
print(s)

# 없는 요소 삭제
# s.remove(10) #에러 발생
s.discard(10) #에러 없음

# 집합의 전체 요소 삭제
s.clear()
print(s) # set() : 빈 집합

# 집합 삭제
del s #삭제 됨

# print(s) --- NameError: name 's' is not defined

# 집합 연산
# 합집합 : A.union(B)
# 교집합 : A.intersection(B)
# 차집합 : A.difference(B)

#-------------------------------------------------
a = {1,2,3}
b = {4,5,6}

# 합집합 --- 연산기호 |
c = a.union(b) # {1, 2, 3, 4, 5, 6}
C = a|b # {1, 2, 3, 4, 5, 6}
print(c,C)

# 교집합 --- 연산기호 &
c = a.intersection(b)
C = a&b
print(c,C)

# 차집합 --- 연산기호 -
c = a.difference(b)
C = a-b
print(c,C)




