#깊은복사(deep copy)
#list 함수 또는 deepcopy 함수를 사용해서
#리스트의 복사본ㅇ르 새로 생성하여 반환
#복사본 리스트의 값을 변경해도 원본에 영향을 주지 않는다
import copy #import 구문은 코드 맨위에 기술한다
scores=[1,2,3,4,5]
values=list(scores)
#deepcopy() 사용방법 - copy 모듈을 import해야한다
values2 = copy.deepcopy(scores)

values[0] =100
print(scores)
print(values)
# [1, 2, 3, 4, 5]
# [100, 2, 3, 4, 5]

#len 함수
#len(s)은 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다. 갯수 세기
#count 갯수세기;

##파이썬은 참조형변수사용 주소값저장
# 리스트의복사시에는값을유지하기위해 깊은복사를 시행해야함





