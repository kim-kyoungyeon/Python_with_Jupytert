# 다음과 같이 리스트를 선언하고 각 학생의 총점과 평균을 출력
students = [
    {"name":"홍길동","korean":87,"english":88,"science":95,"math":98},
    {"name":"이몽룡","korean":92,"english":96,"science":98,"math":98},
    {"name":"성춘향","korean":76,"english":94,"science":90,"math":96},
    {"name":"변학도","korean":98,"english":96,"science":92,"math":92},
    {"name":"박지성","korean":95,"english":98,"science":98,"math":98},
    {"name":"류현진","korean":64,"english":92,"science":92,"math":88}
]
# students[0]['name']
# 반드시 반복문 이용할 것(for 문)

print()
print('이름','\t 총점','\t 평균')

for s in students :
    std_sum = s['korean']+s['math']+s['english']+s['science']
    std_avg = std_sum / 4

    print(s["name"],'\t',std_sum,'\t',std_avg)



















