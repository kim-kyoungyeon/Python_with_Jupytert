#포맷코드
#print()에서 문자열과 변수를 함께 출력할대
#방법1
#print ("문자열",변수) , 로 나열하는방법
#방법2 포맷코드를 사용하는 방법
#print("서식" % 값 )
# #print("문자열 %d 문자열 %변수)
# ""안에 있는 포맷코드 위치에 뒤의 변수값이 매칭
#%d 는 정수형 의미
age= 10
print("나이 : %d 살" %age)
print("내 이름은 %s 입니다" %name)

# 포맷코드정리
# %s 문자열
# %c문자 1개
# %d 정수
# %f 부동소수
# %o 8진수
# %x 16진수
# %% %자체

#%c는 1문자
grade = 'A'
average = 93.5

# 포맷코드 사용 출력
print('학점 : %c '%grade)
print('학점 : %s '%grade)# 한문자여도 %s 문자열 처리가능하다

print('학점 : %c '%name)
# 두글자 이상은 %c 사용불가
print('학점 : %c '%24)#TypeError: %c requires int or char

print('평균 : %f '%average)# %f 포맷코드는 소수점 이하 6자리 까지 출력
print('평균: %.2f'% average) # .표현자리 숫자 f 로 소수점이하출력제한가능

# 퍼센트로 % 출력
 print("10%")# 제대로 출력
 rate = 80
print("출석률: %d% " %rate) # ValueError: incomplete format
# % 가 형식문자로 인식되어서 나타나는 에러 %%로 인식



