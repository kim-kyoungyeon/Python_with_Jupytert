#문자열포맷팅 : 형식에맞게 문자를출력하는방법
# 포매팅 방법
# 1. 포맷 코드 사용 :
print('이름 : %s ,총점 : %d , 평균 : %.2f '% ('홍길동',97,88.2))
# 2포맷함수 사용
print('당신의 BMI : ',format(25.2,'.2f'))
# 2-1 포맷 함수의 형식 -위치인덱스사용
name= '홍길동'
age = 23
print('이름 : {0}' .format(name))
print('이름 : {0}, 나이 : {1}' .format(name,age)) #{0}값에 name {1}값에 age 숫자로 인덱싱
#2-2 포맷 함수의 형식 - 인덱스 네임 = 값을 이용
print('{name}은 {age}살 입니다'.format(name='이몽룡',age = 22)) #변수명으로 인덱싱
