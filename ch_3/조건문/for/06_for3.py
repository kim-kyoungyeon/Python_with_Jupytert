# Q. 리스트에 저장되어 있는 성적에 따라 합격 불합격을 판별하시오.
# 리스트에 저장된 점수가 60점 이상이면 합격 아니면 불합격 처리하시오.
# 출력 양식 : (리스트 저장 순서에 따라) 1번 90점 합격

# 필요변수 생성
scores = [90,57,88,45,78] #리스트 변수 생성, 리스트는 [] 안에 요소를 나열해서 생성한다.
num = 0 #출력 시 앞에 사용할 번호를 위한 변수(ex. 1번)

for score in scores :
    num += 1
    if score >= 60 :
        result = '합격'
    else :
        result = '불합격'
    print('%d번 %d점은 %s' % (num,score,result))

# Q1. 위 프로그램의 반복 횟수를 쓰시오.
# A1. 5번, scores 리스트 요소의 개수만큼 반복이 일어나게 됨.