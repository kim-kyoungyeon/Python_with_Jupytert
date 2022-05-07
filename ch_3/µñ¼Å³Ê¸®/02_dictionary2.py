# 딕셔너리 선언
dictionary = {'name':'버섯불고기덮밥',
              'type':'덮밥',
              'ingredient':['소고기','버섯','양파','간장','설탕'],
              'origin':'한국'}

# 딕셔너리 내용 출력
print('요리명 : ', dictionary['name'])
print('종류 : ', dictionary['type'])
print('재료 : ', dictionary['ingredient']) # 리스트 형태로 출력
print('원산지 : ', dictionary['origin'])

# 딕셔너리 값 변경
dictionary['name'] = '한우 버섯 불고기 덮밥'
print('요리명 : ', dictionary['name'])

# 재료를 출력하되 리스트의 원소만 출력되도록 변경
ingredient = ''
for i in dictionary['ingredient'] :
    ingredient += i + ' '
print(ingredient)

# 출력 결과
print('요리명 : ', dictionary['name'])
print('종류 : ', dictionary['type'])
print('재료 : ', ingredient)
print('원산지 : ', dictionary['origin'])
