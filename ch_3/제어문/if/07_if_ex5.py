# obj = int(input('도형 입력 (1: 사각형, 2: 삼각형, 3 : 원): '))
# if obj == 1 :
#     num1 = float(input('가로 입력 : '))
#     num2 = float(input('세로 입력 : '))
#     wid = num1 * num2
#     print('사각형의 면적 = %.2f ' % wid)
#
# elif obj == 2:
#     num1 = float(input('가로 입력 : '))
#     num2 = float(input('세로 입력 : '))
#     wid =  num1 * num2 /2
#     print('삼각형의 면적 = %.2f ' % wid)
# else:
#     num1 = float(input('가로 입력 : '))
#     wid = num1**2 *3.1416
#     print('원 면적 = %.2f ' % wid)
####################w정답
#도형의 종류 입력
choice = input('도형입력(1: 사각 2: 삼각 3 :원 )')
shape = ''
area = ''
# 프로그램 내에서 공통적/반복적으로 사용되는 변수 선언
#무조건 선언할 필요는 없다

# 도형 판단후 계산 완료 후에 출력

#도형 종류에 따라 계산에 필요한 데이터 입력후 면적계산코드

if choice == '1' :
    # int 안해놔서 문자열과 숫자비교
    #사각형 가로 세로 입력 후 계산
    w= int(input("가로입력"))
    h = int(input("세로입력"))
    area = w * h
    shape = '사각형'
elif choice == '2' :
    b = int(input("밑변입력"))
    h = int(input("높이입력"))
    area = b * h /2
    shape = '삼각형'
    # 삼각형 밑변높이 입력 후 계산
else :
    r=int(input('반지름 입력: '))
    area = 3.141592*r*r
    shape = '원'
    #원의 반지름 읿력후 계싼
print('%s의 면적 = %.2f' % (shape,area))














