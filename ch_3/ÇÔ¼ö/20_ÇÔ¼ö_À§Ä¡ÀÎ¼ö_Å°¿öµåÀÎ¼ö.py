# 위치 인수 (일반적인 인수)
# 함수 호출 시 위치에 의하여 구별하는 방식
# 매개변수 순서대로 인수를 전달하여 사용하는 경우
# 순서대로 전달

# def add(a,b,c) :
# 호출 : add(10,20,30) a=10 b=20 c=30이 저장됨

# 키워드 인수
# 인수들 앞에 키워드를 두어서 인수를 구별하는 방식
# 인수의 위치가 매개변수의 위치와 달라도 됨
# def add(a,b,c) :
# 호출 : add(c=30,a=10,b=20)

# 주의 !
# 위치 인수와 키워드 인수를 섰어서 사용해도 되지만, 위치 인수를 키워드 인수보다 앞에 둬야 한다.
# add(10, c=30, b=20) : 에러 없음
# add(c=30, 20, 10) : 에러 발생

def student_info(name,age,gender) :
    print('이름 : ',name)
    print('나이 : ',age)
    print('성별 : ',gender)

student_info(name='kim',age=23, gender='여')
student_info('lee',gender='남',age=22)
# student_info(gender='남',age=22,'lee') #에러 발생