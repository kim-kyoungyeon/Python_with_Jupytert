# in / not in
# 문자열 안에 특정 문자열이 포함되어 있는지 확인 후 결과를 반환하는 연산자
# True / False를 반환

string = 'Python programming'

print('Python' in string) # True
print('Programming' in string) # False --- 대소문자 구별해서 연산

if 'python' in string :
    print('있음')
else :
    print('없음') # '없음' 출력 --- 대소문자 구별
