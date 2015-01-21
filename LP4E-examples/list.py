__author__ = 'admin'
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2
print l3       #[1, 2, 3, 4, 5, 6]
print l3 * 3   #[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
for x in l3:
	print(x)
print (3 in l3)
l3.append(3)
print l3
l3.extend([5,6,7,8])
print l3
l3.insert(1,88)
print l3
l3.insert(0,88)
print l3
print l3.index(4)
print l3.count(3)
l3.sort()
print l3

l3.reverse()
print l3
del l3[0: 2]
print l3
print l3.pop()
l3.remove(2)
print l3
l3[0:3] =[]
print l3
l3[4] = 6
print l3

l3[1:4] = [1,2]
print l3

L = [x**2 for x in range(5)]
print L

print list(map(ord, 'spam'))

print len([1 ,2 ,3])
print [1, 2, 3] + [4, 5 ,6]
print ['Ni!'] * 4

s1 = str([1,2]) + '34'
print s1
print [1, 2] + list('34')
print 3 in [1 ,2 ,3]
print [c * 4 for c in 'SPAM']
L = ['SPAM', 'eat', 'more', 'please']
del L[0]
print L
del L[1:2]
print L