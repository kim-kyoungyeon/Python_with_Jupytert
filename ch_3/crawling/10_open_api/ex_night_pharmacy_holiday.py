#강남구에서 공휴일에 문을 여는 약국 추출
#번호 약국명 주소, 진료시간
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote #한글 코드 가져오기

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"
serviceKey="Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D"
Q0= quote('서울특별시') #주소 시도 한글인코딩
Q1= quote('강남구')
ORD= 'NAME' # 순서
pageNo= '1' #현재 페이지 번호
startPage="1" #시작페이지
numOfRows='4817' #한페이지의결과수
pageSize= "100" #페이지크기
paramset= "serviceKey="+serviceKey+"&" \
          + "Q0=" + Q0 + "&" \
          + 'Q1='+Q1+'&'\
          + 'ORD=' + ORD + '&' \
          + 'pageNo=' + pageNo + '&' \
          + 'startPage=' + startPage + '&' \
          + 'numOfRows=' + numOfRows + '&' \
          + 'pageSize=' + pageSize
url= endpoint+paramset
print(url)

result= requests.get(url)
bs_obj=BeautifulSoup(result.content, 'html.parser')
#print(bs_obj)
items= bs_obj.findAll('item')

# n= 0
#
# for item in items:
#     holiday_time= item.find('dutytime8s')
#     if holiday_time !=None:
#         n +=1
#         name =  item.find('dutyname').text
#         address=item.find('dutyaddr').text
#1600>>16:00으로 바꾸기 09:00으로 바꿔보자
#         holiday_time= holiday_time.text[0:2]\
#             +":"+holiday_time.text[2:]#문자열은 [start,end] start에서 end -1 까지
#         # 2에서 부터 끝까지
#         print(n, ",",name,address,",",holiday_time)



n=0
for item in items:
    hol_start_time= item.find("dutytime8s")# 공휴일 오픈하는 약국
    if hol_start_time != None:
        n += 1 #앞에 숫자붙이는 함수
        address = item.find("dutyaddr").text
        hol_start_time =hol_start_time[0:2]+":"+hol_start_time[2:]
        print(n,item.find('dutyname').text,",",address, hol_start_time)


# 질문: 48번째 줄에서 hol_start_time= item.find("dutytime8s").text를 붙이면 실행이되지 않습니다.
#AttributeError: 'NoneType' object has no attribute 'text'
#라는 오류가 뜨구요,
# 48번째에 그대로 text없이 처리한후, 52번째 주석처리되어있는것을 풀면 또 정상 실행되는데 이유가 뭘까용?