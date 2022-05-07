# Q. 이메일 주소를 입력 받아서, 이메일 형식이 아니면 "이메일 형식이 아닙니다." 출력
# 이메일 형식이 아닌 경우 : # @, . --- 없는 경우, 둘의 위치가 바뀐 경우, 둘 사이에 문자가 없는 경우. @ 앞에 문자가 없는 경우, . 뒤에 문자가 없는 경우

# abc@mc.ac.kr <- email 변수에 저장
# len(), count(), find(), index()
# @ 없는 경우 : email.find('@') == -1 or
# . 없는 경우 : email.find('.') == -1 or
# @과 . 위치가 바뀐 경우 : email.index('@') > email.index('.') or
# @과 . 사이에 문자가 없는 경우 : email.index('.') - email.index('@') < 2 or
# @ 앞에 문자가 없는 경우 : email.index('@') == 0 or
# . 뒤에 문자가 없는 경우 : len(email) - email.index('.') <= 1 or ** abc@mc.ac. : 정상 이메일로 인식 (오류)
## . 문자가 마지막 문자인 경우 : email[len(email)-1] =='.' or
# @ 두 번 이상 있는 경우 : email.count('@') >= 2 or
# . 두 번 이상 있는 경우 : email.count('.') >= 2

email = input('이메일을 입력하세요. : ')

if (email.find('@') == -1 or
    email.find('.') == -1 or
    email.index('@') > email.index('.') or
    email.index('.') - email.index('@') < 2 or
    email.index('@') == 0 or
    email[len(email)-1] =='.' or
    email.count('@') >= 2 or
    email.count('.') >= 3) :
     print('이메일 형식이 아닙니다.')

print('입력한 이메일 : %s' % email)