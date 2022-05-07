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
#print("\u2665") #<=하트출력
#중첩 for문을 이용


# 중첩 for 문

numstr, starstr=  '',''
i = k= ch=starNum=0
numstr=input('숫자를 여러개 입력하세요')
#len 리스트 크기 확인
#range 함수
#필요한 만큼의 숫자를 만들어내는 유용한 기능
#range([start,] stop [,step])는 for문과 함께 자주 사용되는 함수이다.
# 이 함수는 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴한다.
for i in range(0,len(numstr)) :
    starNum=int(numstr[i])
    starstr='' # 리스트 값을 초기화 없을시 누적해서 나타난다
    for k in range(0,starNum) :
        starstr +="\u2665"#필요한 만큼 하트 문자 누적

    print(starstr)
#파이썬에선 곱하기연산자 있음
#위코드에서 안쪽 for문의 k 변수는 사용되지 않았음



#문자열 * 연산자
#print('\u2665')# 하트문자 아스키코드
num=input('숫자를 여러개 입력하세요')#문자열
#345 3개 3줄에 걸쳐서
for i in range(len(num)) :
    print('\u2665'*int(num[i])) #문자열 str > int 해서   변경
# 위코드에서 for 문 k 변수는 사용되지 않음
#내부적으로 반복의 회수를 계산하는데 사용
#반복변수라고 부름