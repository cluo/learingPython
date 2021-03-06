#number

print 2 ** 100
print 1.5 * 4
print len(str(2 ** 100000))

3.1415 * 2
print (3.1415 * 2)
import math
print math.pi
print math.sqrt(4)

import random
print random.random()
print random.choice([1, 2, 3, 4])

S = 'Spam'
print len(S)
print S[0]
print S[3]
print S[-1]
print S[-2]
print S[1:3]
print S[:]
print S + 'xyz'
print S * 8

#str only support over rewrite
S = 'z' + S[1:]
print S
strList = "aaa,bbb,cccc,dd"
list = strList.split(',')
print list
print list[1:]

#str method
S = S.upper()
print S
isAl = S.isalpha()
print isAl
isDigit =  S.isdigit();
print isDigit
line = 'aaa,bbb,ccc,dd\n'
line =  line.rstrip()
print line * 2

#str format
str = '%s,eggs,and %s' %('cluo','chunling')
print str
str = '{0} eggs , and {1} chicken'.format('1','3')
print str

#check method of object
methodlist = dir(str)
print methodlist
print __name__
doc = help(str.replace)

#break line """" <pre></pre>
msg = """ cluo
cluo1
cluo2
cluo3
cluo4"""

fileObj = open('cluo','w')
fileObj.write(msg)
fileObj = open('cluo','r')
arr = []
for eachLine in fileObj:
    arr.append(eachLine)
str = 'a'.join(arr)
fileObj = open('cluo','w')
fileObj.write(str)

#regex
import re
match = re.match('Hello\s+(.*)world','Hello        python world')
inner = match.group(1);
print inner

match = re.match('/(.*)/(.*)/(.*)','/usr/home/bbq')
groups = match.groups()
print groups
print groups[0:]


#list
l = [123, 'spam', 1.23]
s = 'string'
print len(l)
print len(s)
print l[-1]
print l[0:-1]
print l + [4, 5, 6]

132

#list method
l.append('NI')
print l

l.sort();
print l
l.reverse();
print l

m = [
[1, 2, 3],
[4, 5, 6],
[7, 8 ,9]
]
print m
print m[1];
print m[1][0]

#list parse method  (pre result_function)
cols2 = [row[1] for row in m]
print cols2;

cols3 = [row[1] + 1 for row in m]
print cols3

#list parse method (add filter_function) map
cols4 = [row[1] + 1 for row in m if row[1] % 2 == 0]
print cols4

#list numpy filter
diag = [m[i][i] for i in [0, 1 ,2]]
print diag

doubles = [c * 2 for c in 'spam']
print doubles

G =  (sum(row) for row in m)
print G
print next(G)
print next(G)
print next(G)

list = [ord(x) for x in 'spaam']
print list
list = {ord(x) for x in 'spaam'}
print list
list = {x:ord(x) for x in 'spaam'}
print list

D = {'food':'spam', 'quantity':4, 'color':'pink'}
print D['food']
print D['quantity'] +1

D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print D

rec ={
    'name':{'first': 'Bob', 'last': 'Smith'},
    'job':['dev', 'mgr'],
    'age': 40.5
}

print rec['name']
print rec['name']['last']
print rec['job'][-1]
rec['job'].append('janitor')
print rec

print D.keys()
list  = D.keys()
list.sort() #return none????
print list

#auto sorted
D ={'b':2,'a':1,'c':3}
for item in D:
    print(item,'=>',D[item])
for item in sorted(D):   #sorted key
    print(item,'=>',D[item])

for c in 'spam':
    print(c.upper()),

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1
#TIME TIMEIT PROFILE
squares = []
for x in [1, 2, 3, 4, 5]:
    squares.append(x ** 2)
print squares
squares = [x ** 2 for x in [1, 2, 3, 4 ,5]]
print squares


#key test time timeit profile
if not 'f' in D:
    print('missing')
value = D.get('x', 'b')
print value
value = D['x'] if 'x' in D else 0
print value

#tuple
T = (1, 2, 3, 4)
print len(T)

T += (5, 6)
print T
#T appears once
print T.count(4)
print T.index(4)
T = ('spam', 3.0, [11, 22 ,33])
print T[1]
print T[0]
#tuple could not change
#T.append(4)
#print T

f = open('cluo_bb','w')
f.write('Hello\n')
f.write('world\n')
f.close()


f = open('cluo_bb')
content = f.read();
print content
list = content.split()
print list
#dir seek
doc = dir(f)
print doc
help(f.seek)

X = set('spam')
Y = {'h', 'a', 'm'}

print X, Y
#intersection
print X & Y
#union
print X | Y
#diff
print X - Y
list = {x ** 2 for x in [1, 2, 3, 4]}
print list

#decimal fixed precision
import decimal
d = decimal.Decimal('3.141')
print d + 1

#initrialize name obj
X = None
print(X)
L = [None] * 100
print L

print type(L)

#type
# if type(L) == type([]):
#     print('yes')
# if type(L) == list:
#     print('yes')
# if isinstance(L,list):
#     print('yes')
class Worker:
    def __int__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker('bob cluo',5000)
print bob.lastName();