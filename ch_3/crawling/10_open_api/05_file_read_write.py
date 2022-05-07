# api 통해서 얻은 데이터를 저장하고 활용하기
# 파일 입출력을 이용해서 api로 얻은 결과를 저장하고 이용하는 프로그램을 작성
# (1) api에서 얻은 json 데이터를 로컬에 저장하는 프로그램
# (2) json 데이터를 불러와서 원하는 대로 처리하는프로그램
# 실제 서비스에서는 대량의 데이터를 데이터베이스에 저장하고 쿼리(Query)라고 부르는 검색작업을 통해 저장된
# 데이터를 검색할 수 있도록 시스템을 구성한다.
#파일 입출력
#쓰기 모드 파일 열기
#파일이 존재하지 않으면 새로 생성하고
#존재하면 내용덮어씀


# 파일 경로
# (1) 절대경로 : 드라이브명부터 파일명까지 전체경로 "C:/PythonStudy/crawling/10_open_api/test_data.txt"
#
# (2) 상대경로: 현재 디렉터리 기준"./job_api_data.json"
# 파일생성하고 데이터 저장 (쓰기_)#쓰기노드
f= open("C:/PythonStudy/crawling/10_open_api/test_data.txt",'w')
data="easy_python_crawler"
f.write(data)
f.close()
# 읽기 모드로 파일열고 출력
f = open("C:/PythonStudy/crawling/10_open_api/test_data.txt",'r')
#덮어쓰기
#끝에 추가 하기 append
for str in f. readlines():
    print(str)
f.close()





































