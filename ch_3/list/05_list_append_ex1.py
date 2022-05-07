# Q. 3명의 회원을 입력 받아 리스트에 추가하고, 리스트 내용 출력(for 문 사용)
# 빈 리스트 생성
members = []

# 리스트에 추가
for i in range(3) :
    member = input('회원 입력 : ')
    members.append(member)

# 리스트 내용 출력
print('회원 명단 : ',end=' ')
for member in members :
    print(member, end=' ')
# 회원 명단 :  홍길동 이몽룡 성춘향

print('\n 회원명단 :',members)
#  회원명단 : ['홍길동', '이몽룡', '성춘향'] --- 리스트 형태로 출력