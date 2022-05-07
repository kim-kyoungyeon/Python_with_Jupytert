# money= float(input('값을 입력하세요 : ') )
# rate = float(input('이자율 입력(%)하세요 : ') )
# rate2 = money * (rate/100)
# mr= money+rate2
#
# print("예금 이자 : %.f 원 , 잔액 : %.f원"  % (rate2,mr))
# print("예금 이자 :"+ str(rate2) + "원")
# print("잔액 :" + str(mr) + "원" )
# print("예금 이자 :" ,format(int(rate2),',')+"원")
# print("잔액 : ",format(int(mr),',')+"원")

###----------------------------- 정답----------------------------------------

amt_in = int(input("예금액 입력:")) # input 문자열 # int 정수형
amt_rate = float(input("이자율 입력(%): ")) #flaot 실수형
amt_rate_col = amt_in *amt_rate / 100 # 계산결과 float = %f
amt_tot = amt_in+amt_rate_col # 정수 + 실수값이라 실수의 값이 나온다

print("-----------------------------------------------")
print("예금액 : %d 원" %amt_in) # 포맷문자에는 1개당 변수가  1개  변수가 2개이상일시 괄호
print("이자율 : %.1f%%" %amt_rate ) #실수인 값 소수점 1개 까지 #%% = 그냥 %  % 하나만 쓰면 플로트 함수로 잘못인식!
print("예금이자 : %.f원 " % amt_rate_col) #하나의 변수로 인식
print("잔액 : %.f 원"% amt_tot)
print("-----------------------------------------------")
#숫자의 천단위 구분자를 출력하고자 할 때는 format 함수를 사용
print("예금액 : " ,format(amt_in,','),"원")
print("이자율 : %.1f%% " %amt_rate ) #%% = 그냥 %  % 하나만 쓰면 플로트 함수로 잘못인식!
print("예금이자 : ",format(amt_rate_col,',.0f'),"원") #
print("잔액 : " , format(amt_tot,',.0f'),"원") #여러개의 매개변수 ',.0f'








