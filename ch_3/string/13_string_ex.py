# Q. 사용자에게 주민등록번호를 입력받아서 성별을 구분하는 프로그램을 작성하시오.

# 입력 : 970820-1xxxxxx
# 출력 : 남성입니다.

# 제출 : mkm0515@naver.com
# 제목 : 청취_xxx_문자열_주민번호
# index 글자가 여성, 남성

# num = input('주민등록번호를 입력하세요. : ')
# num_list = num.split('-')[1]
# num_check = int(num_list[0])
#
# if num_check == 1 or num_check == 3 :
#     print('남성입니다.')
# else :
#     print('여성입니다.')


#=== 풀이 ===#
# 주민번호 안에 - 있으면 8번째 글자
# 1,3 이면 남성
# 2,4 면 여성
# 그 외는 잘못된 주민번호로 표시

print('입력양식 : xxxxxx-xxxxxxx')
jumin = input('주민번호를 입력하세요. : ')

if jumin[8] in ('1','3') :
    print('남성 입니다.')
elif jumin[8] in ('2','4') :
    print('여성 입니다.')
else :
    print('잘못된 주민번호 입니다.')

# 저장을 위해서 주민번호의 - 를 제거하려고 할 때 --- 1. split 이용
jumin_list = jumin.split('-')
# ['970620','1111111']

if jumin_list[1][0] in ('1','3') :
    print('남성 입니다.')
elif jumin_list[1][0] in ('2','4') :
    print('여성 입니다.')
else :
    print('잘못된 주민번호 입니다.')

# 저장을 위해서 주민번호의 - 를 제거하려고 할 때 --- 2. replace 이용
jumin_rep = jumin.replace('-','')

if jumin_rep[7] in ('1','3') :
    print('남성 입니다.')
elif jumin_rep[7] in ('2','4') :
    print('여성 입니다.')
else :
    print('잘못된 주민번호 입니다.')
