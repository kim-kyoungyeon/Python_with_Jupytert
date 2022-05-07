import bs4

html=""""""

soup=bs4.BeautifulSoup(html,'lxml')
#bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
# 오류 메시지 pip 터미널창으로 가서 깔아주기
# lxml 은 xml 해석이 가능한 파서


