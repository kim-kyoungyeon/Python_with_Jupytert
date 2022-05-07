#초 단위의 시간을 받아서
#몇일 몇시 몇분 몇초인지 계산하는 프로그램을
#작성하시오.
#입력 ex
#초를 입력하세요. :

#출력 ex
# x일 x 시 x 분 x 초 입니다.

# 내가 푼 것
long = int(input('초를 입력하세요. :'))
day = long // (24*60**2)
rest1 = long % (24*60**2)
hour = rest1 // (60**2)
rest2 = rest1 % (60**2)
minutes = rest2 // 60
seconds = rest2 % 60

print('%d일 %d시 %d분 %d초'%(day,hour,minutes,seconds))

#===풀이===#
# 1일은 86400초
# 1시간 3600초
# 1분 60초

cho = int(input('초를 입력하세요. '))
day = cho // 86400
remainder = cho % 86400

hour2 = remainder // 3600
remainder = remainder % 3600 #remainder %= 3600

minute = remainder // 60
second = remainder % 60

print('%d 초 : %d 일 %d 시 %d 분 %d 초'%(cho,day,hour,minute,second))