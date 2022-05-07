# 다음과 같이 출력
# *****
# ****
# ****
# **
# *

for y in range(5) :
    for x in range((6-y)-1) :
        print('*',end='')
    print()