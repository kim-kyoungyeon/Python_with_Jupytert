#나의 email 주소는 python777@naver.com 입니다!
#알파벳,숫자,스페이스,기타 개수출력

#
# munza =input('문장을 입력하세요')
#if (munza.isalpha()) :
#   print(munza.count.isalpha())
# elif (munza.count.isdigit()) :
#     print(munza.isdigit())
# elif (munza.isspace()):
#     print(munza.isspace())
# else:
#     print('기타')
#
#
#정답

#알파벳 : isalpha
# 숫자 : isdigit
# 스페이스 :isspace
# 기타 개수 : 위 검사에서 전부 false면 개수
# 문자열은 반복문에 반복범위로 사용가능
#for c in string :
#    print(c)
#한문자씩 가져와서 문자,숫자,공백,기타를 판별, 해당 그룹에 계수 count한다
#count 변수 생성 및 초기화
string = input('문장입력해:')
string ='나의 email 주소는 python777@naver.com 입니다.!'
alphas = digits = spaces = others = 0 #문자를 개수 .. .
for c in string : #string 변수에서 한 글자씩 c에 대응
    if c .isalpha() :
        alphas += 1
    elif c.isdigit() :
        digits += 1
    elif c.isspace() :
        spaces += 1
    else :
        others += 1
print('문자: %d개'% alphas)
print('숫자: %d개'% digits)
print('공백: %d개'% spaces)
print('기타: %d개'% others)
















