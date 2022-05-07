# 구구단 출력
# 사용자로부터 단을 입력 받아서 사용자가 입력한 구구단 출력

dan = int(input('단을 입력하세요. : '))

for n in range(1,10) :
    print('%d * %d = %d' % (dan,n,dan*n))

