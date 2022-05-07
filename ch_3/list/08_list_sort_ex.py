scores = [] #빈리스트 생성
sum_s = 0 #점수 총합을 위한 변수(누적변수)
count = 0 #80점 이상 학생 계수

# 학생수 입력
student = int(input('학생 수 입력 : '))

# 입력 받은 학생수만큼 점수 입력
for i in range(student) :
    score = int(input('학생'+str(i+1)+' 점수 입력 : '))
    # 입력 시 80점 이상 학생 확인
    if score >= 80 :
        count += 1
    scores.append(score)

# 리스트의 각 점수 합계
# sum_s = sum(scores) : sum 함수 이용해서 리스트 총합 계산 가능
for s in scores :
    sum_s += s

avg = sum_s/len(scores)

# 점수 내림차순 정렬
scores.sort(reverse=True) #원본 반영

print('총점 : %d' % sum_s)
print('평균 : %.2f' % avg)
print('80점 이상 학생 : %d 명' % count)
print('점수 내림차순 정렬 : ',scores)

# Q. 점수를 내림차순 정렬하여 출력