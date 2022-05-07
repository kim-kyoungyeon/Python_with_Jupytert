# 서울 심야 약국 수 조사
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote #한글 코드 가져오기

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"

serviceKey="Svf%2F7KhRrhXVq41V4ZsZlS7Odrcq%2Fas1J3tfu9Kg%2BRJTy7tE21Ja1IKaSHUHzDPKswJAMGmYyWhr4EcqR1ue5Q%3D%3D"
Q0= quote('서울특별시') #주소 시도 한글인코딩
Q1= quote('강남구') # 지역주소 시군구 한글인코딩
QT= '1' #진료요일 (1월)
QN= quote('삼성약국')#기관명
ORD= 'NAME' # 순서
pageNo= '1' #현재 페이지 번호
startPage="1" #시작페이지
numOfRows='10' #한페이지의결과수
pageSize= "10" #페이지크기
paramset= "serviceKey="+serviceKey+"&"\
            +"Q0="+Q0+"&"\
            +'Q1='+Q1+'&'\
            +'QT='+QT +'&'\
            +'QN='+QN+'&'\
            +'ORD='+ORD+'&'\
            +'pageNo='+pageNo+'&'\
            +'startPage=' +startPage+'&'\
            +'numOfRows='+numOfRows+'&'\
            +'pageSize='+pageSize
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
