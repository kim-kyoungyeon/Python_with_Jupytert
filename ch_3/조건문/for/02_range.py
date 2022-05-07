# range() 함수
# 특정 범위의 정수 생성
# range(10) : 0~9까지의 정수(10개/시작은 0)

# range(start,stop) : start에서 stop-1까지의 정수
# range(0,10) : 0~9까지의 정수

# range(start,stop,step) : start에서 stop-1까지 step 간격으로 정수 생성
# range(0,10,2) : 0~9까지 2씩 증가하면서 10보다 작은 정수

# range(10,0,-2) : 10부터 -1까지 2씩 감소하면서 정수 생성  --- 감소 step 사용 가능

for i in range(10) :
    print(i) #0~9까지의 정수

for i in range(11,21) :
    print(i) #11~20까지의 정수

for i in range(0,10,2) :
    print(i) #0부터 9까지 2씩 증가 정수 생성

for i in range(10,0,-2) :
    print(i) #10부터 -1까지 -2씩 감소 정수 생성