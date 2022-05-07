m = int(input('예금액 입력 : '))
i = float(input('이자율 입력(%) : '))

print('예금액 : '+str(m)+' 원')
print('이자율 : '+str(i)+' %')

mi=m*i/100
total=int(m+mi)

print('예금이자 : %d'% mi +' 원')
print('잔액 : ' + str(total) +'원')

#----------------------------
print('예금액 : '+format(int(m),',')+'원')
print('예금이자 : '+format(int(mi),',')+'원')
print('잔액 : '+format(int(total),',')+'원')


#=========================================================================
# 풀이

amt_in = int(input('예금액 입력 : '))
amt_rate = float(input('이자율 입력(%) : '))
amt_rate_col = amt_in * amt_rate / 100 # 계산결과 실수(float)
amt_tot = amt_in + amt_rate_col

print('-------------------------------------')
print('예금액 : %d 원' % amt_in )
print('이자율 : %.1f%%' % amt_rate)
print('예금이자 : %.f 원' % amt_rate_col)
print('잔액    : %.f 원' % amt_tot)

print('-------------------------------------')
# 숫자의 천단위 구분자를 출력하고자 할 때는 format() 함수를 사용
print('예금액 : ', format(amt_in,','),'원') # , 이용해서 출력해야 할 내용
print('이자율 : %.1f%%' % amt_rate)
print('예금이자 : ', format(amt_rate_col,',.0f'),'원') # ,.f도 가능
print('잔액    : ', format(amt_tot,',.0f'),'원')
