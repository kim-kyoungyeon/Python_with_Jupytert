# 사용자로부터 숫자를 입력받아 입력받은 숫자를 분해하여 낱개 숫자만큼
# 하트를 출력하는 프로그램을 작성하시오.

# 입력
# 숫자를 여러개 입력하세요 : 325
#
# 출력
# ♥♥♥
# ♥♥
# ♥♥♥♥♥

# 하트 문자 : "\u2665"
print("\u2665") #<=하트(하트 모양 글자 아스키 코드)출력

# 1) 중첩 for 문을 이용

# numstr,starstr = '',''
i=k=ch=starNum=0

numstr = input('숫자를 여러개 입력하세요. : ')

for i in range(0,len(numstr)) :
    starNum = int(numstr[i])
    starstr = ''
    for k in range(0,starNum) :
        starstr += '\u2665' #필요한만큼 하트 문자를 누적

    print(starstr)

# 위 코드에서 안쪽 for 문의 k 변수는 사용되지 않았음
# 내부적으로는 반복의 횟수를 계산하는 데 사용되고 있음
# 이러한 변수를 '반복변수'라고 부름

# starstr 변수 --- for 문 내 초기화 역할(밖에 나와 있으면 누적)
# ♥
# ♥♥♥
# ♥♥♥♥♥♥

# 2) 문자열 * 연산자
num = input('숫자를 여러개 입력하세요. : ') # 문자열
# 345

for i in range(len(num)) :
    print('\u2665'*int(num[i]))