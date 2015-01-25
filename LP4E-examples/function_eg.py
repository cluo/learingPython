__author__ = 'admin'
def mysum(L):
	if not L:
		return 0
	else:
		return L[0] + mysum(L[1:])

L = [1, 2 ,3 ,4 ,5]
print mysum(L)

def mysum(L):
	return 0 if not L else L[0] + mysum(L[1:])

L = [1, 2 ,3 ,4 ,5]
print mysum(L)

f = lambda x,y,z: x + y +z
print f(2,4,5)

x = (lambda a ='fee', b='fie', c='feo':a+b+c)
print x('wee')
print x(a='bb',b='cc',c='dd')
L = [lambda x:x ** 2,
	 lambda x:x ** 3,
	 lambda x:x ** 4]
for f in L:
	print(f(2))


key  = 'got'
map_fun = {
	'already':(lambda: 2 + 2),
	'got': (lambda : 2 *4 ),
	'one':(lambda:2 ** 6),
	'param':(lambda x: x**2)
}

print map_fun['got']()
print map_fun['one']()
print map_fun['param'](2)

s1 = 'abc'
s2 = 'xyz'

print list(zip(s1, s2))
print dict(zip(s1,s2))

print [x + y for x in [1 ,2 , 3] for y in [5, 6 ,7]]
print {x:y for x in [1,2,3] for y in [5,6,7]}




