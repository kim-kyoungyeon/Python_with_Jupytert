# Q. 학생 5명의 점수를 입력 받아서 총점과 평균을 구하여 출력(리스트에 저장할 것)

# 변수 생성
scores = [] #빈리스트 생성
sum_s = 0 #점수 총합을 위한 변수(누적변수)

# 5명 점수 입력 받아서 리스트에 저장
for i in range(5) :
    score = int(input('학생'+str(i+1)+' 점수 입력 : '))
    scores.append(score)

# 리스트의 각 점수 합계
# sum_s = sum(scores) : sum 함수 이용해서 리스트 총합 계산 가능
for s in scores :
    sum_s += s

avg = sum_s/len(scores)

print('총점 : %d' % sum_s)
print('평균 : %.2f' % avg)

# grades = []
# n = 0

# for i in range(5) :
#     n +=1
#     student = int(input('학생%d 점수 입력 : ' % n))
#     grades.append(student)
# print(grades)
