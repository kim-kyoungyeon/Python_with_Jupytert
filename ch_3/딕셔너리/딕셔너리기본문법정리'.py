# 딕셔너리 만들기
#딕셔너리 만드는 방법
# (1) {} 중괄호 안에 키: 값 형식으로 저장
#           딕셔너리 = {키1 : 값1, 키2:값2}
# (2) 빈딕셔너리 만ㄷ르기 {} 만 지정
#           딕셔너리 = {}
# (3) dict() 함수 사용
#       딕셔너리 = dict()
#       딕셔너리 = dict(키1=값1)
#       딕셔너리 = dict(zip[키1,키2],[값1,값2])
#       딕셔너리 = dict([(키1,키2),(값1,값2)])
#       딕셔너리 = dict({키1:값2,키2,값2}) # dict 생략해도 가능

#(1)
scores={'kor':90,'eng':88, 'math':95}
print(scores)
#(2)
students = {} #빈 딕셔너리 생성
#item 추가
students['name']= '홍길동'
students['age'] =23
print(students)

#(3)
person= dict() #빈 딕셔너리 생성
person['이름'] = '홍길동'
person['키'] = 175
person['몸무게'] = 65
print(person)

person2 = dict(이름= '이몽룡', 키=175) # 키값이 문자열 이어도 '' 사용하지 않습니다.(only)
print(person2)

person3 =dict(zip(['이름','키','몸무게'],['성춘향',160,50]))
print(person3)

#딕셔너리 item추가
#key: value 로 이루어짐
d= {1:'a'}
print(d)
#두번째 요소 추가 key2 vlaue b
d[2] = 'b' #주의 2는 인덱스가 아닌 그냥 키에 해당된다
print(d) #{1: 'a', 2: 'b'}

print(type(d))
# =-----------------------
#key는 문자도 가능
d['no']=3
print(d) #{1: 'a', 2: 'b', 'no': 3}

#길면  여러줄로 입력
naver = {
    'name ' :'naver',
    'url' : 'www.naver.com',
    'userid' : 'nv',
    'password' :'1234'}
print(naver)
#{'name ': 'naver', 'url': 'www.naver.com', 'userid': 'nv', 'password': '1234'}
#관련함수
#keys(), values(), items() 함수
print(naver.keys())# key리스트반환
print(naver.values())#value 리스트반환
print(naver.items())# key,value 쌍으로된 튜플의 리스트
# dict_keys(['name ', 'url', 'userid', 'password'])
# dict_values(['naver', 'www.naver.com', 'nv', '1234'])
# dict_items([('name ', 'naver'), ('url', 'www.naver.com'), ('userid', 'nv'), ('password', '1234')])

print(type(naver.keys()))
print(type(naver.values()))
print(type(naver.items()))
# <class 'dict_keys'>
# <class 'dict_values'>
# <class 'dict_items'> > 바로사용불가
#반환되는 값들을 list형태로 형 변환해서 사용해야 함
to_list=list(naver.keys())
print(to_list)
print(type(to_list))
#['name ', 'url', 'userid', 'password']
#<class 'list'>
#각요소출력
for key in naver.keys():
    print(key)
    # url
    # userid
    # password
    # naver
#naver.딕셔너리의 value만 출력하시오
for value in naver.values():
    print(value)
# www.naver.com
# nv
# 1234
#네이버 딕셔너리의 아이템모두 출력
for item in naver.items():
    print(item)
# ('name ', 'naver')
# ('url', 'www.naver.com')
# ('userid', 'nv')
# ('password', '1234')


#key로 value 접근하기
print(naver['userid'])
#get 함수사용가능
print(naver.get('password'))

#존재하지 않는 키로 접근시
print(naver['link'])
#KeyError: 'link'
#get 함수 통해 접근시
print(naver.get('link','없음'))
#없음
#딕셔너리 value 접ㄱ느시 get 이동하면 키가 존재하지 않을경우 에러 방지 가능
######
#관련함수
#딕셔너리 합치기
# 1) update 함수 사용
# 2) ** 연산 사용
#
## 1_ update 사용 : 원래의 dict 값 없어지고 병합 결과만 남음
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

#dict1에 dict 2를 결합하고 dict 1 에 덮어써짐
dict1.update(dict2) #dict1 딕셔너리 변경됨
print(dict1)
print(dict2)

dict2.update(dict1)
print(dict1)
print(dict2)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# {'c': 3, 'd': 4, 'a': 1, 'b': 2}

#(2) ** 연산자 사용
dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}
# dict3 = {dict1,dict2} # 에러 튜플로인식
#TypeError: unhashable type: 'dict'
#print(dict3)
dict3 = {**dict1,**dict2}
#포인터 연산자 [딕셔너리 튜플이 아닌 ]
print(dict3)
print(dict1)
print(dict2)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 결합된 dict3
# {'a': 1, 'b': 2} #dict1 변경없음
# print(dict2)
# {'c': 3, 'd': 4} #dict 2 변경없음



































































































