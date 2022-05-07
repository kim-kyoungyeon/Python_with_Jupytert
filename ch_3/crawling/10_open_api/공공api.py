# 커리어넷 진로 직업 정보 : 데이터 구조 확인

import requests

endpoint = "http://www.career.go.kr/cnet/openapi/getOpenApi?"
apiKey = "fd5cd444a879fd9ca0c54ea676f4da1a"
svcType = "api"
svcCode = "JOB"
contentType = "json"
gubun = "job_dic_list" # 커리어넷직업분류별
perPage = "10000"

paramset = "apiKey=" + apiKey + "&" \
           + "svcType=" + svcType + "&" \
           + "svcCode=" + svcCode + "&" \
           + "contentType=" + contentType + "&" \
           + "gubun=" + gubun + "&" \
           + "perPage=" + perPage

url = endpoint + paramset
print(url)

result = requests.get(url)
career_data = result.json()
print(career_data)


