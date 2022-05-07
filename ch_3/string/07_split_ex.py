#Q. 그림과 같이 입력 받고 split()을 사용하여 분리

birth = input('생일 입력(연/월/일) : ')
birth_list = birth.split('/')

print('당신은 %s 년에 태어났고' % birth_list[0] + '\n' +
      '생일은 %s 월 %s 일 입니다.' % (birth_list[1],birth_list[2]))
