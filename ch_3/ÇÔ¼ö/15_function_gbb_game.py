# Q. 가위 바위 보 게임 함수 작성
# 함수명 : gbb_game()
# 랜덤으로 COM 숫자를 생성해서 --- 함수 내에서
# 전달받은 YOU 숫자와 비교하여 --- 매개변수
# 결과 출력 --- 함수 내에서(리턴값이 없음)
# 1:가위, 2:바위, 3:보
# COM이 이기는 경우 :
# COM  YOU  차이
#  1    3    -2
#  2    1     1
#  3    2     1

from random import randint

# def gbb_game(you_n) :
#     COM = randint(1,3)
#     if COM == 1 and YOU == 3 or COM == 2 and YOU == 1 or COM == 3 and YOU == 2:
#         print('컴퓨터가 이겼습니다.')
#         print('COM : %d' % COM)
#     elif COM == YOU :
#         print('비겼습니다.')
#         print('COM : %d' % COM)
#     else :
#         print('당신이 이겼습니다.')
#         print('COM : %d' % COM)
#
# YOU = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
#
# gbb_game(YOU)

### 풀이 ###
# 1:가위, 2:바위, 3:보
# COM이 이기는 경우 :
# COM  YOU  차이
#  1    3    -2
#  2    1     1
#  3    2     1

def gbb_game(you_n) :
    com_n =randint(1,3)
    if com_n - you_n == 1  or com_n - you_n == 2 :
        print('컴퓨터가 이겼습니다.')
    elif com_n == you_n :
        print('비겼습니다.')
    else :
        print('당신이 이겼습니다.')
    print('COM : %d' % com_n)

you = int(input('YOU 입력 (1:가위, 2:바위, 3:보) : '))
gbb_game(you)


