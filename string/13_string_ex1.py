#사용자에게 주민등록번호를 입력받아서 성별구분하는프로그램작성
#입력: 970307-1xXXXX
#남성입니다.

# 주민번호 안에  - 8번째 글자 / 없으면 7번째 글자
# 1.3 이면 남성
# 2.4 여성
# 1234 외에는 잘못된 주민번호
# print('입력양식 : xxxxxx-xxxxxxx')
# jumin = input('주민번호를 입력하세요 :')
# # 8째자리 (-)포함
# if jumin[8] in ('1','3'):
#     print('남성입니다')
# elif jumin[8] in ('2','4') :
#     print('여성입니다')
# else :
#     print('잘못된 주민번호입니다')
# split(sep="",maxsplit="1")
#기본적으로 공백과 1 저장 -디폴트

#문자열.replace(“검색 문자”, “치환 문자” [, 치환 횟수])
# 저장을 위해서 주민번호의 -를 제거 하려고 할 때
# 리스트를 묶을때 대시를 제거..
# split 이용
jumin_list= jumin.split('-')
# -를기준으로 리스트를 만든다
jumin= ['970820','1111111']
if jumin_list[1][0] in ('1','3'): #첫번째 글자를 지칭 [0]번
    print('남성입니다')
elif jumin_list[1][0] in ('2','4') :
    print('여성입니다')
else :
    print('잘못된 주민번호입니다')
#저장을 위해 주민번호 -를 제거
#replace # 7째자리
jumin_rep = jumin.replace('-','')
if jumin_rep[7] in ('1','3'): #첫번째 글자를 지칭 [0]번
    print('남성입니다')
elif jumin_list[7] in ('2','4') :
    print('여성입니다')
else :
    print('잘못된 주민번호입니다')

## 코딩은 제일뒤쪽
