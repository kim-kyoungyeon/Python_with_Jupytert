# 난수 발생 방법
# 파이썬이 기본으로 제공하는 random 모듈 사용

# 사용함수 : randint(최소, 최대)
# 최소부터 최대 사이의 임의의 정수 반환
# 프로그램 첫줄에
# from random import randint -> 기본함수가 아닌 외부 모듈을 사용할 때 함수가 어느 모듈에 속해있는지 알려주는 코드
# 모듈과 함수 등록 코드

from random import randint

n = randint(1,100)

print(n)

com = randint(1,3)
print(com)