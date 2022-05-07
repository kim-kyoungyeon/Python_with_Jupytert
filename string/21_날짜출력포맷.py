#날짜출력포맷:format 함수 사용
#날짜와 시간을 처리하기위해
#datetime 모듈 import
from datetime import date,datetime


#날짜출력포맷
today = date.today()#오늘날짜 반환
year= today.year
month = today. month
day =  today.day
print('오늘날짜: {0}'.format(today))
print('연도:{0}'.format(year))
print('월:{0}'.format(month))
print('일:{0}'.format(day))

now =datetime.now()
print('now:{0}'.format(now))
#now:2020-07-21 10:49:46.351149
#오늘날짜와 현재시간을 반환

#시간만 추출
#current_time = now.time
#print(current_time)
#<built-in method time of datetime.datetime object at 0x014C0FC8>- 파이썬이 사용하는 내장 시간객체
current_time = now.time()
print(current_time)
#10:54:27.825584

#함수를 이용하여 볼 수있는 형태로 변환 후 반환 받아야 함
#now 에서 시분초 각각 추출
now = datetime.now()

hour = now.hour
minute = now.minute
second= now.second
microsecond= now.microsecond
#속성
print('시 :' , hour)
print('분 :' , minute)
print('초 :' , second)
print('마이크로초 :' , microsecond)




































































