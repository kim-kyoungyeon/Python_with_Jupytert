# choice ==
# num1 = '바위', '가위', '보'
# num2 = '바위', '가위', '보'
# name = '홍길동','이몽룡'
# cal = '바위 > 가위, 바위 = 바위,바위 <보,가위 > 보,가위 =가위,보 = 보'
#
# a<-print('홍길동 입력: '% num1 )
# b<-print('이몽룡 입력: '% num2 )
#
# if a>b :
#     print(' %s 가 이겼습니다. ' %a)
# elif a<b :
#     print('%s가 이겼습니다' %b)
# else a=b:
#     print('비겼습니다.' ))

## 가위비위보 게임
#사용자에는 가위바위보중 하나의 값]을 입력한다
#사용자값입받기
hong = input('홍길동 입력 :')
lee = input('이몽룡 입력 : ')
# 홍길동이 이기는 경우의 수

if hong == '가위' and lee =='보' or\
hong == '바위' and lee == '가위'or\
hong == '보' and lee == '바위' :
    print('홍길동이 이겼습니다.')
elif hong == lee :
    print('비겼습니다.')
else:
    print('이몽룡이 이겼습니다.')
