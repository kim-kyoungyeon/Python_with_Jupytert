# 도형 선택해서 면적 구하기
# shape = int(input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) :'))
#
# if shape == 1 :
#     sv = int(input('가로 입력 : '))
#     sh = int(input('세로 입력 : '))
#     print('사각형의 면적 = %.2f' % sv*sh)
# elif shape == 2 :
#     tv = int(input('밑변 입력 : '))
#     th = int(input('높이 입력 : '))
#     print('삼각형의 면적 = %.2f' % (tv*th/2))
# else :
#     ch = input('반지름 입력 : ')
#     print('원의 면적 %.2f '% ch)

#=========================풀이============================
# 도형의 종류 입력 받기
choice = input('도형 입력(1: 사각형, 2: 삼각형, 3: 원) : ')
shape = ''
area = ''
# 문장 바깥에서 선언하는 변수 : 암묵적으로 프로그램 코드 본격적으로 나오기 전 반복적으로 이용되고, 공통되는 변수임을 알리는

# 도형 판단 후 계산 완료 후에 출력

# 도형 종류에 따라서 계산에 필요한 데이터 입력 후 면적 계산코드
if choice == '1' :
    # 사각형 가로 세로 입력 후 계산
    w = int(input('가로 입력 : '))
    h = int(input('세로 입력 : '))
    area = w * h
    shape = '사각형'
elif choice == '2' :
    # 삼각형 밑변 높이 입력 후 계산
    b = int(input('밑변 입력 : '))
    h = int(input('높이 입력 : '))
    area = b * h / 2
    shape = '삼각형'
else :
    # 원의 반지름 입력 후 계산
    r = int(input('반지름 입력 : '))
    area = 3.141592 * r * r
    shape = '원'

print('%s의 면적 = %.2f' % (shape,area))