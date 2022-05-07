# 딕셔너리를 이용해 사용자로부터 영단어와 뜻을 입력받아 사전을 구성하고,
# 사용자가 입력한 단어를 뜻으로 출력하는 프로그램을 작성하시오.
# 단어 등록은 사용자가 exit를 입력할때까지 계속하며
# 단어 검색 또한  exit를 입력할때까지 계속한다.

# 입력 예시)
# 단어입력(종료는 exit) : dog
# dog의 뜻 입력 : 강아지
#
# 단어입력(종료는 exit) : cat
# dog의 뜻 입력 : 고양이
#
# 단어입력(종료는 exit) : exit

#출력 예시)

# 단어를 입력하세요.(종료는 exit) : dog
# # dog의 뜻은 강아지 입니다.

### 풀이 ###
# 필요 변수 생성 --- 사전을 구성하기 위해 빈 딕셔너리 생성
ek_dic = {}
# ek_dict = dict()

# 단어를 사전에 등록하는 모듈 --- 무한루프로 구성
# 종료조건 : exit 입력
while True :
    eng = input('\n영어 단어 등록 (종료는 exit) : ')
    if eng == 'exit' :
        break
    elif eng not in ek_dic :
        kor = input('%s의 뜻 입력 (종료는 exit) : ' % eng)
        ek_dic[eng] = kor
    else :
        print('%s는 이미 등록된 단어 입니다.' % eng)

# print(ek_dic)

print('---------- 검색 시작 ----------') # 검색 시작 시 한줄 내려서 시작

while True :
    eng = input('\n검색할 단어 입력 (종료는 exit) : ')
    if eng == 'exit' :
        break
    elif eng in ek_dic :
        print('%s의 뜻은 %s 입니다.' % (eng,ek_dic[eng]))
    else :
        print('%s는 사전에 없는 단어입니다.' % eng)