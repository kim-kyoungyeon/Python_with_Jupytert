import bs4
import time
from bs4 import BeautifulSoup
html=""" <html><head></head><p>test</p></html>"""
soup= BeautifulSoup(html,'lxml')
print(soup)
time_sum=0
loop_count =5
for i in range(0,loop_count): #반복문 loop_count 변수생성
    start_time = time.time()
    BeautifulSoup(html,'lxml')
    lxml_end_time= time.time() - start_time

    start_time=time.time()
    BeautifulSoup(html,'html5lib') #
    html5lib_end_time=time.time() -start_time
    rate= html5lib_end_time/lxml_end_time

    print("%d 번째 시도"%(i)) #정수형
    print('lxml 시간측정 : %f '%(lxml_end_time)) #실수형 참조자 endtime
    print('html5lib시간측정 :%f'%(html5lib_end_time))
    print('**',rate,'**\n')
    time_sum+=rate # #시간 합계 = rate


    average= time_sum / loop_count
    print('평균속도 : %f'%(average))