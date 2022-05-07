# 문자열 포맷팅 : 형식에 맞게 문자를 출력하는 방법
# 포맷팅 방법
#1. 포맷 코드 사용 : %s, %d, %f, %c
print('이름 : %s, 총점 : %d, 평균 : %.2f' % ('홍길동',97,88.2))
#2. 포맷 함수 사용 :
print('당신의 BMI : ',format(25.2,'.2f'))

#2_1. 포맷함수의 형식 --- 위치 인덱스 사용 {0}
name = '홍길동'
age = 23
print('이름 : {0}'.format(name))
print('이름 : {0}, 나이 : {1}'.format(name,age))

#2_2. 포맷함수의 형식 --- 인덱스네임 = 값 을 이용
print('{name}은 {age}살 입니다.'.format(name='이몽룡',age=22))

