# 정수 : int
num = 100
print('num : ',type(num))

# 실수 : float
PI = 3.14
print('PI : ',type(PI))

# 문자열 : str
# 문자형을 숫자형으로 형 변환이 가능하지만 값 모양에 따라서 불가능할 수도 있음
name = '홍길동' # 형 변환 불가능
price = '1000' # 숫자형 변경 가능
grade = 'A'
print(type(name),type(price),type(grade))

# 논리형 : bool
done = True
print('done : ', type(done))

# 파이썬에서 변수는 지정된 자료형이 없음(가변 자료형)
# 저장한 값에 따라 변수 자료형이 지정

a = 100 # 정수형 변수
a = "hello" # 문자열형 변수