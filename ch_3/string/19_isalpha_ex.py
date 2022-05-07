# 그림과 같이 문장을 입력하고 알파벳, 숫자, 스페이스, 기타 개수 출력

string = input('문장을 입력하세요 : ')
# string = '나의 email 주소는 python777@naver.com 입니다!'

# 알파벳 : isalpha()
# 숫자 : isdigit()
# 스페이스 : isspace()
# 기타 : 위 검사에서 전부 False면

# 문자열은 반복문의 반복 범위로 사용 가능
# for c in string :
#     print(c)

# 한 문자씩 가져와서 문자, 숫자, 공백, 기타 판별 --- 해당 그룹에 계수(count)한다.
# count 변수 생성 및 초기화
alphas = digits = spaces = others = 0

for c in string : #string 변수에서 한글자씩 c에 대응
    if c.isalpha() :
        alphas += 1
    elif c.isdigit() :
        digits += 1
    elif c.isspace() :
        spaces += 1
    else :
        others += 1

print('문자 : %d 개' % alphas)
print('숫자 : %d 개' % digits)
print('스페이스 : %d 개' % spaces)
print('기타 : %d 개' % others)


