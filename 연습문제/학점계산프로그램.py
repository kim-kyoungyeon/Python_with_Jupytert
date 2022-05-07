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
##정답
jumsu= int(input('점수를 입력하시오:'))
if jumsu >=90 :
    print('학점 : A',' 점수 :',jumsu)
elif jumsu >=80:
    print('학점 : B',' 점수 :',jumsu)
elif jumsu >=70:
    print('학점: C',' 점수 :',jumsu)
elif jumsu >= 60:
    print('학점: D',' 점수 :',jumsu)
else:
    print("학점 : F",' 점수 :',jumsu)