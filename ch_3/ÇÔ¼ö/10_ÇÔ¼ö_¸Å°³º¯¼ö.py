# 매개변수
# 함수로 전달되는 값을 받는 변수(함수 정의에서 나타남)

# 인수(인자)
# 함수에게 실제로 전달되는 값(함수 호출 시 나타남)

def show_name(name) :
    print(name)

show_name('홍길동')

# Q. 사용자에게 국어, 영어, 수학 점수를 입력받아서 평균을 구한 후 출력하시오.
# 단, 평균은 함수 get_average() 정의한 후 함수를 호출해서 계산할 것

# 평균을 계산하는 함수
def get_average(k,e,m) :
    return (k+e+m)/3

kor = int(input('국어점수 : '))
eng = int(input('영어점수 : '))
mat = int(input('수학점수 : '))

print('평균 : %.2f ' % get_average(kor,eng,mat))









