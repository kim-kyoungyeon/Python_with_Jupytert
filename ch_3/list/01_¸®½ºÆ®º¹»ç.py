# 얕은 복사(shallow copy)
# 실제 리스트는 복사되지 않고 참조값(주소)만 복사
# 복사본 리스트 요소의 값을 변경하면 원본 리스트 요소 값도 변경
scores = [10,20,30,40,50]
values = scores
values[0] = 100 #복사본 리스트 요소값 직접 변경

print('scores : ',scores) #원본 리스트 요소값 변경
print('values : ',values)