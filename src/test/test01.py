# 과제.
#       1.
#       1 ~ 12월 중에서 달(Month)에 'r'이 들어있는 달(Month)을 출력하는 프로그램을
#       작성 하세요?


months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
# result = 0
# print(' *r이 포함된 달')
# for i in months:
#     result = result + 1
#     if 'r' in i:
#         print(i)
#-----------------------------
# for month in months:
#     if 'r' in month.lower():
#         print(month)
#----------------------------------
for month in months:
    if month.count('r')>0:
        print(month)

#      2.
#        키보드로 3개의 정수를 입력 받았을때, 입력한 값 중에서 최대값과 최소값을 구하는
#        프로그래을 작성하세요? (단, if  else 문을 이용하세요?)
print('\n *3개의 정수를 입력하세요')
#       1번째 방법 --------------------------------------------
# list = [1,2,3]
# for i in range(len(list)):
#     print(list[i],end=' ');print('번째 정수를 입력하세요')
#     list[i] = int(input())
#
# print(list)
# print('max = ',max(list))
# print('min = ',min(list))

#        2번째 방법 --------------------------------------------
# list = [1,2,3]
# list[0] = int(input('1번째 정수를 입력하세요'))
# list[1] = int(input('2번째 정수를 입력하세요'))
# list[2] = int(input('3번째 정수를 입력하세요'))
# list.sort()
# print('min = ',list[0])
# print('max = ',list[2])

#        3번째 방법 --------------------------------------------
n1 = int(input('1번째 정수를 입력하세요'))
n2 = int(input('2번째 정수를 입력하세요'))
n3 = int(input('3번째 정수를 입력하세요'))

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
