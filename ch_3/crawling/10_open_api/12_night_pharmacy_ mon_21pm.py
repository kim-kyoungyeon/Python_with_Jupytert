#월요일 밤 9시 이후에도 문을 여는 서울의 모든 심야 약국 조사
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote #한글 코드 가져오기

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"

serviceKey="Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D"
Q0= quote('서울특별시') #주소 시도 한글인코딩

ORD= 'NAME' # 순서
pageNo= '1' #현재 페이지 번호
startPage="1" #시작페이지
numOfRows='4817' #한페이지의결과수
pageSize= "100" #페이지크기
paramset= "serviceKey="+serviceKey+"&" \
          + "Q0=" + Q0 + "&" \
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
#print(items)
count = 0 #여기 count왜함?
n= 0
for item in items:
    monday_close_time= item.find("dutytime1c") # 월요일 운영하는 약국
    if monday_close_time != None:
        close_time= int(monday_close_time.text)
        if (close_time >2100): # 21시간에 문을 닫는다?
            count+=1 #파이썬 문자열 메소드 중 하나 부분문자열의 개수를 세는 메소드
            n += 1 #앞에 숫자붙이는 함수
           # print(n,item.find('dutyname').text,monday_close_time.text )
print("월요일 밤 9시 이후까지 운영하는 약국수" + str(count))


#print(items)
# for item in items:
#         name= item.find('dutyname')
#         print(name.text)
    #옆에 주소 출력

# #items= bs_obj.findAll('item')
# #print(items)
# for item in items:
#         name= item.find('dutyname').text
#         night_time=item.find("dutytime1c")
#         if night_time >= '2100':
#             print(name,night_time) #+로 연결하면 바로 이어진다.
# items= bs_obj.findAll('item')
# print(items)
