#사용자로부터 세 과목의 점수를 입력받아
#아래 조건으로 합격과 불합격을 판정하시오.
#조건
#1.세 과목의 평균이 70점 이상이어야 한다.
#2.세 과목 중 한과목이라도 40점 미만이면 과락으로
#불합격 처리한다.
s1 = float(input("과목 1 점수:"))
s2 = float(input("과목 2 점수:"))
s3 = float(input("과목 3 점수:"))

if s1<40 or s2<40 or s3<40 :
    print('과락으로 불합격 입니다.')
elif (s1+s2+s3)/3 <70 :
    print('평균 점수 %d으로 평균미달 불합격입니다' %(int(s1+s2+s3)/3))
else:
    print('패스했습니다.')

#입력 예시 1 :
#과목 1 점수 : 90
#과목 2 점수 : 40
#과목 3 점수 : 50

#출력 :
#평균점수 60으로 평균미달 불합격입니다.

#입력 예시 2 :
#과목 1 점수 : 90
#과목 2 점수 : 39
#과목 3 점수 : 90

#출력 :
#과락으로 불합격 입니다.

## 정답##
jumsu1 = int(input('과목 1 점수 :'))
jumsu2 = int(input('과목 2 점수 :'))
jumsu3 = int(input('과목 3 점수 :'))

avg= (jumsu1+jumsu2+jumsu3)/3
#중첩 if
if avg >=70 :
     #과락검사
     if(jumsu1 <40 or jumsu2<40 or jumsu3<40)
         print('과락 불합격 입니다')
     else :
         print('합격')
else :
    print("평균미달 불합격")

# if~elif 문으로 작성
if avg< 70 :
    print('평균 미달 불합격')
elif jumsu1 <40 or jumsu2<40 or jumsu3<40 :
    print('과락 불합격')
else :
    print('합격')







