# 반복문 : while문
# while 조건식 :
#       조건식이 참인 경우에 실행될 문장

# 1~100까지 홀수, 짝수의 합을 구하는 프로그램

i = 1; odd = even = 0
while i<=100:
    if i%2 == 0:
        even += i
    else:
        odd += i
    i += 1
print('1~100까지 홀수의 합 : ', odd)
print('1~100까지 짝수의 합 : ', even)