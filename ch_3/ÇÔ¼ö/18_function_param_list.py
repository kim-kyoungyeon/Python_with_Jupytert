# 함수에 리스트 전달

# 사용자로부터 회원 명단을 전달받아 명단을 출력하는 함수 정의
def show_name(names) :
    for name in names :
        print(name,end=' ')

names_list = ['kim','lee','park']
show_name(names_list)

#--------------------------------------------------------
# 함수에 딕셔너리 전달
def show_info(info) :
    print(info) #딕셔너리 전체 출력
    print('이름 : '+info['name'])

info_dict = {'name':'kim','age':23,'phone':'01012345678'}
show_info(info_dict)

