# (1) 정보 통신과 관련있는 직업군을 찾고
# 해당 직업군의 직업명과 코드출력
#직업군,코드,직업명
# 정보통신 이 어디에 있는지 content['profession']에 들어있으면 content['profession']에서 추출

# (2) 정보통신 관련 직업의 평균연봉구해서 출력
# for 문에서 각 연봉구해서 다 더한다음(total) for문 밖에서 평균 구해서(average)출력
# 평균구하기 total/ 개수
# 개수는 어떻게 구하나? for 문에서 카운트세기
## for문 안에서 구할것
#   직업군. 코드.직업명 변수에 저장 (누적) (job_info)
#   `총 연봉 금액 (salary_total)
#   해당 직업군 개수(job_count)
#for 문 종료 후
#   평균 연봉 계산 :
#   출력
#(3) (1)번결과를 csv 파일로 저장

import requests
from urllib.parse import urlparse
import json
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
print(url)
result= requests.get(url)
career_data= result.json()

career_list=career_data ['dataSearch']['content']
#1
## 정답
job_info= "" #문자열 "" , : 직업군,코드,직업명 저장할 변수
salary_total= 0  #연봉총액
job_count = 0 # 해당 직업 개수 (평균 연봉 구할때 사용)

for content in career_list : #content를 뽑아서 careerlist에 넣음
    if content['profession'] !='null':#직업군 추출하기
        #print(type(content['profession']))
        #'정보통신'들어있는 경우
        if '정보통신' in content['profession'] :
        # if content['profession'].find('정보통신') >= 0 : #'str' 문자열 (결과는 위 if 조건과 동일함. 같은 함수)
        #if content['profession'].find('정보통신') != -1 #문자열 -1  파이썬find 함수 공부하기
            if content['salery'] != 'null':
                salary_total+=int(content['salery'].split(" ")[0])
                job_count+=1
            prof = content['profession']
            job_code=content['job_code']
            job_name =content['job']
            job_info += prof+','+job_code+','+job_name +"\n"
print(job_info)
print(job_count)

# (2) 정보통신 관련 직업의 평균연봉구해서 출력
# for 문에서 각 연봉구해서 다 더한다음(total) for문 밖에서 평균 구해서(average)출력
job_avg=salary_total/job_count
print('정보통신관련 직업의 평균연봉 %d 원' %int (job_avg))

#(3) 1번결과 csv파일저장
file=open('정보통신 _관련_직업.csv','w',encoding='utf-8')
file.write(job_info)
file.close()


#
# for career in career_list:
#     if career['job_ctg_code'] =="105098":
#         print(career['profession'],career['job'],career['job_ctg_code'])
# #2
#
# for career in career_list:
#     if career['job_ctg_code'] =="105098":
#         print(career['salery'])
#
# salary_count=0
# for career in career_list:
#     if career['salery'] != 'null' :
#         print(career['salery'])
#         if int(career['salery'].split(' ')[0])>=0:
#             salary_count += 1
#
# print('연봉직업의 수',salary_count)

# f= open("C:/PythonStudy/crawling/10_open_api/ex_career.csv",'w')
# data= career_list
# f.write(data)
# f.close()