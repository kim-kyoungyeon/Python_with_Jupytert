# 포맷코드
# print()에서 문자열과 변수를 함께 출력할 때
# 방법 1
# print("문자열",변수) ,로 나열하는 방법

# 방법 2 : 포맷코드 사용 방법
# print("서식" % 값)
# print("문자열 %d 문자열" % 변수)
# "" 안에 있는 포맷코드 위치에 뒤의 변수값이 매칭
# %d : 정수형을 의미

age = 10
name = "apple"
print("나이 : %d 살" % age)
print("내 이름은 %s 입니다." % name)

# 포맷코드 정리
# %s 문자열(string)
# %c 문자 1개(character)
# %d 정수(integer)
# %f 부동 소수(floating-point)
# %o 8진수
# %x 16진수
# %% % 자체


# %c는 1문자
grade = "A"
average = 93.5

#--- 포맷코드 사용 출력
print("학점 : %c" % grade)
print("학점 : %s" % grade)
# print("학점 : %c" % name) # error -- 두 글자 이상은 %c 사용 불가
# TypeError: %c requires int or char
print("학점 : %c" % 24) # 한문자여도 %s에 해당하는 문자열 처리 가능
print("평균 : %f" % average) # %f 포맷코드는 소수점 이하 6자리까지 출력
print("평균 : %.2f" % average) # .표현자리숫자f로 소수점 이하 출력 제한 가능

# 퍼센트로 % 출력
print("10%") # 제대로 출력

rate=80
print("출석률 : %d%" % rate)
# ValueError: incomplete format
# %가 형식문자로 인식되어서 나타나는 에러 = %%로 해결
print("출석률 : %d%%" % rate)
