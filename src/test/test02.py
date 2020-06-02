# 과제
#
# 반복문 for문을 이용해서 구구단(2~9단)을  각 단별로 세로로 출력하는 프로그램을
# 작성하세요?
for x in range(2,10):
    print('[',x,'단]',end='\t\t')
    if x == 9:
        print()
        x += 1
x = 1
for i in range(1,10):
    for j in range(2,10):
        print('{0} * {1} = {2}'.format(j,i,i*j),end='\t')
        if j == 9:
            i = 1
            print()
