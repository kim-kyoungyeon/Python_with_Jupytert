#리스트원소삭제_연습.py
##리스트에 있는 원소를 삭제하는 프로그램
# 기능 1 : 원소 중 사용자로 부터 입력받은
#값에 해당하는 원소를 삭제
# 기능 2 : 리스트의 마지막 원소를 삭제
# 기능 3 : 사용자가 선택한 위치를 삭제
#리스트는 미리 준비 한다.
# 종료시 while true 종료조건 임의로 만들어야한다

list_a=[1,2,3,5,5,5,6,7,8,2,2,4,6]

print("1. 마지막 원소 삭제\n"
      "2. 입력한 값의 원소 삭제\n"
      "3. 선택한 위치의 원소를 삭제\n"
      "위 리스트에서 원소를 삭제할 수 있습니다.")
sel = input("삭제 방법을 선택하세요.")
while True:
    if sel == 1 :
        print()
        int(input("1. 마지막 원소 삭제"))
        del list_a[12:]
    elif sel ==2 :
        print("2. 입력한 값의 원소 삭제")
        i =int(input("삭제할 값을 입력하세요.삭제할 값은 입력하세요. 입력된 값은 모두 삭제 됩니다"))
        if i.isdigit() :
            i = int(i)
        list_a.remove('i')
    else:
        d= int(input("3. 선택한 위치의 원소를 삭제"))
        d =int(input("리스트의 첫번째 원소의 위치값은 %s 입니다."%list_a[0],
                     "\n 삭제할 위치를 입력하세요."))
        list_a.remove(d, list_a)
        break

print()
print(list_a)
print()
#위 리스트에서 원소를 삭제할 수 있습니다.
#1. 마지막 원소 삭제
#2. 입력한 값의 원소 삭제
#3. 선택한 위치의 원소를 삭제
#삭제 방법을 선택하세요.1

#출력
#작업 후 리스트
#[1,2,3,5,5,5,6,7,8,2,2,4]

#입출력예시 2
#[1,2,3,5,5,5,6,7,8,2,2,4,6]
#위 리스트에서 원소를 삭제할 수 있습니다.
#1. 마지막 원소 삭제
#2. 입력한 값의 원소 삭제
#3. 선택한 위치의 원소를 삭제
#삭제 방법을 선택하세요.2

#삭제할 값을 입력하세요.삭제할 값은 입력하세요. 입력된 값은 모두 삭제 됩니다.5

#출력
#작업 후 리스트
#[1,2,3,6,7,8,2,2,4,6]

#입출력예시 3
#[1,2,3,5,5,5,6,7,8,2,2,4,6]
#위 리스트에서 원소를 삭제할 수 있습니다.
#1. 마지막 원소 삭제
#2. 입력한 값의 원소 삭제
#3. 선택한 위치의 원소를 삭제
#삭제 방법을 선택하세요.3

#리스트의 첫번째 원소의 위치값은 0 입니다.
#삭제할 위치를 입력하세요.1


#출력
#작업 후 리스트
#[1,3,5,5,5,6,7,8,2,2,4,6]
#



















