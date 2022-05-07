# 2단부터 9단까지 구구단 전부 출력
for dan in range(2,10) :
    for n in range(1,10) :
        print('%d * %d = %d' % (dan,n,dan*n))
    print('----------------------')