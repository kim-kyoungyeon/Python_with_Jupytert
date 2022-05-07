#빈 리스트 생성
data_list = []

print("목록에 데이터 삽입")
print("목록에 삽입할 데이터 중 모두 숫자로 되어 있으면 수치형 데이터로 입력합니다.")
print("다른 형태의 데이터는 모두 숫자형 데이터로 입력됩니다.")

while True :
    print("---------------------------")
    print("현재 데이터 목록 : ", data_list)
    print("\n위 목록에 다음과 같이 원소를 삽입할 수 있습니다.")
    print("1. 마지막에 원소 삽입")
    print("2. 입력한 위치에 원소 삽입")
    print("- 종료는 입력 없이 ENTER")
    print("-------------------------------------------")

    sel = input("삽입방법을 선택하세요 : ")

    if sel == "1" or sel =="2" :
        data = input("삽입할 데이터를 입력하세요. : ")
        if data.isdigit() : #입력 data가 모두 숫자일 경우 수치로 변환
            data = int(data)
# 중첩if는 좋은코드가아니다. data가 1/2에 중복으로 걸려있음

        #1번이면 append() 마지막에 데이터 추가
        if sel == "1" :
            data_list.append(data)
        else :
            #insert() 원하는 위치에 데이터 추가
            idx = int(input("삽입할 위치는 0부터 시작하고 목록 범위를 벗어나면 마지막에 삽입됩니다.\n"
                            "삽입 위치 입력 : "))
            data_list.insert(idx,data)

    elif sel == "" :
        print("종료합니다.")
        break
    else :
        print("잘못 입력 하였습니다.")





