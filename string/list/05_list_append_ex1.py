# 3명의 회원ㅇ르 입력받아 리스트에추가하고 리스트내용 출력 for문사용
#
# name=print('회원 입력')
# for i in range(3) :
#     name.append(i)
# print(name)
# 빈리스트
#정답
members = []
for i in range(3) :
    member = input('회원입력')
    members.append(member)
  #리스트내용 출력
print('회원명단', end=' ')
for member in members:
    print(member,end=' ')

print('\n 회원명단 :'.member)
#리스트형태로 출력된다






