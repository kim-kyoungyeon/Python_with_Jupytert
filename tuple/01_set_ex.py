#파티에 참석한 사람이 다음과 같을때 집합을
# 생성하고 아래 조건에 맞게출력해라
#partyA : 'Park','Kim','Lee'
#partyB : 'Park','길동','몽룡'
# # 조건
partyA = {'Park','Kim','Lee'}
partyB = {'Park','길동','몽룡'}

# 파티에 참석한 모든 사람은?
print(partyA.union(partyB))
# #2개의 파티에 모두 참석한사람은?
print(partyA.intersection(partyB))
# 파티a만 참석한사람
print(partyA.difference(partyB))
# 파티b 에만 참석한사람
print(partyB.difference(partyA))














