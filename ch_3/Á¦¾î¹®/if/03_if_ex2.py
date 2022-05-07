# 짐의 무게가 20을 초과할 경우, '무게 초과, 수수로 20,000원' 출력
# 20 이하인 경우에는 '수수료 없음' 출력
# 프로그램 종료 시 '종료합니다.' 출력

weight = float(input('짐의 무게는 얼마입니까? '))
if weight > 20 :
    print('무게 초과, 수수료 20,000원')
    print('종료합니다.')
else :
    print('수수료 없음')
    print('종료합니다.')


## 풀이
weight = float(input('짐의 무게는 얼마입니까? '))
if weight > 20:
    print('무게 초과. 수수료 20,000원')
else:
    print('수수료 없음')

print('종료합니다.')
