#리스트로 저장 > 학생 5명의 점수입력받아서 총점/평균구하기
# students=[]
# for i in range(5):
#     students= input('학생 점수 입력 : ')
#     students.append(students)
#     print('총점', end =' '% sum(students))
#     print('\n평균', end = ' ' % sum(students)/5)

#정답
scores=[] #빈리스트 생성
sum_s = 0 #점수 총합을 위한 변수
#5명 점수 입력 리스트에 저장
for i in range(5):
    score = int(input('학생'+str(i+1)+'점수 입력:')) #문자열 글자입력 str
    scores.append(score)
#f리스트 각 점수 합계
#sum_s = sum(scores)
for s in scores :
    sum_s += s

avg= sum_s/len(scores)
print('총점: %d'% sum_s)
print('평균 : %.2f'%avg)






