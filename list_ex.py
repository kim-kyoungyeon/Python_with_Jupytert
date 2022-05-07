
# 1. 리스트 만들기 :  홍길동 이몽룡 성춘향 변학도
names = ['홍길동','이몽룡','성춘향','변학도']

# 2. 리스트의 각 요소 출력
for name in names :
    print(name)

# 3. 첫 번째 요소 출력
print(names[0])

# 4. 두 번째 요소 출력
print(names[1])

# 5. 마지막 요소 출력
print(names[-1])

# 6.  빈 리스트 만들고 출력하기 : products
products = []
print(products)

# 7. prd_string 문자열에서 추출하여 products 리스트에 추가
prd_string = "노트북 모니터 마우스 키보드"
prd_string_split = prd_string.split() # 디폴트가 띄어쓰기
for i in range(len(prd_string_split)) :
    products.append(prd_string_split[i])
    print(products)

# 또는
for i in range(4) : # 리스트 길이를 알고 있는 경우만 가능
    products.append(prd_string.split()[i])

# 8. new_members 리스트 새로 만들고
# members  각 요소의 공백 제거하고 저장
members = [" 홍길동 ", " 이몽룡 ", " 성춘향 ", " 변학도 "]
print(members)

new_members = []
for member in members :
    new_members.append(member.strip())
print(new_members)

# 9. 다음의 2개의 리스트로 딕셔너리 생성 : std_dict
# students : 리스트 만들기 :  홍길동 이몽룡 성춘향 변학도
# age : 23 25 26 27
students = ['홍길동','이몽룡','성춘향','변학도']
age = [23,25,26,27]

std_dict = dict(zip(students,age))
print(std_dict)

# 10. std_dict에서 이름만 출력
for name in std_dict.keys() :
    print(name, end=' ')

# 11. std_dict에서 나이만 출력
for age in std_dict.values() :
    print(age, end=' ')

# 12. std_dict에서 이름:나이 출력
for all in std_dict.items() :
    print(all, end=' ')