# 공백 제거
# strip() : 양쪽 공백 제거
# lstrip() : 왼쪽 공백 제거
# rstrip() : 오른쪽 공백 제거

s = '    서울시 강남구 역삼동    '
print(s.strip()) # 서울시 강남구 역삼동
print(s.lstrip()) # 서울시 강남구 역삼동    --- 오른쪽 공백 남아 있음
print(s.rstrip()) #     서울시 강남구 역삼동



