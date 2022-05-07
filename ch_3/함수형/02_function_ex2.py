# Q. 다음의 함수를 포함하는 프로그램을 작성하시오.
# 함수이름 : show_info()
# 성명, 나이, 연락처 출력 : 임의의 값을 함수 내에서 출력

def show_info() :
    print('홍길동')
    print('20')
    print('010-1234-5678')

show_info() #함수 호출

# Q. 함수를 호출할 때 이름, 나이, 연락처를 전달하고 전달된 내용이 출력되는 함수로 수정하시오.

def show_info(name,age,tel):
    print(name)
    print(age)
    print(tel)

show_info('홍길동',20,'010-1234-5678')


