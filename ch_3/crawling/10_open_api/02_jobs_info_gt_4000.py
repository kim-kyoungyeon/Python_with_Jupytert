#커리어넷 진로 직업정보
#연봉이 4000만원 이상인 직업 찾아보기
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
print(career_list)

salary_4000_count=0
for career in career_list:
    if career['salery'] != 'null' :
        print(career['salery'])
        if int(career['salery'].split(' ')[0])>=4000:
            salary_4000_count += 1
print('연봉이 4000만원 이상인 직업의 수'+str(salary_4000_count))
