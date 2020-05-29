# 논리연산자
# 5과목의 점수를 입력 받아서 합격, 불합격을 판별하는 프로그램을 작성하세요
# 단. 과목당 과락은 40점이고, 평균 60점 이상이면 합격

# input() : 키보드로 입력을 받는 경우에 사용하는 함수
# int() : 문자를 정수형으로 형변환 해주는 함수
# n = input('점수를 입력하세요')
# print(n)
# print(type(n))
# n = int(n)              # 문자를 정수형으로 변환
# print(type(n))

n1 =int(input('점수1을 입력하세요'))
n2 =int(input('점수2을 입력하세요'))
n3 =int(input('점수3을 입력하세요'))
n4 =int(input('점수4을 입력하세요'))
n5 =int(input('점수5을 입력하세요'))

sum = n1 + n2 + n3 + n4 + n5
avg = sum/5
if n1>=40 and n2>=40 and n3>=40 and n4>=40 and n5>=40 and avg>=60:
    print('합격')
else:
    print('불합격')
print('총합 : ',sum)
print('평균 : ',avg)