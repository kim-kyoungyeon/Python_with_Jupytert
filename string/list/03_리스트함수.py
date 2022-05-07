#내장함수 vs 메서드
#내장함수 : 파이썬에서 이미 만들어져있는 있는 함수
#print() len()
# 사용법 print(변수(객체)), len(변수)

#메서드
#함수와 같은 코드 집합이지만 클래스의 멤버로 객체를 통해서 사용가능
#append /insert
# 사용법 :객체 메서드 ()
#names.append () names.count()
#len 과 count 함수
#len : 리스트의 길이를 반환한다 (원소의 개수)
#len(리스트) : 내장함수

#count() : 특정 요소의 개수를 세기
# 리스트, count (특정요소)
a= [1,2,3,4,5]
print('원소의 개수 : ', len(a))
print('3의 개수 : ',a.count(3))

#append () insert()
#append( ) 리스트의 끝에 새로운 요소 추가

#리스트, append 새로운 요소
#insert() 특정위치에 새로운 요소 삽입
#리스트 insert(위치,값)
a= [1,2,3,4]
a.append(5)
print(a)#[1, 2, 3, 4, 5]
a.append([6,7])
a
#[1, 2, 3, 4, 5, [6, 7]]
a.append(8,9)#원소2개추가하면 에러
#TypeError: append() takes exactly one argument (2 given)
#빈 리스트 생성하고 요소나중에추가가능
values=[]
values.append(10)
values.append(20)
values.append(30)
print(values)#[10, 20, 30]#사용자에게 정보를 입력받는코드
#for문 사용하여 요소 추가
scores=[]
for i in range(5) :
    scores.append(i)
print(scores)
#[0, 1, 2, 3, 4]
#insert() 특정 위치에 새로운 요소 삽입
#리스트. insert (위치,값)
nums=[1,2,3,4,5]
nums.insert(1,200)
print(nums)#[1, 200, 2, 3, 4, 5]
#삽입위치 이상에 있는 요소들은 위치값을 +1로 증가하게된다

nums.insert(-1,'홍길동')
print(nums)#[1, 200, 2, 3, 4, '홍길동', 5]

nums.insert(len(nums),12.3) #맨뒤에 삽입
print(nums)
#[1, 200, 2, 3, 4, '홍길동', 5, 12.3]

nums.insert(len(nums)-1,[10,20])#마지막 원소 하위 리스트삽입
print(nums)
#[1, 200, 2, 3, 4, '홍길동', 5, [10, 20], 12.3]

##remove()/pop()###############333
#remove() 리스트에서 ㄱ밧에 해당되는 요소 제거
#리스트.remove(값)
#동일한 값이 여러개 있는 경우 첫번째 값만 제거
#여러개 있는 동일한 값 모두 제거 하려면 반복문 써야힘
#모든요소제거 clear() 빈리스트만 남음
#pop 꺼내오다
#리스트.pop () 리스트의 마지막 요소 반환후 삭제
#리스트.POP() 인덱스 위치에 있는 요소를 반환후 삭제
n = [1,2,3,4,5,5,3,4,4.3]
n.remove(4) #첫번째 4만 제거
print(n)
# 동일한 원소를 한번에 제거
#모두 제거되서 없는데 remove 명령이 들어가면 에러
#몇개 있는지 꼭 확인후 그 수만큼 반복
n = [1,2,3,4,5,5,3,4,4,3]
count=n.count(3)
for i in range(count):
    n.remove(3)
    print('3삭제',n)
print(n)

#####
x=['a','b','c','d']
y=x.pop()
print(y) #d
print(x) #['a', 'b', 'c']

x.pop()
x.pop()
x.pop()
print(x) #[]
#리스트가 빈 상태에서 pop 하면 에러
x.pop()
#IndexError: pop from empty list

#pop 인덱스 : 인덱스 위치 요소 반환하고 삭제
heroes = ['슈퍼맨', '스파이더맨','헐크','아이언맨']
heroes.pop(2) # 헐크가 반환되고 원 리스트에서 삭제
print(heroes)
# 리스트 확장 : extend()
#리스트.extend()
#이전 리스트에 원소 추가하여 확장된 리스트로 변환
#원래 리스트 변경됨
a = [1,2,3]
#a.extend([4,5])
#print(a) # [1, 2, 3, 4, 5] 리스트 결합

a.append([4,5]) #끼워넣기 #하위리스트 삽입
print(a)#[1, 2, 3, [4, 5]]

# sort ()/ sorted()/reverse()
# sort() : 리스트들의 원소를 정렬 (기본: 오름차순)
# 원본 리스트 변경
# 리스트.sort / sort(reverse=True)내림차순
scores= [90,78,81,64, 89]
scores.sort()
print(scores) #오름차순결과
scores= [90,78,81,64, 89]
scores.sort(reverse=True) #내림차순
print(scores)

# reverse
# 역순으로 원본 리스트 변경 ( 정렬은 하지 않고 순서만 반대로 변경)
#리스트.reverse ()

scores= [90,78,81,64, 89]
scores.reverse()
print(scores) # 순서만 변경된상태

# sorted 파이썬내장함수
# 원본유지 하면서
# 정렬된 새로운 리스트 반환
# sorted(리스트)
a= [3,5,2,1,4]
b= sorted(a)
print('a:',a)
print('b:',b)

#sort의 정렬기준 정리########
# 영문자는 대문자 앞으로 소문자 뒤로 정렬
#아스키코드값이 대문자가 소문자보다 작다
char = ['b','A','d','C']
char.sort()
print(char)#['A', 'C', 'b', 'd']
#대소문자/ 소문자 구별
#대소문자 구별없이 정렬
#key 매개변수에 str.lower 지정하고
char = ['b','A','d','C']
char.sort(key=str.lower)
print(char)#['A', 'C', 'b', 'd']
#['A', 'b', 'C', 'd'] 대소문자 구별없이 정렬하기
char = ['b','A','d','C']
char.sort(key=str.lower,reverse=True)
print(char)#['A', 'C', 'b', 'd']
#['d', 'C', 'b', 'A']

#문자열은 첫문자로 정렬됨 : 대문자 먼저 소문자 나중에
ids= ['SKY',"Blue",'red','eBook',"GREEN"]
ids.sort()
print(ids)#['Blue', 'GREEN', 'SKY', 'eBook', 'red']
#대소문자 구별없이 정렬
ids= ['SKY',"Blue",'red','eBook',"GREEN"]
ids.sort(key=str.lower)
print(ids)#['Blue', 'eBook', 'GREEN', 'red', 'SKY']

#-------ㅡmax() min()#########3
n = [100,7,-2,99,30]
print('최대:',max(n)) # 100
print('최대:',min(n)) # -2
#문자는 아스키 코드값 비교
n =['c','a','D','B','A']
A: 65
B: 66
C : 67
a: 97
b: 98
c: 99
print('최대: ',max(n))
print('최소',min(n))

#index() 함수 리스트 안에서 원소의 위치값 반환
#원소가 존재하지 않으면 에러
#리스트.index(r값)
a=[1,2,3,4,5]
print(a.index(3)) # 2
print(a.index(0)) #에러

names=['홍길동','이몽룡','성춘향']
print (names.index('성춘향'))
print (names.index('변학도')) #에러발생
#리스트에서는 find 메서드가 없음 :에러 처리를 반드시 해줘야함
#in/not in (포함여부)
#리스트내에서 원소의 존재 여부 반환 True/False
num=[1,2,3,4,5]
result= 2 in num #2가 있나? 있다 true
print(result)
result =3 not in num # 3이 없나?
print(result) # 3이 있다 false
# 리스트 일치 검사
# 비교 연산자 사용해 2개의 리스트 비교
# ==>= <= >< !=
# 첫번째 요소부터 비교 시작
# 첫번째 요소의 비교에서 결과 false 면 더이상 비교 하지 않고 종료
#첫번째 요소결과가 true = 두번째 요소 비교 true 면 세번째 비교
# 모든요소 비교에서 모두 true 면 최종 true
list1 = [1,2,3]
list2 = [1,3,3]
print(list1 == list2)



















































