# 다음과 같이 가위바위보 게임 작성
# hgd = input('홍길동 입력 : ')
# lmr = input('이몽룡 입력 : ')
# =
# 가위 보
# 가위 바위
# 보 바위
#
#
# if hgd != lmr and hgd == '가위' and lmr == '보' :
#     print('홍길동이 이겼습니다.')

#================ 풀이 ===================
# 가위바위보 게임
# 사용자는 가위바위 보 중에 하나의 값을 입력한다고 전제한다.
# 사용자 값 입력 받기
hong = input('홍길동 입력 : ')
lee = input('이몽룡 입력 : ')

# 승자 판단
# 홍길동이 이기는 모든 경우의 수
if hong == '가위' and lee == '보' or hong == '바위' and lee == '가위' or  hong == '보' and lee == '바위' :
    print('홍길동이 이겼습니다.')
elif hong == lee :
    print('비겼습니다.')
else :
    print('이몽룡이 이겼습니다.')





