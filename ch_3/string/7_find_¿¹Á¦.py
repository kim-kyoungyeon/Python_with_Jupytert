# Q. 대한민국 광역시도를 문자열로 저장하고, 사용자로부터 광역시도를 입력받아 입력이 올바른지 확인하는 프로그램
# find() 함수 이용할 것

cities = '인천 대전 광주 울산 대구 부산 경기 서울 충남 충북 강원 전북 전남 경남 경북 제주'

city = input('우리나라 광역시도 중 하나 입력 : ')

if cities.find(city) != -1 :
    print('정답입니다.')
else :
    print('틀렸습니다.')

if city in cities :
    print('정답입니다.')
else :
    print('틀렸습니다.')