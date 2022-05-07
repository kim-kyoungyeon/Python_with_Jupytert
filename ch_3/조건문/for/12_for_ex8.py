# 다중 for문을 사용하여 다음과 같이 출력
# Q. 1부터 12까지 4x3 행렬로 출력하시오.
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

a = 0
for y in range(3) :
    for x in range(4) : # x,y 변수는 출력 횟수를 결정
        a += 1 # a 변수는 출력 데이터 값을 결정
        print(a,end='\t') # '\t' 정렬
    print()
