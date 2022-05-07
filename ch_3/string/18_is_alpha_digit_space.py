# 문자의 요소 종류가 숫자인지, 글자인지, 숫자글자인지 등을 파악
# 결과를 True / False 로 반환
# isalpha() : 문자 여부 결과 반환
# isdigit() : 숫자 여부 결과 반환
# isspace() : 하나의 문자에 대해 공백 여부 결과 반환
# isalnum() : 문자 또는 숫자 여부 결과 반환

phone = input('전화번호 입력 (숫자만) : ')

if phone.isdigit() : # == True :
    pass
else :
    print('숫자만 입력하세요.')

#########################################
name = input('이름 입력 : ')

# 문자가 아닌 경우
if not(name.isalpha()) : #위 라인의 if ~ else 와 같은 결과지만 구조가 다르게 쓰여진 것
    print('문자만 입력하세요.')

#########################################
ID = input('ID 입력(ID는 문자와 숫자로 구성됩니다.) : ')

# ID 구성이 문자와 숫자인지 확인
if not(ID.isalnum()) :
    print('숫자와 문자만 사용할 수 있습니다.')

#########################################
# 한 개의 문자에 대해서 공백인지 확인 --- 공백 아닌 다른 글자가 한 개라도 있으면 False, 공백 여러개 있으면 True
print('  '.isspace()) #True
# 두 개 이상의 문자에 대해서는 확인 불가
print('    c'.isspace()) #False