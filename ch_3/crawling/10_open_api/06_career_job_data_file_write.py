#api 를 통해서 얻은 데이터를 파일로 저장
#커리어넷 진로 직업정보
#연봉이 4000만원 이상인 직업 중에서
#직업 구성 분포 확인 (직업 분류수)

import requests
endpoint= "http://www.career.go.kr/cnet/openapi/getOpenApi?"
apiKey= "dcc2db5b377c881a9328b3e764f2ad3d"
svcType= "api"
svcCode= "JOB"
contentType="json" #커리어넷 기본정보
gubun="job_dic_list"
perPage='10000'

paramset= "apiKey="+apiKey +"&" \
        + "svcType="+svcType +"&"\
        + 'svcCode=' +svcCode+"&"\
        + 'contentType='+contentType+"&"\
        +'gubun='+gubun+"&"\
        + 'perPage='+perPage

url= endpoint+paramset
#print(url)
result= requests.get(url)
career_data= result.json()

#현재 디렉터리(./)에 추가
# f =open('./job_api_data.json','w',encoding='utf-8')
f =open('job_api_data2.json','w',encoding='utf-8')
f.write(str(career_data))
f.close()
