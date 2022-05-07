#105100에 어떤 직업카테고리가 있는지 확인
#연봉이 4000만원 이상인 직업중에서
#가장 많은직업코드인 105100에 해당되는 직업확인

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
career_list=career_data ['dataSearch']['content']
#print(career_list)

#직업분류코드 _ 직업명 연봉
for career in career_list:
    if career['job_ctg_code'] == '105100':
        print(career['job_ctg_code'],career['job'],career['salery'])



































