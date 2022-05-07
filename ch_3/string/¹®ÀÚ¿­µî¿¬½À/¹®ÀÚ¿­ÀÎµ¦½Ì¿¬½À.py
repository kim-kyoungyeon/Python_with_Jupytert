#1) lang가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하라.
# >> lang = 'python'
#
# 실행 예
# p t

lang = 'python'
print(lang[0],lang[2])

#2) 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하라.
# >> license_plate = "24가 2210"
#
# 실행 예: 2210

license_plate = "24가 2210"
print(license_plate[4:])

#3) 아래의 문자열에서 '홀' 만 출력하라.
# >> string = "홀짝홀짝홀짝"
#
# 실행 예:
# 홀홀홀

string = "홀짝홀짝홀짝"
print(string[::2]) # 홀홀홀
print(string[1::2]) # 짝짝짝

#4) 문자열을 거꾸로 뒤집어 출력하라.
# >> string = "PYTHON"
#
# 실행 예:
# NOHTYP

string = "PYTHON"
print(string[::-1])


#5) 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하라.
# >> phone_number = "010-1111-2222"
#
# 실행 예
# 010 1111 2222

phone_number = "010-1111-2222"
print(phone_number[0:3],phone_number[4:8],phone_number[9:13])
print(phone_number.replace('-',' '))

#6) 위 문제의 전화번호를 아래와 같이 모두 붙여 출력하라
# 실행 예
# 01011112222
print(phone_number.replace('-',''))

#7) url 에 저장된 웹 페이지 주소에서 도메인을 출력하라.
# >> url = "http://sharebook.kr"
#
# 실행 예:
# kr

url = "http://sharebook.kr"
print(url[-2:])
print(url.split('.')[1])

#8) 아래 코드의 실행 결과를 예상하라
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

# 예상 : 문자열에 직접 접근해서 수정은 불가능
# 'str' object does not support item assignment

#9) 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하라.
# >> string = 'abcdfe2a354a32a'
#
# 실행 예:
# Abcdfe2A354A32A

string = 'abcdfe2a354a32a'
print(string.replace('a','A'))

#10) 아래 코드의 실행 결과를 예측하라.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

# 예상 : aBcd (x) abcd (o)
# repalce() 함수는 원본을 변경시키지 않기 때문에 코드에서 저장이 일어나지 않으므로 원본이 유지되어서 abcd가 출력된다.
# 문자열 관련 함수는 저장을 해야 원본에 적용이 된다.