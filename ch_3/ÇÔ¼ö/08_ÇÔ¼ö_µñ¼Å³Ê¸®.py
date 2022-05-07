# 사용자에게 이름과 나이를 입력받아 딕셔너리로 구성 후 반환하는 함수 get_info() 정의
def get_info() :
    info = {}
    name = input('회원 이름 입력 : ')
    age = input('회원 나이 입력 : ')
    info = {'name':name, 'age':age}
    # info['name'] = name
    # info['age' = age

    return info

std_info = get_info()
print(std_info)
print(type(std_info)) # <class 'dict'>









