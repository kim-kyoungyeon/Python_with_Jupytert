# Q. 노래방 기계 : 1곡에 2000원
# 현재 잔액 : 10000원

# 노래를 몇 곡 불렀는지 표시하고 잔액을 표시하시오.
# 필요변수 생성
song = 2000 #노래 한곡
money = 10000 #현재 잔액
count = 0 #현재 곡 수

while True :
    money = money - song
    count += 1
    print('노래를 '+str(count)+'곡 불렀습니다.')

    if money == 0 : # 잔액이 없으면
        print('잔액이 없습니다. 종료합니다.')
        break
    else :
        print('현재 '+str(money)+'원 남았습니다.')

## Tip !
# while True:
# while 1 :
# while money : 전부 무한루프
# 단, money의 값이 0이면 money는 False로 처리

# 프로그래밍에서 0은 False, 0이 아닌 값은 True로 간주
