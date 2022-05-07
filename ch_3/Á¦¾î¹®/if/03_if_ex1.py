# 다음과 같은 로그인 프로그램 작성
# 등록된 ID : flower
# 비밀번호 : 1234

# ID와 비밀번호를 입력받아 로그인 성공 또는 로그인 실패를 출력하시오.

# ID, 비밀번호 변수에 저장
ID = "flower"
password = '1234'

# 입력 코드
input_id = input('아이디 입력 : ')
input_pass = input('비밀번호 입력 : ')

# 비교 후 출력 코드
if(ID==input_id) and (password==input_pass) :
    print('로그인 성공!')
else :
    print('로그인 실패!')