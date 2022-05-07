#사용자에게 id 입력받아 해당 id가 리스트에있으면
#로그인성공, 없으면 로그인 실패를 출력하시오
#단 입력시 삽입되는 공백을 제거하고 로그인 여부를 판별하시오
# ids = ['sun','moon','flower','sky']
# user=input('id입력: ')
# print(user.strip())
# if user == ids :
#     print('로그인성공')
# else:
#     print('로그인실패')
#
##정답
ids = ['sun','moon','flower','sky']
ID= input('ID를 입력하시요:')
if(ID.strip() in ids) :
    print('로그인 성')
else:
    print("로그인실패")
