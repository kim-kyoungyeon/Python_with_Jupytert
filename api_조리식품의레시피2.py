import requests

endpoint = "http://openapi.foodsafetykorea.go.kr/api/"
keyId = "880ad8b4b32a4adf9e17"
serviceId = "COOKRCP01"
dataType = "json"
startIdx = "1"
endIdx = "500"

paramset = keyId + "/" + serviceId + "/" + dataType + "/" + startIdx + "/" + endIdx
url = endpoint + paramset
# print(url)

result = requests.get(url)
cooking = result.json()
# print(cooking)

#데이터 추출
recipe_list=cooking['COOKRCP01']['row']
# print(food_list)
# print(recipe_list)

# manual01부터 데이터가 들어있는 manual**까지 반복 프린트

manual1 = "MANUAL0"
manual2 = "MANUAL"

# for cook in recipe_list:
#     n = 0
#     print(cook['RCP_NM'])
#
#     for c in cook:
#         n += 1
#         if n <= 9:
#             manual = manual1 + str(n)
#         else:
#             manual = manual2 + str(n)
#
#         try:
#             if cook[manual] != "":
#                 print(cook[manual])
#
#         except Exception:
#             pass
#
#     print('\n')
    # print(cook['INFO_ENG'] + ', ' + cook['INFO_CAR'] + ', ' + cook['INFO_PRO'] + ', ' + cook['INFO_FAT'])


#파일 생성하고 데이터 저장(쓰기)
f=open("C:/PythonStudy/탄단지/recipe_data.txt",'w')
for cook in recipe_list:
    n = 0
    print(cook['RCP_NM'])
    f.write(cook['RCP_NM']) # 메뉴명
    for c in cook:
        n += 1
        if n <= 9:
            manual = manual1 + str(n)
        else:
            manual = manual2 + str(n)

        try:
            if cook[manual] != "":
                print(cook[manual] + '\n')
            f.write(cook[manual] + '\n') # 내용
        except Exception:
            pass

    print('\n')

f.close()

# #읽기 모드로 파일 열고 출력
# f=open("C:/PythonStudy/탄단지/recipe_data.txt",'r')
#
# lines = f.readlines()
#
# for line in lines:
#     print(line)
#
# f.close()
#
# f=open("C:/PythonStudy/탄단지/recipe_data.txt",'w')
# data="easy_python_crawler"
# f.write(data)
# f.close()