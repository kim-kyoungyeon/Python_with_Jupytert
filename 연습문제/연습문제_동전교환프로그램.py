#동전교환프로그램
#입력한 값은 얼마든지 모두 동전으로 교환하지만
#동전의 개 수를 최소화 하여 교환하는 프로그램

#입력예시
#교환할 돈은 얼마입니까?

#출력예시
#오백원짜리 ===>
#백원짜리 ===>
#오십원짜리 ===>
#십원짜리===>
#일원짜리 ===>


#내가 푼 것
money = int(input('교환할 돈은 얼마입니까?'))
fivehundred = money // 500
change1 = money % 500
hundred = change1 // 100
change2 = change1 % 100
fifty = change2 // 50
change3 = change2 % 50
ten = change3 // 10
one = change3 % 10

print('오백원짜리 ===> %d' % fivehundred,'\n',
      '백원짜리 ===> %d' % hundred,'\n',
      '오십원짜리 ===> %d' % fifty,'\n',
      '십원짜리===> %d' % ten,'\n',
      '일원짜리 ===> %d' % one,'\n')

#===풀이===#

# 필요 변수 선언 부분
money, c500, c100, c50, c0 = 0,0,0,0,0

# 사용자 입력값
money = int(input('교환할 돈은 얼마입니까? : '))

# 500원짜리 동전 교환
c500 = money // 500

# 500원 동전 교환 후 남은 금액 계산
remain = money % 500

# 100원짜리 동전 교환
c100 = remain // 100

# 100원 동전 교환 후 남은 금액 계산
reamin = remain % 100 # remain %= 100

# 50원짜리 동전 교환
c50 = remain // 50

# 50원 동전 교환 후 남은 금액
remain %= 50

# 10원짜리 동전 교환
c10 = remain // 10

# 10원짜리 교환 후 남은 금액(1원짜리)
remain %= 10

print('500원짜리 ==> %d 개' % c500)
print('100원짜리 ==> %d 개' % c100)
print('50원짜리 ==> %d 개' % c50)
print('10원짜리 ==> %d 개' % c10)
print('1원짜리 ==> %d 개' % remain)