# 반복문 : while문
# while 조건식 :
#       조건식이 참인 경우에 실행될 문장

# 구구단을 모두 출력
dan=2;i = 1
while dan <=9:
    print('[',dan,'단]')
    while i <= 9:
        print('{0} * {1} = {2}'.format(dan,i,dan*i))
        i += 1
    dan += 1
    i = 1