# 정수 리터럴
a = 0b1010 # 2진수
b = 300 # 10진수
c = 0o123 # 8진수
d = 0x12fc # 16진수
print(a,b,c,d) # 변수값 저장할 때 2진수 8진수 16진수로 저장해도 print() 함수는 10진수로 변환해서 출력

#-----------------------------------------------------
# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234567e5
print(f1,f2,f3)

#------------------------------------------------------
# 문자열 리터럴
char1 = 'A'
char2 = "B"
print(char1,char2)

str1 = '홍길동'
str2 = "python"
str3 = """Python Programming"""
str3 = '''Python Programming'''

str4 = '''삼 따옴표는
여러줄에 나누어서
문자를 저장할 떄 사용''' # enter까지 문자열로 저장

print(str4)

# 논리값 리터럴
t = True
f = False

print(t,f)

# 특수 리터럴
# None

address = None
print(address)
print(type(address))
# <class 'NoneType'>


