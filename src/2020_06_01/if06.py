# 조건문 : if ~ elif ~ else문
# if 조건식1 :
#           실행문장
# elif :
#           실행문장
# else :
#           위의 조건식을 만족하지 않을 경우에 실행될 문장

n1 = int(input('정수1을 입력하세요'))
n2 = int(input('정수2을 입력하세요'))
n3 = int(input('정수3을 입력하세요'))

if n1>=n2 and n1>=n3:
    max = n1
elif n2>=n3 and n2>=n3:
    max = n2
else:
    max = n3
if n1<=n2 and n1<=n3:
    min = n1
elif n2<=n3 and n2<=n3:
    min = n2
else:
    min = n3
print('[',n1,n2,n3,']')
print('min = ',min)
print('max = ',max)
