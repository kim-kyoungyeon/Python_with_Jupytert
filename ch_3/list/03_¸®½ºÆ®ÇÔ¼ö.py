# 내장함수 vs 메서드
# 내장함수 : 파이썬에서 이미 만들어져 있는 함수
# 예) print(), len()
# 사용방법 : print(변수(객체)), len(변수)

# 메서드 : 함수와 같은 코드 집합이지만 클래스의 멤버로 객체를 통해서 사용 가능
# 예) append(), insert()
# 사용방법 : names.append(), names.count() --- 객체.메서드()

###### len(), count() 함수 ######
# len() : 리스트의 길이 반환(원소의 개수)
# len(리스트) : 내장함수

# count() : 특정 요소의 개수 세기
# 리스트.count(특정요소)

a = [1,2,3,4,5]
print('원소의 개수 : ', len(a))
print('3의 개수 : ',a.count(3))

###### append(), insert() 함수 ######
# append() : 리스트의 끝에 새로운 요소 추가
# 리스트.append(새로운요소)

a=[1,2,3,4]
a.append(5)
print(a) #[1, 2, 3, 4, 5]

a.append([6,7])
print(a) #[1, 2, 3, 4, 5, [6, 7]]

# a.append(8,9) : 원소를 2개 추가하면 에러 발생
# TypeError: append() takes exactly one argument (2 given)

# 빈 리스트 생성하고 요소 나중에 추가 가능
values = []
values.append(10)
values.append(20)
values.append(30)
print(values) #[10, 20, 30]

# for 문 사용하여 요소 추가
scores = []
for i in range(5) :
    scores.append(i)

print(scores) # [0, 1, 2, 3, 4]

# insert() : 특정 위치에 새로운 요소 삽입
# 리스트.insert(위치,새로운요소)

nums = [1,2,3,4,5]
nums.insert(1,200) # 1번 인덱스에 200 삽입, 삽입 위치 이상에 있는 요소들은 위치값을 +1로 증가하게 됨
print(nums) # [1, 200, 2, 3, 4, 5]

nums.insert(-1,'홍길동') # 마지막 원소 앞에 삽입
print(nums) # [1, 200, 2, 3, 4, '홍길동', 5]

nums.insert(len(nums),12.3) # 맨 뒤에 삽입(append()가 더 용이)
print(nums) # [1, 200, 2, 3, 4, '홍길동', 5, 12.3]

nums.insert(len(nums)-1,[10,20]) # 마지막 원소 앞에 하위 리스트 삽입
print(nums) # [1, 200, 2, 3, 4, '홍길동', 5, [10, 20], 12.3]

###### remove(), pop() 함수 ######
# remove() : 리스트에서 값에 해당되는 요소 제거
# 리스트.remove(값)
# 동일한 값이 여러개 있는 경우 첫번째 값만 제거
# 여러개 있는 동일한 값을 모두 제거하려면 반복문 사용
# 모든 요소 제거 : clear() --- 빈 리스트만 남게 됨
n = [1,2,3,4,5,5,3,4,3]
n.remove(4)
print(n) #첫번째 4만 제거

# 동일한 원소 한번에 제거
# 모두 제거되어서 없는데도 remove() 명령이 들어가면 에러 발생
# 몇 개 있는지 확인하고 그 수만큼 반복
n = [1,2,3,4,5,5,3,4,3]
count = n.count(3)
for i in range(count) :
    n.remove(3)
    print('3 삭제 ',n)

print(n) # [1, 2, 4, 5, 5, 4]

# pop() : 꺼내오다
# 리스트.pop() : 리스트의 마지막 요소 반환하고 삭제
# 리스트.pop(인덱스) : 인덱스 위치에 있는 요소 반환하고 삭제
x = ['a','b','c','d']
y = x.pop() # 마지막 요소 반환하고 그 요소 삭제
print(y) # d
print(x) # ['a', 'b', 'c']

x.pop()
x.pop()
x.pop()
print(x) # []

# 리스트가 빈 상태에서 pop() 하면 에러 발생
# x.pop() # IndexError: pop from empty list

# pop(인덱스) : 인덱스 위치 요소 반환하고 삭제
heroes = ['슈퍼맨','스파이더맨','헐크','아이언맨']
heroes.pop(2) # 헐크가 반환되고 원 리스트에서 삭제
print(heroes) # ['슈퍼맨', '스파이더맨', '아이언맨']

###### 리스트 확장 : extend() 함수 ######
# 리스트.extend()
# 이전 리스트에 원소 추가하여 확장된 리스트로 변환
# 원래 리스트 변경 됨
a = [1,2,3]
a.extend([4,5])
print(a) # [1, 2, 3, 4, 5] : 리스트의 결합
# a.append([4,5])
# print(a) # [1, 2, 3, [4, 5]] : 하위 리스트로 삽입

###### sort(), sorted(), reverse() 함수 ######
# sort() : 리스트들의 원소들 정렬(기본 : 오름차순)
# 원본 리스트 변경
# 리스트.sort() : 오름차순 vs. 리스트.sort(reverse=True) : 내림차순
scores = [90,78,81,64,89]
scores.sort()
print(scores) # [64, 78, 81, 89, 90] : 오름차순 정렬된 결과

scores = [90,78,81,64,89]
scores.sort(reverse=True)
print(scores) # [90, 89, 81, 78, 64] : 내림차순 정렬된 결과

# reverse()
# 역순으로 원본 리스트 변경(정렬은 하지 않고 순서만 반대로 변경)
# 리스트.reverse()
scores = [90,78,81,64,89]
scores.reverse() # [89, 64, 81, 78, 90] : 정렬 없이 역순으로 변경
print(scores)

# sorted() : 파이썬 내장 함수
# 원본 유지하면서 정렬된 새로운 리스트를 반환
# sorted(리스트)
a = [3,5,2,1,4]
b = sorted(a)
print('a : ', a) # a :  [3, 5, 2, 1, 4]
print('b : ', b) # b :  [1, 2, 3, 4, 5]

### sort 정렬 기준 정리 ###
# 1) 영문자 : 대문자 앞으로, 소문자 뒤로 정렬
# 아스키 코드값이 대문자가 소문자보다 작다
char = ['b','A','d','C']
char.sort()
print(char) # ['A', 'C', 'b', 'd']

# 대소문자 구별없이 정렬하고자 한다면 : key 매개변수에 str.lower 지정
char = ['b','A','d','C']
char.sort(key=str.lower)
print(char) # ['A', 'b', 'C', 'd']

# 대소문자 구별없이 역순으로 정렬
char = ['b','A','d','C']
char.sort(key=str.lower,reverse=True)
print(char) # ['d', 'C', 'b', 'A']

# 문자열은 첫문자로 정렬됨 : 대문자 먼저 소문자 나중에
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort()
print(ids) # ['Blue', 'GREEN', 'SKY', 'eBook', 'red']

# 대소문자 구별없이 정렬
ids = ['SKY','Blue','red','eBook','GREEN']
ids.sort(key=str.lower)
print(ids) # ['Blue', 'eBook', 'GREEN', 'red', 'SKY']

###### max(), min() 함수 ######
n = [100,7,-2,99,30]
print('최대 : ',max(n)) # 최대 :  100
print('최소 : ',min(n)) # 최소 :  -2

# 문자는 아스키 코드값으로 비교
n = ['c','a','D','B','A']
# A : 65
# B : 66
# C : 67
# a : 97
# b : 98
# c : 99

print('최대 : ',max(n)) # 최대 :  c
print('최소 : ',min(n)) # 최소 :  A

###### index() 함수 ######
# index() : 리스트 안에서 원소의 위치값 반환
# 원소가 존재하지 않으면 에러 발생
# 리스트.index(값)
a = [1,2,3,4,5]
print(a.index(3)) # 2
# print(a.index(0)) # ValueError: 0 is not in list

names = ['홍길동','이몽룡','성춘향']
print(names.index('성춘향')) # 2
# print(names.index('변학도')) # ValueError: '변학도' is not in list
# 주의 ! 리스트에는 find() 메서드가 없음 : 에러 처리를 반드시 해줘야 함

###### in(), notin() 함수 ######
# 리스트 내에서 원소의 존재 여부를 반환(포함여부: True/False)
num = [1,2,3,4,5]
result = 2 in num # 2가 있나? -> 있다 : True
print(result)

result = 3 not in num # 3이 없나? -> 있다 : False
print(result)

# 리스트 일치 검사
# 비교연산자 사용해서 2개의 리스트 비교
# ==, >=, <=, >, <, !=
# 첫번째 요소부터 비교 시작
# 첫번째 요소의 비교에서 결과가 False면 더이상 비교하지 않고 종료
# 첫번째 요소 결과가 True면, 두번째 요소 비교 True면 세번째 비교
# 모든 요소 비교에서 모두 True면 최종적으로 True가 됨
list1 = [1,2,3]
list2 = [1,3,3]
print(list1 == list2)




