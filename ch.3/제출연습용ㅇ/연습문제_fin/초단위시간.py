#초 단위의 시간을 받아서
#몇일 몇시 몇분 몇초인지 계산하는 프로그램을
#작성하시오.
#입력 ex
#초를 입력하세요. :

#출력 ex
# x일 x 시 x 분 x 초 입니다.


#동전 계산과 똑같은 로직
# 1일 : 86400초
# 1시간 : 3600초
# 1분 : 60초
cho = int(input('초를 입력 하세요.'))

day= cho//66400
remainder = cho % 86400

hour = remainder//3600
remainder = remainder %3600

minute= remainder // 60
second =remainder %60
print("%d초 : %d 일 %d시 %d분 %d초" %(cho,day,hour,minute,second) )