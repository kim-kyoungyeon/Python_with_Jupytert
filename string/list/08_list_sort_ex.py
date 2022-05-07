scores=[] #빈리스트 생성
sum_s = 0 #점수 총합을 위한 변수
count = 0 #80점 이상 학생 계수
num=int(input('학생수 입력: '))

for i in range(num):
    score = int(input('학생'+str(i+1)+'점수 입력:')) #문자열 글자입력 str
    #입력시 80점 이상 학생 확인
    # if score >=80 :
    #     count +=1
    scores.append(score)
#f리스트 각 점수 합계
#sum_s = sum(scores) 함수이용해서 리스트 총합계상 가능
for s in scores : #s 가 각학생의 점수
    if s >=80 :
        count +=1
    sum_s += s

avg= sum_s/len(scores)
print('총점: %d'% sum_s)
print('평균 : %.2f'%avg)
print('80점 이상 학생 : %d 명 '%count )

scores.sort(reverse=True) #내림차순 #원본반영
print("점수내림차순정렬:",scores)