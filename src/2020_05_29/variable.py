# 변수 : 메모리상에 데이터를 저장하기 위한 기억 공간의 이름
# 변수 만드는 형식 :   변수명 = 값(데이터)

# 정수형 변수
i = 10
print("i=",i)

# 실수형 변수
r=3.14
print(type(r))
print('r=',r)

# 복소수형 변수
c = 3 + 5j
print(type(c))
print('c=',c)

# 논리형 변수
b1 = True
b2 = False
print('b1=',b1)
print('b2=',b2)
print(type(b1))
print(type(b2))

# 문자형 변수
s1 = '파이썬'
s2 = 'python'
print(type(s1))
print(type(s2))

# 리스트(list)
list = ['빨','주','노','초','파','남','보']
print(type(list))
print(list[0])
list[0] = 'red'
print(list[0])
print('list=',list)

# 튜플(tuple)
t = ('red','orange','yellow','green','blue','navy','purple')
print(type(t))
print(t[0])
# t[0] = '빨강'           # 튜플은 원소의 값을 수정할 수 없다.
print('t=',t)
print(type('red'))

# 집합(set)
s = set([1,2,3])
print('s=',s)
print(type(s))

# 딕셔너리(dictionary) : { 'key' : 'value' }
d = {'네이버' : 'http://www.naver.com',
     '구글' : 'http://www.google.com',
     '애플' : 'http://www.apple.com'}
print('d=',d)
print(type(d))
