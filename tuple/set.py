#집합(set)
#수학의 집합
#중복되지 않은 항목이 모인것
#집합 = {항목1, 항목2,............항목 n}
#특징 순서가 없다
#입력되는 순서와 출력되는 순서가 다를수있따
#동일한 요소값이 중복될수 없다
#인덱스 사용불가 :이미 포함되어있는 요소 값을 변경할 수 없다

#요소 추가/삭제가능
#집합안에 변경가능한 항목포함할수없음
#리스트포함불가 튜플 포함가능/ 튜플은 변경불가
#집합만들기
s= {1,2,3,4,5}
print(s)
print(type(s)) # class set
#set 함수로 집합생성
s1  = set([10,20,30]) #리스트로 형변환 시켜 집합생성
print(s1) #집합형태로 변환됨
print(type(s1))#<class 'set'>
s2 = set((100,200,300)) #튜플을 집합으로 형변환
print(s2)#{200, 100, 300}
#동일요소 중복될수없다
s3 = {1,2,3,3,4}
print(s3) # {1, 2, 3, 4} 동일요소가 두번 입력되어있으면 한개 남기고 전부삭제

#튜플을 요소로 갖는 집합 생성
s4={1,2,3,(5,6)}
print(s4)#{1, 2, 3, (5, 6)} - 튜플은 set 요소로 가능

#리스트를 요소로 갖는 집합 생성
s5={1,2,[3,4]}
print(s5)
#TypeError: unhashable type: 'list'
# index 사용불가
print(s4[0])
#TypeError: 'set' object is not subscriptable

#집합의 요소 추가
# add () 1개 추가시 , update() 여러개추가시
s={1,2,3}
s.add(4)
print(s)

s.update(5,6)
#TypeError: 'int' object is not iterable
#여러개의 요소를 추가할때는 list 형태로 전다
s.update([5,6])
print(s) #{1, 2, 3, 4, 5, 6}


#집합요소제거 :remove 값 -없는값 제거시 에러
# discard 값 - 없는값 제거시 에러없음

s.remove(3)
print(s)
s.discard(4)
print(s)

#없는요소삭제
#s.remove(10)
s.discard(10)

#전체요소삭제
s.clear()
print(s) # set() :빈집합입니다

# 집합삭제
del s # 삭제됨
print(s) #NameError: name 's' is not defined

#집합연산
#합집합 A.union(B)
# 교집합 A.intersection(B)
# 차집합 A.difference(B)
###############
a= {1,2,3}
b={4,5,6}
#합집합 ?-연산기호 |
c= a.union(b)
C = a|b
print(c,C)
#교집합 &
c=a.intersection(b)
C= a&b
print(c,C)

#차집 = -
c= a.difference(b)
C= a-b
print(c,C)


































































































