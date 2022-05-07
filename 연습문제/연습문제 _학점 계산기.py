#학점계산프로그램.py
#사용자로부터 점수를 입력받아
#학점을 구하는 프로그램
#학점은
# 90점이상 A
# 80점이상 B
# 70점이상 C
# 60점이상 D
# 60점미만 F


#입력
#점수를 입력하세요. : 95

# 출력
# 학점 : A, 점수 : 95

# 내가 푼 것
grade = int(input('점수를 입력하세요. : '))
if grade >= 90 :
    print('학점 : A, 점수 : %d'%grade)
elif grade >= 80 :
    print('학점 : B, 점수 : %d'%grade)
elif grade >= 70 :
    print('학점 : C, 점수 : %d'%grade)
elif grade >= 60:
    print('학점 : D, 점수 : %d' % grade)
else :
    print('학점 : F, 점수 : %d' % grade)

#===풀이===#
jumsu = int(input('점수를 입력하세요. '))

if jumsu >= 90 :
    print('학점 : A',' 점수 : ', jumsu)
elif jumsu >= 80 :
    print('학점 : B',' 점수 : ', jumsu)
elif jumsu >= 70:
    print('학점 : C',' 점수 : ', jumsu)
elif jumsu >= 80:
    print('학점 : D',' 점수 : ', jumsu)
else :
    print('학점 : F',' 점수 : ', jumsu)