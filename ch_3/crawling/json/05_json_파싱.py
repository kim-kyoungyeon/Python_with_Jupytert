import json
# with open('json file path or name')as jason_file:
#     jason_data = jason.load(json_file)
#     {
#         'json_string': "string_example",
#         'json_number':100,
#         "json_array":[1,2,3,4,5],
#         "json_object":{'name':'John','age':30},
#         'json_bool':true
#     }

#with을 이용해파일을연다
#jason파일이 같은 폴더에 있따고 가정한다
file_path="./student.json"
with open(file_path,'   r')as json_file:
    json_data= json.load(json_file)
    print(json_data)
#    문자열
#key가 jason_string인 문자열 가져오기
json_string=json_data['json_string']
print(json_string)

#숫자
#key가 json_number인 숫자가져오기
json_number=json_data['json_number']
print(str(json_number))# 숫자이기때문에 str()함수를 이용
#배열
#key가 json_array인 배열가져오기
json_array=json_data["json_array"]
print(json_array)
#객체
#key가 jsonobject인 객체가져와서만들기
#json obect 인 경우 python object로 바꿀때에는 따로처리하기
#기본형은 딕셔너리입니다.
json_object = json_data['json_object']
print(json_object)
#bool형
#key가 json_boolㅇ린 bool형 자료 가져오괴
json_bool= json_data['jason_bool']
print(json_bool)

