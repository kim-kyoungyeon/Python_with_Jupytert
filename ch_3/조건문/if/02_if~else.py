# password는 1234이다
# 사용자에게 password를 입력받아 맞는지 아닌지를 확인하는 프로그램을 작성하시오.

# 입력 양식 :
# 비밀번호를 입력하세요. :

# 출력 양식 :
# 비밀번호가 일치합니다.
# 또는
# 비밀번호가 일치하지 않습니다.

password = 1234 #수치로 입력

# 사용자 입력 코드
in_pass = int(input('비밀번호를 입력하세요. : '))

if in_pass == password :
    print('비밀번호가 일치합니다.')
else :
    print('비밀번호가 일치하지 않습니다.')

# 위 프로그램을 수정해서 패스워드가 일치하면 비밀번호가 일치합니다. 출력
# 일치하지 않으면 어떤 출력도 하지 마시오.(단, if~else구문을 사용할 것)

# 사용자 입력 코드
in_pass = int(input('비밀번호를 입력하세요. : '))

if in_pass == password :
    print('비밀번호가 일치합니다.')
else :
    # print('') #출력 위한 함수 실행 --- 좋은 코드는 아님
    pass # 아무것도 수행하지 않을 경우 pass