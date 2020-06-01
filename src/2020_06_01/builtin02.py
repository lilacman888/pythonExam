# 내장 함수 : input(), int()
# input() : 키보드로 입력을 받는 경우에 사용하는 내장함수
# int() : 문자형을 정수형으로 변환해주는 내장함수

name = input('이름을 입력하세요')
age = int(input('나이을 입력하세요'))

print(type(name))
print(type(age))

if age >= 20:
    print('성인입니다.')
else:
    print('미성년입니다.')
