# BMI = 몸무게/키의 제곱
kg=float(input('몸무게(킬로그램): '))
m=float(input('키(미터): '))
BMI=kg/m**2
input('당신의 BMI: %.2f' % BMI)