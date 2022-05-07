#서울의 모든약국추출
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote #한글 코드 가져오기

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"

serviceKey="Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D"
Q0= quote('서울특별시') #주소 시도 한글인코딩
ORD= 'NAME' # 순서
pageNo= '1' #현재 페이지 번호
startPage="1" #시작페이지
numOfRows='5000' #한페이지의결과수
# pageSize= "100" #페이지크기
paramset= "serviceKey="+serviceKey+"&"\
            +"Q0="+Q0+"&"\
            +'ORD='+ORD+'&'\
            +'pageNo='+pageNo+'&'\
            +'startPage=' +startPage+'&'\
            +'numOfRows='+numOfRows
            # +'pageSize='+pageSize
url= endpoint+paramset
print(url)
result= requests.get(url)
bs_obj=BeautifulSoup(result.content, 'html.parser')
#print(bs_obj)
items= bs_obj.findAll('item')
print(items)
for item in items:
        name= item.find('dutyname')
        print(name.text)
    #옆에 주소 출력

items= bs_obj.findAll('item')
print(items)
for item in items:
        name= item.find('dutyname').text
        address=item.find("dutyaddr").text
        print(name+","+address) #+로 연결하면 바로 이어진다.
items= bs_obj.findAll('item')
print(items)