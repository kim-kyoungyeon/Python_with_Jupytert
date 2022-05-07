# 딕셔너리 만들기
# 딕셔너리 만드는 방법

# (1) {} 중괄호 안에 키:값 형식으로 저장
#     딕셔너리 = {키1:값1,키2:값2,...,키n:값n}

# (2) 빈 딕셔너리로 만들기 : {}만 지정
#     딕셔너리 = {}

# (3) dict() 함수 사용 : 형변환
#     딕셔너리 = dict()
#     딕셔너리 = dict(키1:값1, 키2:값2)
#     딕셔너리 = dict(zip([키1,키2], [값1,값2]))
#     딕셔너리 = dict([(키1,키2), (값1,값2)])
#     딕셔너리 = dict({키1:값1,키2:값2}) -----> dict() 생략해도 가능

#---------------------------------------
# (1)
scores = {'kor':90,'eng':88,'math':95}
print(scores) # {'kor': 90, 'eng': 88, 'math': 95}

#(2)
students = {} # 빈 딕셔너리 생성
# item 추가하기
students["name"] = "홍길동"
students["age"] = 23
print(students) # {'name': '홍길동', 'age': 23}

#(3)
person = dict() # 빈 딕셔너리 생성
person["이름"] = "홍길동"
person["키"] = 175
person["몸무게"] = 65
print(person) # {'이름': '홍길동', '키': 175, '몸무게': 65}

person2 = dict(이름='이몽룡',키=175)
#### 이 경우, 키 값이 문자열이어도 '' 사용하지 않는다 ####
print(person2) # {'이름': '이몽룡', '키': 175}

person3 = dict(zip(['이름','키','몸무게'],['성춘향','160','50']))
print(person3) # {'이름': '성춘향', '키': '160', '몸무게': '50'}

# 딕셔너리에 item 추가
# key:value로 이루어짐
d = {1:'a'}
print(d)

# 두번째 요소 추가(key=2,value='b')
d[2] = 'b' ## !!주의!! 2는 인덱스 XXX. 키에 해당함. 순서랑 무관함
print(d) # {1: 'a', 2: 'b'}
print(type(d)) # <class 'dict'>

#-------------------------------------------------
# key는 문자도 가능
d["no"]=3
print(d) # {1: 'a', 2: 'b', 'no': 3}

# 길면 여러 줄로 입력 가능
naver ={
    'name':'naver',
    'url':'naver.com',
    'userid':'nv',
    'password':'1234'
}
print(naver)
# {'name': 'naver', 'url': 'naver.com', 'userid': 'nv', 'password': '1234'}

#-------------------------------------------------
### 관련 함수
# keys(), values(),items() 함수
print(naver.keys()) #key 리스트 반환
print(naver.values()) #value 리스트 반환
print(naver.items()) #(key,value) 쌍으로 된 튜플의 리스트
# dict_keys(['name', 'url', 'userid', 'password'])
# dict_values(['naver', 'naver.com', 'nv', '1234'])
# dict_items([('name', 'naver'), ('url', 'naver.com'), ('userid', 'nv'), ('password', '1234')])

print(type(naver.keys())) # <class 'dic_keys'>
print(type(naver.values())) # <class 'dic_values'>
print(type(naver.items())) # <class 'dic_items'> => 바로 사용 불가

# 반환되는 값들을 list 형태로 형 변환해서 사용해야 함
to_list=list(naver.keys())
print(to_list)
print(type(to_list))
# ['name','url','userid','password']
# <class 'list'>

# 각 요소 출력
for key in naver.keys() :
    print(key)
    # name
    # url
    # userid
    # password

# naver 딕셔너리의 value만 출력하시오.
for value in naver.values() :
    print(value)
    # naver
    # www.naver.com
    # nv
    # 1234

# naver 딕셔너리의 item을 모두 출력하시오.
for item in naver.items() :
    print(item)
    # ('name', 'naver')
    # ('url', 'naver.com')
    # ('userid', 'nv')
    # ('password', '1234')

# key로 value 접근하기
print(naver['userid'])
## get() 함수 사용 가능
print(naver.get('password'))

# 존재하지 않는 키(ex. link)로 접근했을 때
# print(naver['link'])
# KeyError : 'link'

# get() 함수 통해서 접근하면,
print(naver.get('link','없음'))
# 없음
# 딕셔너리 value 접근 시 get() 이용하면 키가 존재하지 않을 경우에 에러를 방지할 수 있음

#----------------------------------------------------------
# 관련함수
# 딕셔너리 합치기
#(1) update() 사용
#(2) ** 연산 사용

#(1) update() 사용 : 원래의 dict 값 없어지고 병합 결과만 남음
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

# dict1에 dict2를 결합하고 dict1에 덮어쓰여짐
# dict1.update(dict2) # dict1 딕셔너리가 변경됨
# print(dict1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(dict2) # {'c': 3, 'd': 4}

dict2.update(dict1)
print(dict1) # {'a': 1, 'b': 2}
print(dict2) # {'c': 3, 'd': 4, 'a': 1, 'b': 2}

#(2) ** 연산자 사용
dict1 = {'a':1,'b':2}
dict2 = {'c':3,'d':4}

# dict3 = {dict1,dict2} --- 에러! 데이터를 튜플로 인식
# TypeError: unhashable type: 'dict'
dict3 = {**dict1,**dict2}
print(dict3) # {'a': 1, 'b': 2, 'c': 3, 'd': 4} : 결합된 dict3
print(dict1) # {'a': 1, 'b': 2} : dict1 --- 변경 없음
print(dict2) # {'c': 3, 'd': 4} : dict2 --- 변경 없음