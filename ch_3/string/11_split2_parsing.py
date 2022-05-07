# 패턴이 있는 문자열에서 숫자만 추출해서 총 합계 구하기
str_data = '{a1:20},{a2:30},{a3:15},' \
           '{a4:50},{a5:-14},{a6:15},' \
           '{a7:20},{a8:70},{a9:-100}'

# 위 문자열에서 구분자를 찾아서 분리
# ,(쉼표)로 구분해서 문자열 분리
split_str_data = str_data.split(',')
print(split_str_data)

print(len(split_str_data)) # 9

# 누적변수
tot=0

# 숫자만 추출하기
for i in range(0,len(split_str_data)) :
    str_temp = split_str_data[i].split(':')[1].split('}')[0] #추출결과 문자열
    # print(str_temp)
    tot += int(str_temp)

print('추출된 숫자의 합은 %d 입니다.' % tot)
