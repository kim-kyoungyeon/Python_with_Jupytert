# Q. 다음의 함수를 포함하는 프로그램 작성
# 함수 이름 : get_area() #매개변수는 없는 함수로 작성
# 사각형의 가로길이와 세로길이를 입력받아 면적을 구하여 반환 후 사각형의 면적을 출력

def get_area() :
    width = int(input('가로길이 입력 : '))
    height = int(input('세로길이 입력 : '))
    area = (width*height)
    return area

rec_area = get_area()
print('사각형의 넓이 : %d'%rec_area)