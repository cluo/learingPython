__author__ = 'admin'
L1 = [1,2,3,4]
L2 = [6,7,8,9]
print zip(L1,L2)
print list(zip(L1,L2))

for(x, y) in zip(L1,L2):
	print(x,y ,'--',x+y)

T1, T2, T3 =(1,2,3),(4,5,6),(7,8,9)
print T3
print list(zip(T1,T2,T3))
S1 = 'abc'
S2 = 'xyz123'
print list(zip(S1,S2))

print list(map(ord,'spam'))
D1 = {'spam':1, 'egg':3 ,'toast':5}
print D1

D1={}
D1['spam'] = 1
D1['egg'] = 3
D1['toast'] = 5
print D1

keys = ['spam', 'egg', 'toast']
vals = [2, 3, 4]
print zip(keys,vals)
print dict(zip(keys,vals))
D2 = {}
for (k, v) in zip(keys, vals):D2[k] = v
print D2

S = 'spam'
for (offset, item) in enumerate(S):
	print(item, 'appears at offset', offset)