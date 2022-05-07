#dic는 키:값의 쌍으로 되어 있다.
#사용자의 입력을 받아  단어:뜻 으로 되어 있는 영한사전을 만들고
#단어의 일부 문자만 입력해도 해당 문자가 포함되어 있는 단어를 찾아
#단어와 뜻을 출력하는 검색 기능을 생성하라
#단, 사전 생성은 딕셔너리사전.py 파일의 코드를 이용하시오.

#단어등록과 검색 모두 사용자가 exit를 입력할 때 까지 진행시키시오.

# 입출력 예시
# 단어입력(종료는 exit)dog
# dog의 뜻입력(종료는 exit)강아지

# 단어입력(종료는 exit)apple
# apple의 뜻입력(종료는 exit)사과

# 단어입력(종료는 exit)exit

# 검색할 문자를 입력하세요.(종료는 exit) : apple
# apple : 사과

# 검색할 문자를 입력하세요.(종료는 exit) : a
# a (apple:사과)

# 검색할 문자를 입력하세요.(종료는 exit) : d
# d (dog:강아지)

# 검색할 문자를 입력하세요.(종료는 exit) : 사과
# 검색문자와 매치되는 단어가 없습니다.

# 검색할 문자를 입력하세요.(종료는 exit) : exit

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

print('---------- 검색 시작 ----------')

while True :
    eng = input('\n검색할 문자를 입력하세요. (종료는 exit) : ')
    i = 0 #사전에서 단어나 문자를 찾지 못할 경우에 사용할 i
    # 프로그램 종료 전에 i가 0이면 사전에 없는 단어
    # 그 외는 사전에서 찾아서 출력

    if eng == 'exit' :
        break

    if eng in ek_dic : #검색문자가 완성 단어면
        print('%s : %s' % (eng,ek_dic[eng]))
        i += 1
    else : # {dog:강아지, cat:고양이, day:일} --- 사용자가 d 입력
        for key,value in ek_dic.items() :
            if(eng in key) : # key 문자열에 eng 문자가 있으면
                print('%s (%s:%s)' % (eng,key,value))
                i += 1

    if i == 0 :
        print('검색문자와 매치되는 단어가 없습니다.')
