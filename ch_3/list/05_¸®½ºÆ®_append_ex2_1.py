scores = [] #빈리스트 생성
sum_s = 0 #점수 총합을 위한 변수(누적변수)
count = 0 #80점 이상 학생 계수

# 5명 점수 입력 받아서 리스트에 저장
for i in range(5) :
    score = int(input('학생'+str(i+1)+' 점수 입력 : '))
    # 입력 시 80점 이상 학생 확인
    # 택1 if score >= 80 :
    #     count += 1
    scores.append(score)

# 리스트의 각 점수 합계
# sum_s = sum(scores) : sum 함수 이용해서 리스트 총합 계산 가능
for s in scores :
    # 택2 if s >= 80 :
    #       count += 1
    sum_s += s

avg = sum_s/len(scores)

print('총점 : %d' % sum_s)
print('평균 : %.2f' % avg)
print('80점 이상 학생 : %d 명' % count)

# Q. 위 코드를 수정해서 점수가 80점 이상인 학생의 수를 계산한 후에 출력하시오.



