kor=eval(input('국어 점수 입력 : '))
eng=eval(input('영어 점수 입력 : '))
math=eval(input('수학 점수 입력 : '))

sum=kor+eng+math
avg=sum/3

print('총점 : ', sum)
print('평균 : %.2f' % avg)