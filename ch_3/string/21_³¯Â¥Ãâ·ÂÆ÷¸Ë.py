# 날짜 출력 포맷 : format() 함수 사용
# 날짜와 시간을 처리하기 위해서는 datetime 모듈 import
from datetime import date, datetime

# 날찌 츨력 포맷
today = date.today() # 오늘 날짜 반환 --- 시스템 날짜 반환
year = today.year
month = today.month
day = today.day

print('오늘날짜 : {0}'.format(today))
print('연도: {0}'.format(year))
print('월: {0}'.format(month))
print('일: {0}'.format(day))

now = datetime.now()
print('now : {0}'.format(now))
# now : 2020-07-21 10:49:45.956683 --- 오늘 날짜와 현재 시간을 반환

# 시간만 추출
current_time = now.time
print(current_time)
# <built-in method time of datetime.datetime object at 0x01D10FC8> --- 파이썬이 사용하는 내장 시간 객체
current_time = now.time() # time() 함수 이용해서 볼 수 있는 형태로 변환 후 반환 받아야 함
# 10:53:30.372644

# now에서 시 분 초 각각 추출하기
now = datetime.now()

# 속성으로 접근 () 필요 없음
hour = now.hour
minute = now.minute
second = now.second
microsecond = now.microsecond

print('시 : ', hour)
print('분 : ', minute)
print('초 : ', second)
print('마이크로 초 : ', microsecond)
