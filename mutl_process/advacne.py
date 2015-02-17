__author__ = 'admin'
L1 = [1,2,3,4]
L2 = [6,7,8,9]
print zip(L1,L2)
print list(zip(L1,L2))
# [(1, 6), (2, 7), (3, 8), (4, 9)]
# [(1, 6), (2, 7), (3, 8), (4, 9)]

for(x, y) in zip(L1,L2):
	print(x,y ,'--',x+y)

# (1, 6, '--', 7)
# (2, 7, '--', 9)
# (3, 8, '--', 11)
# (4, 9, '--', 13)

T1, T2, T3 =(1,2,3),(4,5,6),(7,8,9)
print T3
print list(zip(T1,T2,T3))
# (7, 8, 9)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

S1 = 'abc'
S2 = 'xyz123'
print list(zip(S1,S2))
# [('a', 'x'), ('b', 'y'), ('c', 'z')]

print list(map(ord,'spam'))
# [115, 112, 97, 109]

D1 = {'spam':1, 'egg':3 ,'toast':5}
print D1
# {'toast': 5, 'egg': 3, 'spam': 1}


D1={}
D1['spam'] = 1
D1['egg'] = 3
D1['toast'] = 5
print D1
# {'toast': 5, 'egg': 3, 'spam': 1}



keys = ['spam', 'egg', 'toast']
vals = [2, 3, 4]
print zip(keys,vals)
print dict(zip(keys,vals))
# [('spam', 2), ('egg', 3), ('toast', 4)]
# {'toast': 4, 'egg': 3, 'spam': 2}

#相当于
D2 = {}
for (k, v) in zip(keys, vals):
	D2[k] = v
print D2
# {'toast': 4, 'egg': 3, 'spam': 2}


S = 'spam'
for (offset, item) in enumerate(S):
	print(item, 'appears at offset', offset)

# ('s', 'appears at offset', 0)
# ('p', 'appears at offset', 1)
# ('a', 'appears at offset', 2)
# ('m', 'appears at offset', 3)







