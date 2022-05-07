#급여를 지불하기 위해 사용자로부터 근로시간과 시간당 임금을 입력받아 출력하는 프로그램을 완성하시오.
#입력ex)

#근로시간을 입력하세요. : 150
#시간당 임금을 입력하세요. : 60000

#출력ex)
#근로시간 150 시간
#시간당 임금 60,000원
#총 급여

# 내가 푼 것
work_hour = int(input('근로시간을 입력하세요. :'))
work_wage = int(input('시간당 임금을 입력하세요. :'))

print('근로시간 %d 시간' % work_hour)
print('시간당 임금 ', format(work_wage,','),'원')
print('총 급여 ', format(work_hour*work_wage,','),'원')


#=== 풀이 ====
w_h = int(input('근로시간을 입력하세요. :'))
h_w = int(input('시간당 임금을 입력하세요. :'))

print('근로시간 : ', w_h)
print('시간당 임금 : ', h_w)
print('총 급여 : ', w_h*h_w,'원')