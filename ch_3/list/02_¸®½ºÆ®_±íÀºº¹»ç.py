# 깊은 복사(deep copy)
# list() 함수 또는 deepcopy() 함수를 사용해서 리스트의 복사본을 새로 생성하여 반환
# 복사본 리스트의 값을 변경해도 원본에 영향을 주지 않음

import copy #import 구문은 코드 맨 위에 기술한다.
scores = [1,2,3,4,5]
values = list(scores)
# deepcopy() 함수 사용 --- copy 모듀을 import해야 함
values2 = copy.deepcopy(scores)

values[0] = 100

print(scores) #[1, 2, 3, 4, 5]
print(values) #[100, 2, 3, 4, 5]

## 파이썬은 참조형 변수를 사용(주소값을 저장)
## 리스트의 복사 시에는 값을 유지하기 위해서 깊은 복사를 실행해야 한다.



