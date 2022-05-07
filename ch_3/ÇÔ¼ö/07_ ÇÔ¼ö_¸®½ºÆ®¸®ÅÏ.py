# 함수의 반환값은 모든 형태 가능
# 리스트 형태로 반환도 가능

# 사용자로부터 회원 이름을 입력받아서 리스트에 저장한 후에 명단 리스트를 반환하는 함수 정의 후 실행 결과를 보이시오.
def get_names() :
    names = []

    for i in range(3) :
        name = input('회원 이름 입력 : ')
        names.append(name)

    return names

name_list = get_names()
print(name_list)
print(type(name_list)) # <class 'list'>
