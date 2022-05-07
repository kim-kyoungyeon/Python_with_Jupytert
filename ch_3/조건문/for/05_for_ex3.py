# Q. 정수 2개를 입력 받아서 두수 사이의 합을 구하는 프로그램 작성(for 문 사용)

num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))

sumx = 0

for x in range(num1,num2+1) :
    sumx += x

print('%d부터 %d까지의 합 : %d' % (num1,num2,sumx))