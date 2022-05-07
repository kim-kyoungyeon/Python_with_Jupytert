# 파이썬의 형 변환 함수
# int 문자열  : 문자열을 정수로 (변환불가문자열이 존재)
# float 문자열 : 문자열을 실수로(숫자 모양의 문자열만 변환 가능)
# str 정수 / 실수   :정수또는 실수를 문자열로 변환 (변환불가없음)

#print('나는 현재' + 23 + '살 입니다.') # 23이 정수이기때문에 더하기연산자불가하다 -TypeError
print('나는 현재' + str(23) + '살 입니다.') #

#int 문자열  문자열을 정수로 변환
# input 함수 사용해서 키보드로 입력  받기
# 형식 : input ('안내문자열') > 키보드 콘솔에서 대기상태
# input 함수 사용시 저장 변수를 같이 사용해야함
# 사용자로부터 숫자를 입력받아 입력 숫자가 맞는지 사용자에게 확인하는 프로그램
# 입력 양식 = 숫자를 입력하세요 : 5
# 출력 양식 = 당신이 입력한 숫자는 5 입니다

# num = input('숫자입력 : ')
# print('당신이 입력한 숫자는 : '+ num + '입니다')

# 숫자입력 : 5
# 당신이 입력한 숫자는 : 5입니다
#키보드로 입력된 숫자는 문자처리되어서 들어옴

# 사용자에게 값를 입력받은 후 120% 의 값을 계산하여 출력하시오
# 입력 양식 = 값를 입력하세요 : xxx
# 출력 양식 = 이자를 합산한 값은 xxx 입니다
num = int(input('값을 입력하세요 : ') )# 문자 입력값을 정수로 변환후 사용
tot = num * 1.2
#TypeError: can't multiply sequence by non-int of type 'float'
print('이자를 합산한 값은 : '+ str(tot) + '입니다')
#can only concatenate str (not "float") to str
#----------------------------------------------------------------
# float( ) 함수 > 실수형 변환
num = float(input('갑을 입력하세요 : ') )# 문자 입력값을 실수로 변환후 사용
tot = num * 1.2
#TypeError: can't multiply sequence by non-int of type 'float'
print('이자를 합산한 값은 : '+ str(tot) + '입니다')
#can only concatenate str (not "float") to str
#=========================================================
#숫자로 변환 eval 함수
x= eval(input('숫자 1 입력 : '))
y= eval(input('숫자 2 입력 : '))
sum= x +y
print('합 : ', sum)

#----------eval 함수는 수식 변환도 가능하다
eval('3+5')
eval('')















































