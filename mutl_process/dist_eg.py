__author__ = 'admin'
D = {}
D = {'spam':2 , 'eggs':3 }
print D
D =  {'food':{'ham':1, 'egg':2}}
print D
print D['food']['ham']
D = dict(name='Bob', age=42)
print D
print D.keys()
print D.values()
print D.items()
print dict(D.items())
D1 = D.copy()
print D1
print D.get('age',5566)
del D['age']
print D.get('age',5566)
print D.pop('name')

print D
#{}
D2 = {'wife':'laopo', 'height':80}
D.update(D2)
print D
print D2.keys()
# {'wife': 'laopo', 'height': 80}
# ['height', 'wife']

D = {x: x*2 for x in range(10)}
print D
print len(D)
print list(D.keys())
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
# 10
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

D['ham'] = ['grill', 'bake', 'fry']
print D
# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 'ham': ['grill', 'bake', 'fry']}


D3 = {'name':'cluo', 'age':26}
print D3.items()
print list(D3.items())
#[('age', 26), ('name', 'cluo')]
#[('age', 26), ('name', 'cluo')]

D3.pop('age')  #dict.pop(key1)
print D3
#{'name': 'cluo'} pop改变了字典

#密码匹配
Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(6, 7, 8)] = 99
x,y,z = 2,3,4
print Matrix[(x,y,z)]
# 88
# 88


if (2,3,4) in Matrix:
	print(Matrix[(2,3,4)])
else:
	print(0)
#相当于
try:
	print(Matrix[(2,3,6)])
except KeyError:
	print(0)
#相当于
print Matrix.get((2,3,6),0) # dict.get(key,'default')

print dict(name='mel', age=45)
#{'age': 45, 'name': 'mel'}

print dict([('name','mel'),('age', '45')])
#{'age': '45', 'name': 'mel'}

print dict.fromkeys(['a','b','c'],0)
#{'a': 0, 'c': 0, 'b': 0}
print list(zip(['a','b','c'],[1,2,3]))
#[('a', 1), ('b', 2), ('c', 3)]
print dict(zip(['a','b','c'],[1,2,3]))
#{'a': 1, 'c': 3, 'b': 2}

D = {x: x ** 2 for x in [1, 2, 3, 4]}
print D
#{1: 1, 2: 4, 3: 9, 4: 16}


D = {c: c*4 for c in 'SPAM'}
print D
#{'A': 'AAAA', 'P': 'PPPP', 'S': 'SSSS', 'M': 'MMMM'}


# expression for args in list if condition
D = {c.lower():c +'!' for c in ['Spam','Eggs','Ham']}
print D
#{'eggs': 'Eggs!', 'ham': 'Ham!', 'spam': 'Spam!'}


#初始化key并设置默认值
D = dict.fromkeys(['a','b','c'],0)
print D
#{'a': 0, 'c': 0, 'b': 0}

#相当于
D = {k:0 for k in ['a','b','c']}
print D
#{'a': 0, 'c': 0, 'b': 0}

D = dict(a=1,c=3,b=2)
print D
#{'a': 1, 'c': 3, 'b': 2}

K = D.keys()
k = K.sort()
print K
#['a', 'b', 'c']
for k in K:
	print(k,D[k])
# ('a', 1)
# ('b', 2)
# ('c', 3)

D = {'g':1,'b':2,'a':3}
for k in sorted(D):print(k,D[k])
#排序后
# ('a', 3)
# ('b', 2)
# ('g', 1)