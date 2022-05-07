# 사용자에게 ID를 입력받아 해당 ID가 리스트에 있으면 로그인 성공, 없으면 로그인 실패를 출력하시오.
# 단, 입력 시 삽입되는 공백을 제거하고 로그인 여부를 판별하시오.

ids = ['sun','moon','flower','sky']
ID = input('ID를 입력하세요. : ').strip()

if ID in ids :
    print('로그인 성공')
else :
    print('로그인 실패')

#=== 풀이 ===#
if (ID.strip() in ids) :
    print('로그인 성공')
else:
    print('로그인 실패')