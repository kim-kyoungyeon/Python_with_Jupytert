#날짜계산 : timedelta() 함수 사용하여 날짜계산 date 객체사용
from datetime import date,datetime,timedelta
today = date.today() #오늘날짜 반환받기
print('오늘 : {0}'.format(today))
print('어제 : {0}'.format(today+timedelta(days=-1)))
print('내일: {0}'.format(today+timedelta(days=+1)))

#기준날짜 + DELTA일수

print("일주일전 : {0}".format(today+timedelta(days=-7)))
print("일주일후 : {0}".format(today+timedelta(days=+7)))
# 오늘 : 2020-07-21
# 어제 : 2020-07-20
# 내일: 2020-07-22
# 일주일전 : 2020-07-14
# 일주일후 : 2020-07-28
######################################################################################################
# 시간 계산

current_time =datetime.now()
print('현재시간: {0}'.format(current_time))
current_hour = current_time + timedelta(hours=-1)
print('한시간전: {0}'.format(current_hour))
current_d_hour = current_time + timedelta(days=1,hours=2)
print('1일2시간후 : {0}'.format(current_d_hour))
# 현재시간: 2020-07-21 11:23:50.109851
# 한시간전: 2020-07-21 10:23:50.109851
# 1일2시간후 : 2020-07-22 13:23:50.109851
##############################################################################
#날짜출력형식설정
#strftime()함수 날짜형식ㅇ르 문자여로 변환
today = datetime.today()
#대문자 y :4자리 소문자 y : 두자리의 연도표시
# H : 24시간제 I : 12시간제 p : am/pm 표시
print(today.strftime('%Y-%m-%d %H:%M:%S'))
#2020-07-21 11:23:50
print(today.strftime('%y-%m-%d %I:%M:%S %p'))
#20-07-21 11:25:16 AM














