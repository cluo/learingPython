__author__ = 'admin'
T = (0, 'Ni',('a', 'b'), 1.2 , 3)
print T[2]
print T + T[2]
for x in T:
	print(x)
print 'Ni' in T
print [x*2 for x in T]
print T.index('Ni')
print T.count('Ni')

T = (1,2) + (3,4)
print T
print (1,2) * 4
T = (1, 2, 3, 4)
print T[0],T[1:3]
T = ('cc', 'aa' ,'dd' ,'bb')
tmp = list(T)
print tmp
tmp.sort()
print tmp
T = tuple(tmp)
print sorted(T)

T = (1, 2, 3, 2, 4, 5)
L = [x + 20 for x in T]
print L
print T.index(2)
print T.index(2, 2)
print T.count(2)

print type([1]) == type([])
print type([1]) == list
print isinstance([1], list)

L = [1 ,2 ,3]
m = ['X', L, 'Y']
print m

L[1] = 0
print m

L = [1 ,2 ,3]
m = ['X', L[:], 'Y']
L[1] = 0
print m

L = [4, 5, 6]
X = L * 4
print X

Y = [L] * 4
print Y

