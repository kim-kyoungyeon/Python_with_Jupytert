# 0부터 10까지의 합계를 구하시오.
# 누적합 변수가 필요
# 0+1+2+3+...+10

sumx = 0 #누적합에 사용할 변수
# 미리 선언하지 않으면 NameError 발생

for x in range(11) :
    print(x)
    sumx = sumx + x
print('sumx = ',sumx)

