#커리어넷 진로 직업 정보 : 데이터 구조 확인
import requests
from urllib.parse import urlparse
import json

endpoint= "http://www.career.go.kr/cnet/openapi/getOpenApi?"
apiKey= "dcc2db5b377c881a9328b3e764f2ad3d"
svcType= "api"
svcCode= "JOB"
contentType="Json" #커리어넷 기본정보
gubun="job_dic_list"
perPage='10000'

paramset= "apiKey="+apiKey +"&" \
        + "svcType="+svcType +"&"\
        + 'svcCode=' +svcCode+"&"\
        + 'contentType='+contentType+"&"\
        + 'gubun='+gubun+"&"\
        + 'perPage='+perPage
url= endpoint+paramset
#print(url)
result= requests.get(url)
career_data= result.json()
print(career_data)
#data serach 출력

print(career_data['dataSearch'])
print(type(career_data['dataSearch']))

#contetn출력
print(career_data['dataSearch']['content'])
print(type(career_data['dataSearch']['content']))
#contetnt 갯술출력
print(len(career_data['dataSearch']['content']))
