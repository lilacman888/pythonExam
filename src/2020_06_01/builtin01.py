# 내장 함수

# 최대값 : max()
print(max(10, 20))                  # 20
print(max(10,20,30,40,50))          # 50
print(max([10,20,30,40,50]))        # 50
print(max('hello word'))            # w

# 최소값 min()
print(min(10,20,30))                # 10
print(min([10,20,30,40,50]))        # 10

# range() 함수
# range(초기값, 최종값, 증감값) : 초기값 ~ 최종값 -1 까지 증감
# range(초기값, 최종값) : 초기값 ~ 최종값 -1 까지
# range(최종값) : 0 ~ 최종값 -1까지
print(range(10))                    # range(0,10)

print(list(range(10)))              # 0 ~ 9 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10)))            # 1 ~ 9 [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1,10,2)))          # [1, 3, 5, 7, 9]

for i in range(1,11):
    print(i)                        # 1 ~ 10

for i in range(10):
    print(i)                        # 0 ~ 9

for i in range(10,1,-1):
    print(i)                        # 10 ~2