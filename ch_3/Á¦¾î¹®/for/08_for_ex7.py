# 사용자가 입력한 이름이 다음과 같은 명단에 있는지 확인하고 결과를 출력하는 프로그램
# 명단 : ['홍길동','이몽룡','성춘향','변학도']

search_name = input('이름 입력 : ')

for name in ['홍길동','이몽룡','성춘향','변학도'] :
    if search_name == name :
        find = True
        break #반복을 종료하고 반복문 탈출하는 문장
    else :
        find = False

# find 변수 값을 확인해서 명단에 있는지 결과 출력
if find :
    print('명단에 있습니다.')
else:
    print('명단에 없습니다.')

#tip! 결과 출력은 반복이 종료된 후에 find 변수에 따라 출력해야 함. 반복 도중에 출력하게 될 경우 출력 반복적으로 일어날 수 있음.
