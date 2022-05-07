# 날짜 계산 : timedelta() 함수 사용하여 날짜 계산(date 객체 사용)

from datetime import date, datetime, timedelta

today = date.today() #오늘 날짜 반환 받기
print('오늘 : {0}'.format(today))
print('어제 : {0}'.format(today+timedelta(days=-1)))
# 기준날짜 + delta 일수
print('내일 : {0}'.format(today+timedelta(days=+1)))

print('일주일 전 : {0}'.format(today+timedelta(days=-7)))
print('일주일 후 : {0}'.format(today+timedelta(days=+7)))

##############################################################
# 시간 계산 : timedelta() 함수 사용

current_time = datetime.now()
print('현재시간 : {0}'.format(current_time))
current_hour = current_time + timedelta(hours=-1)
print('한 시간 전 : {0}'.format(current_hour))
current_d_h = current_time + timedelta(days=1,hours=2)
print('1일 2시간 후 : {0}'.format(current_d_h))

##############################################################
# 날짜 출력 형식 설정
# strftime() 함수 : 날짜형식을 문자열로 변환
today = datetime.today()

# 대문자 Y : 4자리, 소문자 y : 2자리의 연도 표시
# H : 24시간제, I : 12시간제, p : AM, PM 표시
print(today.strftime('%Y-%m-%d %H:%M:%S'))
# 2020-07-21 11:23:51
print(today.strftime('%y-%m-%d %I:%M:%S %p'))
# 20-07-21 11:25:03 AM