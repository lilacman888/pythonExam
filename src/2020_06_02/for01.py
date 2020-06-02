# 반복문 : for문
# for 변수 in range():
#       반복 실행할 문장

# range() 함수
# range(초기값, 최종값, 증감값) : 초기값 ~ 최종값 -1 까지 증감
for i in range(1,10,2):
    print(i,end= '  ')              # 1  3  5  7  9
# range(초기값, 최종값) : 초기값 ~ 최종값 -1 까지
for i in range(5,10):
    print(i,end='  ')               # 5  6  7  8  9
# range(최종값) : 0 ~ 최종값 -1까지
for i in range(10):
    print(i, end='  ')              # 0  1  2  3  4  5  6  7  8  9
