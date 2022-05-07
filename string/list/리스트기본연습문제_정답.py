# 01
#
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 리스트에 저장하라. (순위 정보는 저장하지 않는다.)
#
#
# 순위   영화#
#
# 1      닥터 스트레인지
# 2      스플릿
# 3      럭키
movie_rank = ["닥터 스트레인지","스플릿","럭키"]


# 02
#
# 041의 movie_rank 리스트에 "배트맨"을 추가하라.
movie_rank.append("베트맨")



# 03
#
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1,"슈퍼맨")



# 04
#
# movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
movie_rank.remove('럭키')
del movie_rank[3]


# 05
#
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[2:]

#또는
movie_rank.remove('스플릿')
movie_rank.remove('배트맨')




# 06
#
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2 #리스트 연결 연산자는 하나의 리스트로 결합
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']




# 07
#
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
nums = [1, 2, 3, 4, 5, 6, 7]
#
# 실행 예:
# max:  7
# min:  1
print("max : ",max(nums))
print("min : ",min(nums)


# 08
#
# 다음 리스트의 합을 출력하라.
nums = [1, 2, 3, 4, 5]
#
# 실행 예:
# 15
print(sum(nums))


# 09
#
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
cook = ["피자", 김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))


# 10
#
# 다음 리스트의 평균을 출력하라.
nums = [1, 2, 3, 4, 5]
#
# 실행 예:
# 3.0
print(sum(nums)/len(nums))

# 11
#
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
#
# 출력 예시:
# [100, 130, 140, 150, 160, 170]
print(price[1:7])
print(price[1:]) #끝 인덱스 생략 가능




# 12
#
# 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# 실행 예:
# [1, 3, 5, 7, 9]
print(nums[::2])] #마지막 숫자는 증가감 의미




# 13
#
# 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# 실행 예:
# [2, 4, 6, 8, 10]
print(nums[1::2])]



# 14
#
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
#
# 실행 예:
# [5, 4, 3, 2, 1]
print(nums[::-1])


# 15
#
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
#
#
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver
print(interest[0], interest[2])



# 16
#
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#
#
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
print(' '.join(interest))



# 17
#
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#
#
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
print('/'.join(interest))



# 18
#
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
#
#
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우
print('\n'.join(interest))

for i in interest :
    print(i)



# 19
#
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
string = "삼성전자/LG전자/Naver"
#
#
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

interest = string.split("/") #split 함수는 결과로 list 반환



# 20
#
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우"
#
#
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest = string.split("/") #split 함수는 결과로 list 반환


# 21
# 다음 코드의 결과값에 대해 예측하여라
# interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_1 = interest_0 #얕은 복사가 발생
# interest_1[0] = 'Naver'
# print(interest_0)
#얕은복사로 인해서 interest_1과 interest_0이 동일한 주소를 갖게됨
#interest_1의 요소값을 수정하면 interest_0도 같은 값을 참조하게 됨
#실제 두 변수가 참조하는 값이 수정된 결과로 나타남
['Naver', 'LG전자', 'SK Hynix']


#22
# 다음 코드의 결과값에 대해 예측하여라
# interest_0 = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_1 = interest_0[:2] #깊은복사 발생, 값을 가져와서 새로 interest_1 리스트 생성
# interest_1 =['삼성전자', 'LG전자', 'SK Hynix']의미와 같다.
# interest_1[0] = 'Naver'
# print(interest_0)
#interest_1의 요소를 변경해도 interest_0번의 값은 변하지 않는다
# 두 변수는 서로 다른 주소를 참조 하게 됨

