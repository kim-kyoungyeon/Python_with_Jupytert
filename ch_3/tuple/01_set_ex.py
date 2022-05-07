# 파티에 참석한 사람이 다음과 같을 때 집합을 생성하고 아래 조건에 맞게 출력하시오.

# partyA : 'Park','Kim','Lee'
# partyB : 'Park','길동','몽룡'

# 조건 --------------------------
#1) 파티에 참석한 모든 사람은?
#2) 2개의 파티에 모두 참석한 사람은?
#3) 파티 A에만 참석한 사람
#4) 파티 B에만 참석한 사람

partyA = {'Park','Kim','Lee'}
partyB = {'Park','길동','몽룡'}

#1)
print(partyA.union(partyB))

#2)
print(partyA.intersection(partyB))

#3)
print(partyA.difference(partyB))

#4)
print(partyB.difference(partyA))

