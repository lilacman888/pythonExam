# 반복문 : for문
# for 변수 in range():
#       반복 실행할 문장

# 1 ~ 100까지 홀수의 합과 짝수의 합을 구하는 프로그램을 작성
sum = 0
for i in range(2,101,2):
    sum+=i
    print(i)

print('2의 배수의 합 : ',sum)
