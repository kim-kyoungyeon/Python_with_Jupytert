g_a = 3 #함수 밖에서 정의된 전역변수 g_a
a = 1
b = 1

def add1() :
    global a #전역변수 a를 함수 내에서 사용하겠다! a 이름을 지역변수는 생성하지 않음
    a = 3
    c = a+b
    g_a = 1
    print('함수 : ',g_a) #지역변수
    print('함수 a : ',a) #지역변수
    print('함수 : ',b) #전역변수

add1()
print(g_a) #전역변수
print('외부 a :',a) #전역변수
print(b) #전역변수