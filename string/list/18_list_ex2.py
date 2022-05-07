#빈리스트 생성
data_list=[]

print('목록에 데이터 삽입')
print('목록에 삽입할 데이터 중 모두 숫자로 되어있으면 수치형 데이터로 입력합니다')
print('다른형태의 데이터는 모두 숫자형 데이터로입력됩니다')

while True :
    print('=====================================================')
    print('현재 데이터 목록 :',data_list)
    print('\n 위목록에 다음과 같이 원소를삽입할수있습니다')
    print('1. 마지막 원소삽입')
    print('2. 입력한 위치에 원소삽입')
    print('- 종료는 입력 없이 ENTER')
    print("--------------------------------------------------------------------")

    sel = input('삽입방법을 선택하세요:')

    if sel == '1' or sel=='2' :
        data = input('삽입할 데이터를 입력하세요:')
        if data.isdigit() : #입력데이터가 모두 숫자일경우 수치로 변환
            data=int(data)
        # 1번 선택 :append () 마지막에 데이터 추가
        # 2번이면 insert
        if sel == '1' :
            data_list.append(data)
        else :
            # insert 이용해서 원하는 위치에 데이터 추가
            idx = int(input('삽입할 위치는 0부터 시작하고 목록범위를 벗어나면 마지막에 삽입됩니다.\n'
                            '삽입위치입력 : '))
            data_list.insert(idx,data)
    elif sel == '':
        print('종료합니다')
        break
    else :
        print('잘못입력하였습니다')


































