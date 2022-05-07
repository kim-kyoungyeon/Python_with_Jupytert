# 다음의 함수를 포함하는 프로그램 작성
# 함수 이름 : get_interest()
# 예금액과 이자율을 전달받아서 이자액을 구하여 반환
# deposit, int_rate, interest

def get_interest(dps,rate) : # 매개변수
    inter = dps * rate / 100
    return int(inter)

deposit = int(input('예금액 입력 : '))
int_rate = float(input('이자율 입력(%) : '))

interest = format(get_interest(deposit,int_rate),',') # 소수점 없애려면 ',.f'로 수정하면
## 수치 데이터에 format 함수 적용시키면 문자열로 반환됨

print('이자액 : %s원' % interest)
