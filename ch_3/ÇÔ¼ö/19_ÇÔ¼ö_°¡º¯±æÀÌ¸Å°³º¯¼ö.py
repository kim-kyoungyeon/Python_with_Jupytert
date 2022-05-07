# 가변길이 매개 변수
# 1개의 매개변수로 설정
# 개수가 정해지지 않은 여러개의 값을 전달받을 때 사용하는 매개변수

# *args : 인수 값을 받음 (여러개의 값을 전달받음)
# **kwargs : 키 = 값 의 형태로 인수를 전달받음

# *args 사용 함수
def show(*players) :
    for player in players :
        print(player,end=' ')
    print()

show('홍길동')
show('홍길동','이몽룡')
show('홍길동','이몽룡','변학도')

# 가변길이 매개변수 예제
def order_coffee(coffee,*options) :
    print(coffee+'옵션: ',end=' ')

    for opt in options :
        print(opt, end=' ')
    print()

order_coffee('아메리카노','Tall','HOT','시럽','stay')
order_coffee('까페라떼','Grande','ICE','go')

#--------------------------------------------------------
# 가변길이 매개변수 **kwargs
# keyword arguments의 약자, key=value 값을 받음
# 매개변수는 dict 형태로 생성됨

def show_keywards(**kewargs) :
    print('딕셔너리 형태로 전달됩니다.------------------')
    for key in kewargs.keys() :
        print(key,end=' ')
    print('\n')
    for value in kewargs.values() :
        print(value, end = ' ')
    print('\n')
    for item in kewargs.items() :
        print(item)


show_keywards(id='sun',
              name='kim',
              phone='010-1234-5678')
show_keywards(id='moon',
              name='lee',
              phone='010-1234-5678',
              address='제주도 서귀포시')
