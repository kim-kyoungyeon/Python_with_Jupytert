# 중첩 if
# if문 안에 다른 if문 포함
# if(조건식) :
#   if(조건식2) :
#       문장 A
#   else :
#       문장 B
# else :
#       문장 C

# 중첩 if일 때 else는 가까운 if와 짝이 된다.

# 사과 상태가 신선하면 가격을 물어보고
# 가격이 1000원 미만이면 10개를 사고, 1000원 이상이면 5개를 살 것
# 사과 상태가 신선하지 않으면
# 사과를 사지 않는다고 출력

# 사과 상태 질문
apple_quality = input('사과 상태 입력 : ')

if apple_quality == '신선' :
    #가격을 물어보고 개수를 정한다.
    apple_price = int(input('사과 가격 입력 : '))
    if apple_price < 1000 :
        print('10개를 산다.')
    else :
        print('5개를 산다.')
else :
    print('사과를 사지 않겠습니다.')




