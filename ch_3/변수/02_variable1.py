#문자열에 큰따옴표 사용
name = '홍길동'
age=23

print(name,age)# ,로 변수를 연결하면 2개의 변수내용이 옆으로 출력된다

address='서울 강남구'
print(name + "은" +address+"에 삽니다.")
#문자열 "", '' 모두 사용가능
# 문자열 변수와 문자열 값을 연결하기 위해서는  + 를 사용한다
# 파이썬은 파일 단위로 일괄실행시킨다. 가급적 콘솔 실행은 하지 말것.
# 문자열 변수와 값을 연결시 값이 숫자면 + 값 사용 불가
# 문자열 데이터를 연결할 때문에만 + 사용 가능

print(name + "은" + address + "에 삽니다. ")

print(name + "은" + age + '살 입니다') # age 숫자변수 #에러남
#TypeError: can only concatenate str (not "int") to str
#-error
print(name + "은" + str(age) + '살입니다.') #age 형변환

# 형변환
# 값의 형태를 강제적으로 다른 형태로 변환하는 것
# int -> str , str-> float

# 문자열 형변환 함수 str
#정수형 형변환 함수 int
#실수형 형변환 함수 float











