__author__ = 'admin'
for x in [1, 2, 3, 4]:print(x ** 2,)
for x in (1, 2, 3, 4):print(x ** 3,)
for x in 'spam':print(x*2,)
f = open('cluo')
print f.readline()
print f.readline()
print f.readline()
print f.readline()


print f.readlines()

L = [1,2 ,3]
I = iter(L)
print I.next()
print I.next()
print I.next()

f = open('cluo')
print iter(f) is f
print f.next()
print f.next()
print f.next()
print f.next()

L = ["a", 'b', 'c']
I = iter(L)
while True:
	try:
		x = next(I)
	except StopIteration:
		break
	print(x * 2)

D = {'a':1 ,'b':2, 'c':3}
for key in D.keys():
	print(key ,D[key])

R = range(5)
print R

I =iter(R)
print I.next()

E = enumerate(R)
I = iter(E)
print I.next()
print I.next()

E = enumerate('spam')
I = iter(E)
print I.next()
print I.next()

r = []
L = [1, 2, 3, 4]
for x in L:
	r.append(x + 10)
print r

L = [x + 10 for x in L]
print L

lines = [line.rstrip() for line in open('cluo')]
print lines

lines = [line.replace('', '!') for line in open('cluo')]
print lines
lines = [('sys' in line,line[0]) for line in open('cluo')]
print lines
print [x + y for x in 'abc' for y in 'lmn']

print sum([1,2,3,4,5])
print max([1,2,3,4,5])
print min([1,2,3,4,5])
print any(['spam','','ni'])
print all(['spam','','ni'])



print [x + y for x in 'abc' if x=='b'  for y in 'lmn' if y=='m']
L = ['bb', 'cc', 'dd', 'ee']
print '&&'.join(L)

f = open('cluo')
print f.readlines()
#a,b,c = open('cluo')
#print a,b,c
a,b,c,d,e,f = open('cluo')
print a,b,c,d,e,f

print {x:line.rstrip() for (x,line) in enumerate(open('cluo'))}
Z = zip((1,2,3), (10,20,30))
print Z


D = dict(a=1,b=2,c=3)
print D
k = D.keys()
print k
