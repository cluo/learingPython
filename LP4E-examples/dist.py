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
D2 = {'wife':'laopo', 'height':80}
D.update(D2)
print D

print D2.keys()

D = {x: x*2 for x in range(10)}
print D
print len(D)
print list(D.keys())
D['ham'] = ['grill', 'bake', 'fry']
print D

D3 = {'name':'cluo', 'age':26}
print D3.items()
print list(D3.items())

D3.pop('age')
print D3

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(6, 7, 8)] = 99
x,y,z = 2,3,4
print Matrix[(x,y,z)]

if (2,3,4) in Matrix:
	print(Matrix[(2,3,4)])
else:
	print(0)

try:
	print(Matrix[(2,3,6)])
except KeyError:
	print(0)

print Matrix.get((2,3,6),0)

print dict(name='mel', age=45)
print dict([('name','mel'),('age', '45')])

print dict.fromkeys(['a','b','c'],0)
print list(zip(['a','b','c'],[1,2,3]))
print dict(zip(['a','b','c'],[1,2,3]))
D = {x: x ** 2 for x in [1, 2, 3, 4]}
print D
D = {c: c*4 for c in 'SPAM'}
print D
D = {c.lower():c +'!' for c in ['Spam','Eggs','Ham']}
print D
D = dict.fromkeys(['a','b','c'],0)
print D
D = {k:0 for k in ['a','b','c']}
print D
D = dict(a=1,c=3,b=2)
print D

K = D.keys()
k = K.sort()
print K
for k in K:print(k,D[k])

D = {'g':1,'b':2,'a':3}
for k in sorted(D):print(k,D[k])

