
# list
list = ['사과','딸기','포도','배','키위','바나나']
print(type(list))
print(list)
print(list[0])

# tuple
t = ('red','orange','yellow','green','blue','navy','violet')
print(type(t))
print(t)
print(t[0])

for i in t:
    print(i,end=' ')

# dictionary : { 'key' : 'value' }
dic = {'애플' : 'www.apple.com',
       '구글' : 'www.google.com',
       '네이버' : 'www.naver.com'}

print(type(dic))
print(dic)
print(dic['애플'])

print(k,':',v)
for k, v in dic.items():
    pass