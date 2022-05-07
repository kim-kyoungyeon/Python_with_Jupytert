# 정수 리터럴
a = 0b1010 # 2진수
b = 300
c=0o123 # 8진수
d=0x12fc # 16진수
print(a,b,c,d)# 변수값 저장시 2진수 8진수 16진수로 저장해도
# 결국 print 함수는 10진수로 변환해서 출력
# -------------
#실수리터럴

f1 = 3.14
f2 = -123.45
f3=1.234567e5

print(f1,f2,f3)

#문자열 리터럴
char1 = 'a'
char2 = 'b'
print(char1,char2)
str1 = '홍길동'
str2 ="python"
str3 = """python  programming"""
str3 = '''python  programming'''

str4 = '''삼따옴표는
여러줄에 나누어줄때
문자열을 저장할때 사용''' #enter까지 문자열로 저장

print(str4)
# 논리값 리터러
t =True
f=False
print(t,f)

#특수리터럴
#None
address=None
sprint(address)
print(type(address))
# None
# <class 'NoneType'>



































































































