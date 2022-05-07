# 다음과 같이 출력
# *
# **
# ***
# ****
# *****

n = ''
for y in range(5) :
    for x in range(1) :
        n += '*'
        print(n,end=' ')
    print()

# for y in range(5):
#     for x in range(y+1):
#         print('*', end='')
#     print()