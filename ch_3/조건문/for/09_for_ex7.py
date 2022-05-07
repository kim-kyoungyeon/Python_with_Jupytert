# Q. 숫자 10개를 입력 받아서 양, 음, 0의 개수 출력
# num1 = input('숫자1입력 : ')
# num2 = input('숫자2입력 : ')
# num3 = input('숫자3입력 : ')
# num4 = input('숫자4입력 : ')
# num5 = input('숫자5입력 : ')
# num6 = input('숫자6입력 : ')
# num7 = input('숫자7입력 : ')
# num8 = input('숫자8입력 : ')
# num9 = input('숫자9입력 : ')
# num10 = input('숫자10입력 : ')

# tot = [num1,num2,num3,num3,num4,num5,num6,num7,num8,num9,num10]
# d = 0

# for num in tot :
#     if tot > 0 :
#         result = tot
#     elif tot < 0 :
#         result = tot
#     else :
#         result =


#=== 풀이 ===#
# 양수, 0, 음수 계수할 변수 생성 및 초기화(누적변수)
pos = neg = zero = 0

for i in range(1,11) :
    n = int(input('숫자'+str(i)+'입력 : '))
    if n > 0 :
        pos += 1
    elif n < 0 :
        neg += 1
    else :
        zero += 1

print('--------------------------')
print('양의 개수 : ', pos)
print('음의 개수 : ', neg)
print('0의 개수 : ', zero)