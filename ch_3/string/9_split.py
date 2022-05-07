# split()
# 구분자를 기준으로 문자열을 나눔
# 특징 : 리스트로 반환
# 구분자 : 기본은 공백
# 구분자 지정 : '-', ':', ','
# 문자열.split(구분자)

string = 'python programming'
string_split = string.split()
print(string_split)
# ['python', 'programming'] : 리스트 형태

print(string_split[0])
# python

names = '홍길동, 이몽룡, 성춘향, 변학도'
names_split = names.split(',')
print(names_split)
# ['홍길동', ' 이몽룡', ' 성춘향', ' 변학도'] : 리스트 형태

colors = 'red:blue:yellow:green'
colors_split = colors.split(':')
print(colors_split)
# ['red', 'blue', 'yellow', 'green']

## 리스트 각 요소 출력(반복문에 list 사용 가능)
for c in colors_split : #리스트 요소 개수만큼 반복
    print(c) #리스트인 경우 리스트 각 요소별로 출력

for c in colors : #문자개수만큼 반복
    print(c) #문자열인 경우 문자별(한글자씩) 출력

# 리스트 각 요소 출력 : range() 사용(리스트 인덱스)
for i in range(0,len(colors_split)) :
    print(colors_split[i]) #인덱싱을 통해 리스트에 직접 접근
