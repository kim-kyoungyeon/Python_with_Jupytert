import requests
from bs4 import BeautifulSoup
from urllib.parse import quote #한글 코드 가져오기
endpoint='http://www.career.go.kr/cnet/openapi/getOpenApi?'
apiKey='dcc2db5b377c881a9328b3e764f2ad3d'

svcType= "api"
svcCode= "SCHOOL"
contentType="json" #커리어넷 기본정보
gubun='univ_list'
# region='100260'
perPage='10000'

paramset= "apiKey="+apiKey +"&" \
        + "svcType="+svcType +"&"\
        + 'svcCode=' +svcCode+"&"\
        + 'contentType='+contentType+"&"\
        +'gubun='+gubun+"&"\
+'perPage='+perPage

        # +'region='+region+"&"\

url= endpoint+paramset
# print(url)
result= requests.get(url)
school_data= result.json()
school_list=school_data ['dataSearch']['content']
# print(school_list)

result= requests.get(url)
soup=BeautifulSoup(result.content, 'html.parser')
items= soup.findAll('item')
print(soup)

uni_data= result.json()

uni_list=uni_data ['dataSearch']['content']

uni_total="" #이름저장
uni_info="" #주소저장
uni_count=0
for content in uni_list : #content를 뽑아서 unilist에 넣음
    if content['adres'] !='null':#학교 주소 추출하기
        print(type(content['adres']))
        #'정보통신'들어있는 경우
        if '서울' in content['adres'] :
        # if content['profession'].find('정보통신') >= 0 : #'str' 문자열 (결과는 위 if 조건과 동일함. 같은 함수)
        #if content['profession'].find('정보통신') != -1 #문자열 -1  파이썬find 함수 공부하기
            if content['schoolName'] != 'null': # 이름 리스트
                # uni_total+=int(content['schoolName'].split(" ")[0])
                uni_count+=1
            adr = content['adres']
            sch_name =content['schoolName']
            uni_info += sch_name +','+adr+"\n"
print(uni_info)
print(uni_count)

# (2) 서울내 모든 대학교 개수 추출
print('서울시내 모든 대학교 개수 %d 개' %int (uni_count))


#(3) 위결과 csv파일저장
file=open('대학교_서울.csv','w',encoding='utf-8')
file.write(uni_info)
file.close()


