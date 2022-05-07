from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import pandas
import time
import selenium.webdriver.common.keys


url="http://finance.daum.net/news/20200730170214862"
web=requests.get(url).content
source= BeautifulSoup(web,'html.parser')
urls_list=[]
# 파싱해서 각 뉴스의 기존 url을 수집하고자 했다.
#공통부분추출하여 차이나는 코드만 이어붙이기
for urls in source. find_all('a',{'class':'f_link_b'}):
    new_url_content=urls['href'][-21:-4]
    print(new_url_content)
    new_url="http://finance.daum.net/news/"+new_url_content
    urls_list.append(new_url)
urls_list

#selenium
driver = webdriver.Chrome('C:\PythonStudy\driver\chromedriver.exe')
html = driver.execute_script('return document.body.innerHTML')
contents_list=[]
for i in range (10):
    driver.get(urls_list[i])
    print(driver.current_url)

    time.sleep(3)
    try:
        #댓글더보기 클릭//*[@id="alex-area"]/div/div/div/div[3]/div[2]/a
        #while driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[1]/div[4]/div/div/div/div/div[3]/div[1]/button/span[1]').text!="":
        while driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[2]/a').text!="":
            driver.find_element_by_xpath('//*[@id="alex-area"]/div/div/div/div[3]/div[2]/a').click()
         #driver.find_element_by_xpath('/html/body/div/div[3]/div[3]/div[1]/div[4]/div/div/div/div/div[3]/div[1]/button/span[1]').click()
        time.sleep(3)
    except:
        pass
    time.sleep(2)


    for k in range(40):
        try:
            contents = driver.find_element_by_xpath(
                "/html/body/div/div[3]/div[3]/div[1]/div[4]/div/div/div/div/div[3]/ul[2]/li[1]/div/p"
            ).text
            contents=contents.replace("\n","")
            contents_list.append(contents)
        except:
            pass
        time.sleep(3)

