# 다중 for 문
# 안쪽 for문을 먼저 실행하고 바깥쪽 for문을 실행한다.

for y in range(3) :
    for x in range(5) :
        print(x,end=' ') # 15번 반복
    print() # y에 걸리게 된다. 3번 반복