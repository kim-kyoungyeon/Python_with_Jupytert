#얕은복사(shallowe copy)
실제리스트는 복사안되고 참조값 주소만 복사
복사본 리스트 요소의 값을 변경하면 원본리스트요소값도 변경
scores= [10,20,30,40,50]
values=scores
values[0] = 100

print('scores :',scores)
#리스트요소값변경
print('values :',values)
