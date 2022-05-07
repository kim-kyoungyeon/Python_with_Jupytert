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
career_list=career_data ['dataSearch']['content']
#print(career_list)
salary_4000_count=0
salary_4000_profession = {} # {'직업 분류코드': 개수}

for career in career_list :
    if career['salery'] != 'null':
        if int(career['salery'].split(' ')[0]) >= 4000:
            salary_4000_count +=1

            key_tmp =career['job_ctg_code'] #직업분류코드
            # print(key_tmp)
#salary_4000_profession 딕셔너리에 추가
#key : key_temp 직업분류코드



            if key_tmp in salary_4000_profession :
                salary_4000_profession[key_tmp] +=1
            else:
                salary_4000_profession[key_tmp] =1
            # key_tmp가 딕셔너리에 없으면 새로추가

            # 이후 key_tmp는 추가되지 않고 값만 1씩추가
print("연봉이 4000만원이상인 직업의 수: "+str(salary_4000_count))
print('직업 분류 수:'+str(len(salary_4000_profession)))
print(salary_4000_profession)

# 연봉 4000만원 이상인 직업중 가장 많은 직업분류코드
max = 0 #최대 value
majority = "" #최대  value의 직업코드


#prof 하나가 직업 분류코드
for prof in salary_4000_profession:
    tmp=salary_4000_profession[prof] # tmp: 값
    print(prof+':'+str(tmp))
    if max < tmp:
        max = tmp
        majority = prof

print('연봉이 4000만원 이상인 직업중 가장 많은 직업 분류 코드:',majority)

