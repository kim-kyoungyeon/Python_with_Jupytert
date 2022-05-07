import  json
#딕셔너리 생성
data={'member':[{'name':'Kim','from':'Seoul','website':'naver.com'},
                {'name':'Park','from':'Busan','website':'google.com'},
                {'name':'Lee','from':'Incheon','website':'daum.net'}]}
#딕셔너리를 json 문자열로 변환
data_str = json.dumps(data,indent='\t')

# print(data_str)
# #json 파일쓰기
with open('mebmer.json', 'w' ) as outfile:
    outfile.write(data_str)
# #memberjson파일 생성되었는지 확인 내용도 확인
#
# #######################################3
# #json 파일 읽기(loads)
with open('book.json','r',encoding='utf-8')as infile:
    book_dict=json.loads(infile.read())
print(book_dict)
#
# print('-----------------------------------------------')
for std in book_dict['book']:
    print('도서명:'+ std['title'])
    print('가격:' + str(std['price']))
    print('저자:' + std['author'])
    print()

##################################
#네이버 api 검색한 결과를 출력하면 < response[200]>
# 결과를 json 형태로 변환해야 내용을 알수있음
# 크롤링 결과를 json 형태로반환
#
# json파일로 저장
#     딕셔너리를 문자열로변환
#     json파일저장
#
# json 파일을 분석하려면 읽어들여야하는데
#     읽으면 딕셔너리로 만들어짐
#     딕셔너리는 파이썬 자료형이므로 데이터추출가능




