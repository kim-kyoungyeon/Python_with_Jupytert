# replace()
# 전체 문자열에서 특정 문자열을 찾아 다른 문자열로 변경
# 전체문자열.replace(찾는문자열, 변경할문자열)
# 찾는 문자열이 존재하면 문자열 변경해서 반환
# 찾는 문자열이 없으면 원래 문자열 반환

course = 'Java programming'

# Java를 찾아서 Python으로 변경
c_replace = course.replace('Java','Python')
print(c_replace)

c_replace = course.replace('Web','Python')
print(c_replace) #못찾음 : 원래 문자열 출력