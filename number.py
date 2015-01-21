print 4.0e+2
print 021
print 0x1f
print abs(-77)
print pow(3,2)
print hex(13)
print oct(13)
print bin(13)

if 2 != 3:
    print 'not'
if 2 in (2, 3, 4, 6):
    print 'yes'
if 2 not in (2, 3, 4, 6):
    print 'no'
bCluo = bin(1010)
print bCluo
#print bCluo
#cluocluo = ~bCluo
#print cluocluo
print 3 ** 2
he = [1, 2, 3, 4, 5]
print he[1:3]
print int(3.14)
print float(3)
num = 1/0.333
print num
print '%e' % num

print '%4.2f' % num
print '{0:4.2f}'.format(num)


#floor div

print 10/4.0
print 10//4.0
import math
print math.floor(2.5)
print math.floor(-2.5)

print math.trunc(2.5)
print math.trunc(-2.5)


#int
print 012
print 0x11
print 0b0101
print int('0x40',16)
print int ('0b1101',2);
print int('0x2f',16)
print int ('032',8)

#format
print '{0:o},{1:x},{2:b}'.format(64,64,64)
print '%o, %x, %X' %(64, 255, 255)

#oct 00
print 0012


x=1
print x << 2
print x | 2
print x & 1

print bin(x << 2)
print bin(x | 0b010)

x = ~0xff
print x
print bin(110 ^ 001)
print hex(85)

abs(-42)
print min(3 ,1 ,2 ,4)
print max(3, 3)
import math
print math.pi
print math.e

print math.floor(2.67)
print math.floor(-2.567)
print math.trunc(2.567)
print math.trunc(-2.567)

print int(2.67)
print int(-2.67)

print round(2,6)
print '%.1f' % 2.567 ,'{0:.2f}'.format(2.56)
print 1/3
print round(1/3,2)
print '%.2f' % (1/3)

print 144 ** .5
import math
print pow(144,.5)
print math.sqrt(144)

import random
print random.random();
list = ['cluo', 'chunling', 'luosheng', 'shaoling']
print random.choice(list)

from decimal import Decimal
total = Decimal('0.1') + Decimal('0.11') + Decimal('0.12')
print total

#decimal.getcontext().prec = 4
import decimal
decimal.getcontext().prec = 4
print decimal.Decimal(1) / decimal.Decimal(7)
print Decimal('0.14')

from fractions import Fraction
x = Fraction(1 ,3)
print x
y = Fraction(1 ,5)
print x + y

ret = Fraction('.25') + Fraction('1.25')
print ret

ret = decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
print ret

x = set('abcde')
y = set('bdxyz')
print x,y

print 'e' in x;

print x - y #diff
print x | y #union
print x & y #inntersection
print x ^ y
z = x.intersection(y)
z.add('SPAM')
print z
z.update(set(['X','Y']))
print z
z.remove('b')
print z
for item in set('abc'): print(item * 3) #set
print z | set([3, 4])
ret =  z.union([5,6])
print ret
ret = ret.intersection([1,3,5]);
print ret
S =  {1,2,3,4}
S.add('alot')
S.update(['a','l','o','t'])
print S

#empty set
z = set([])
print z
print type({})


print {1 ,2 ,3} | {3, 4}
print {1, 2, 3}.union([3, 4])
print {1, 2, 3}.union(set([3, 4]))
print {1, 2, 3}.intersection([1, 3, 5])
print {1, 2, 3}.issubset(range(-5,5))

#set only could put in fixed type data  eg:tuple number str
z.add((1 ,2 ,3))
print z
print (1 ,2 ,3) in z
print (1 ,4 ,4) in z
#set set([]) or {}
ret = {x ** 2 for x in [1, 2, 3, 4]}
print ret

ret = {x * 2 for x in 'spam'}
print ret
L = [1, 1, 2, 2, 3, 4, 5]
print set(L)
#L = list(set(L))
#print L

engineers = {'bob', 'sue', 'ann', 'vic'}
managers = {'tom', 'sue'}
print 'bob' in engineers
print engineers & managers
print engineers | managers
print engineers - managers
print engineers > managers  #issupper
print {'sue','ann'} < engineers
print engineers ^ managers
print (managers | engineers) >engineers

#bool
print type(True)
print isinstance(True,int)
print True == 1
print True is 1
print True + 4
print True or False

#NumPy

#REF and copy

L1 = [2 , 3, 4]
L2 = L1 #ref
L1[0] = 24
print L2,L1 #[24, 3, 4] [24, 3, 4]

L1 = [2, 3, 4]
L2 = L1[:] #copy
L1[0] = 24
print L1,L2 #[24, 3, 4] [2, 3, 4]

#copy anything anytype
import copy
Y = [2 ,3,[3,4,5]]
X = copy.copy(Y)
print X
X = copy.deepcopy(Y)
print X

L = [1, 2, 3]
M = L
print M == L #true
print M is L #true   same obj

L = [1, 2, 3]
M = [1 ,2, 3]
print L == M #true
print L is M #false

x = 42
y = 42
x == y  #true
x is y  #true not same object but cache
# #str and small number can be cache

import sys
print sys.getrefcount(1)

#number str tugle can not be change



#string type list could not change  strlist
S = ''
print S
S = "SPAM's"
print S
S = """..."""
print S

S = 'S\np\ta\x00m'
print S

s1 = 'aacccdddd '
s2 = 'bb'
print  s1 + s2
print s1*2 + s2*2
print s1[:]
print s1[0:1]
print len(s1)

print "a %s parrot" % ('kind')
print "a {0} parrot".format('kind')
print s1.find('cd') #return index 4
s1.rstrip()
print s1
s1.replace('xx', 'cd')
print s1
s1 = 'a,b,c,d,e,f'
list = s1.split(',')
print list
print s1.isdigit()
print '123'.isdigit()
print s1.lower()
print s1.upper()
print s1.endswith('d') #return false end test
print s1.endswith('d ')#return true
print 'spam'.join('aa') #aspama  seperator single char
print s1.encode('UTF-8')
for x in S:
    print (x)
ret = [c * 2 for c in s1]
print ret

print 'spa"m'
print "spa'm"
print '''....spam...'''
title  = "Meaning" + ' of' + " Life"
print title

t = 'knight\'s'+" knight\"s"
print len(t)
str = "string" \
      "sdfsfsf"
print str
print "\\ \' \" \n \t \v \x2f \012"

s = '\001\002\x03'
print len(s)
x = "C:\\py\\code"
print x
print len(x)

#raw   can not be odd \ end
print r'c:\new\text.dat'
#
print """\\
dfsdf
sdfsf
sfs
sfsfs
"""

print len('abasdfs');
print 'abc' + 'def'
print 'Ni' * 4

mjob = 'hacker'
for c in mjob: print(c)

print "k" in mjob

S = 'spamspamspam0'
print S[0],S[3],S[:],S[:-1],S[1:]

#stride
print S[0:-1:2]
#- reverse
S ='abcdefg'
print S[::-1]
print S[5:1:-1]
print 'spam'[slice(1,3)]
print 'spam'[1:3]
print 'spam'[slice(None,None,-1)]
print 'spam'[::-1]
tim = "sfsf "
print len(tim)
print tim.rstrip();
print len(tim)

S = 'spamSPAM'
S = S[:4] + 'Burger' + S[-1]
print S

S = S.replace('spam','CCTV')
print S

S = 'That is %d %s bird!' %(1, 'dead')
print S
S = 'That is {0} {1} bird!'.format(1,'dead')
print S

where = S.find('is')
print where

S = 'spammy'
L = ['s', 'p' , 'a']
S = '<>'.join(L)
print S
S = ''.join(L)
print S
line = 'aaa bbb ccc'
print line[0:3]
print line[8:]
line = "i'mSpamssssSpamssssss"
List = line.split('Spam')
print List
line = line +'\n'
print line
print line.rstrip()
print line.upper()
print line.endswith('Ni\n')
print line.startswith('cluo')

print line.find('Ni') != -1
print "%d %s %d" %(1, 'cluo', 2)

print '%f, %.2f'  % (1/3.0, 1/3.0)

print "%(n)d %(x)s" % {"n":1, "x":'spam'}
template = '{0},{1} and {2}'
print template.format('spam', 'ham', 'egg')

#list
L = []
L = [0, 1, 2, 3, 4]
print L
L = range(-4,4)
print L

L1 = [0, 1, 2]
L2 = [3, 4, 5]
L = L1 + L2
print L
print  L * 3
for x in L:
    print(x)
L.append(4)
print L
L.extend([5, 6, 7])
print L
print L.index(5)
L.sort()
print L
L.reverse()
print L
del L[0]
print L
del L[0:2] #by index
print L
L.pop()
print L
L.remove(4) #by value
print L
L[2] = 1
L[3:5]=[3,4]
print L
L = [x**2 for x in range(5)]
res = [c*4 for c in 'SPAM']
print res
res = []
for c in 'spam':
    res.append(c * 4)
print res
L = ['spam', 'Spam','SPAM']
print L[1:]
print L[2]
print L[-2]
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print matrix[1][1]

L.append('please')
print L
L.sort()
print L
L[len(L):]=['xxx']
print L
L[:0]=['BBB']
print L


#print sorted([x.lower() for x in L],reversed=True)
print L.index('SPAM')
L.remove('please')
print L
del L[0]
print L
del L[1:2]
print L
L[1:]=[]
print L

D = { }
D = {'spam':2, 'egg': 3}
print D
D = dict(name='Bob',age=42)
print D
print D.keys()
print D.values()
print D.items()
Y = D.copy()
print Y
D = {'spam':2 , 'ham':1 ,'eggs':3}
print D['spam']

print 'ham' in D
D['ham'] = ['grill', 'bake', 'fry']
print D
del D['eggs']
print D

print D.get('sdfsf')
print D.get('sdsf',88)
D.pop('spam')
print D
D2 ={'ham':'cccc','cluo':'shuai'}
D.update(D2)
print D
for key in D:
    print key,D[key]

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix [(5, 5 ,7)] = 99
X=2; Y=3; Z=4;
print Matrix[(X, Y, Z)]
if (2,3,4) in Matrix:
    print Matrix[(2,3,4)]
else:
    print 0
try:
    print(Matrix[(2,3,5)])
except KeyError:
    print(0)
print Matrix.get((2,3,6),0)
print dict.fromkeys(['a','b'],0)
D ={'a':1, 'b':2, 'c':3}
print D.keys()

ret =  (2,3,4,5) + (6,7,8)
print [ret]
for line in open('cluo'):
    print line
F = open('cluo')
line = F.readline()
line = line.rstrip();
parts = line.split(',')
print parts



D ={'a':1,'b':2}
F = open('cluo', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('cluo','rb')
E = pickle.load(F)
print E

F = open('cluo.bin','wb')
import struct
#data = struct.pack('>i4sh','cluo','4','5')
#F.write(data)
F.close()
#F.open('cluo.bin','rb')
#data = F.read()
#values = struct.unpack('i4sh',data)
#print values

spam,ham ='cluo','cluo1'
print spam
print ham
[spam,ham]= ['cluo','cluo1']
print spam
print ham
[a,b,c,d] = ['1','2','3','4']
print a,b,c,d
(a,b,c)="ABC"
print a,b,c
x='SPAM'
if 'rubby' in 'shrubby':
    print(x * 8)
    x+='NI'
    if x.endswith('NI'):
        x *= 2
        print(x)
if('a' == 'b' and 'c'=='d' and
    'd'=='e' and 'e' == 'f'):
    print('nex')
x = 'SPAM'
while x:
    print(x)
    x = x[1:]
a=0;b=10;
while a <b:
    print(a)
    a+=1

x = 10
# while x:
#     x = x-1
#     if x % 2 != 0:continue
#     print x
# while True:
#     name = input('Enter name:')
#     if name == 'stop': break
#     age = input('Enter age')
#     print 'Hello %s=>%d' %(name,int(age)**2)
sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x
print sum
S = 'lumberjack'
for x in S: print x
T = ('cluo','cluo1','cluo2')
for x in T:print x

file = open('cluo','r')
print file.read()
file = open('cluo','r')
while True:
    char = file.read(1)
    if not char: break
    print char
for char in open('cluo').read():
    print char
for line in open('cluo'):
    print(line)
file = open('cluo')
while True:
    line = file.readline()
    if not line:break
    print(line)
while True:
    chunk = file.read(10)
    if not chunk:break
    print(chunk)
for i in range(3):
    print i
for i in range(0,10,2):
    print i
S = 'abcdefghijk'
for i in range(0,len(S),2):print S[i]
ret = [i+1 for i in range(0,len(S)) if i ==2]
print ret

for (x, y) in zip(L1, L2):
    print(x,y,'--',x+y)
S1 = 'abc'
S2 = 'xyz123'
print zip(S1, S2)

print map(None,S1,S2)
print map(ord,'spam')
res = []
for c in 'spam': res.append(ord(c))
print res
D2 = {}
keys = [1, 2, 3]
vals = ['cluo',' cluo1', 'cluo2']
for (k, v) in zip(keys,vals):D2[k] =v
print D2
ret =  zip(keys, vals)
print ret
print dict(ret)

S = 'spam'
offset = 0
for item in S:
    print(item, 'appears', offset)
    offset+=1
S = 'spam'
for (offset,item) in enumerate(S):
    print(item,'appears as offset',offset)
ret = [c * i for(i, c) in enumerate(S)]
print ret
F = open('cluo')
print F.readline();
print F.readline();

for line in open('cluo'):
    print line.upper()
F.close()
F = open('cluo')
while True:
    line = F.readline()
    if not line:break
    print line.upper()
L = [1, 2 ,3]
I = iter(L)
print I.next()
for X in L:
    print X ** 2
L = [1, 2 ,3]
print L
I = iter(L)
print I
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print X ** 2
D ={'a':1 ,'b':2 ,'c':3}
for key in D.keys():
    print(key,D[key])
E = enumerate('spam')
I = iter(E)
print I.next();
L = [1, 2, 3, 3, 4]
for i in range(len(L)):
    print L[i]
print [x+10 for x in L]
lines = [line.rstrip() for line in open('cluo')]
print lines
print [line.rstrip().upper() for line in open('cluo')]
print [line.split() for line in open('cluo')]
print [line.replace(' ','|') for line in open('cluo')]
print [('sys' in line,line[0]) for line in open('cluo')]
print [x + y for x in 'abc' for y in 'lmn']
print sorted(open('cluo'))
print zip(open('cluo'),open('cluo'))
print enumerate(open('cluo'))
print filter(bool,open('cluo'))
print any([0,'1',2])
print all([0,1,2])

d = {'a':1 , 'b':2 ,'c':3}
for k in sorted(d.keys()): print(k,D[k])

ret = dir([])
print ret
ret = dir(str)
print ret

"""
Module documentation
"""
spam = 40
def square(x):
    """
    function document
    can we have your liver then
    """
    return x ** 2
class Employee:
    "class documentation"
    pass
print(square(2))
print(square.__doc__)
print(Employee.__doc__)

import sys
help(sys.getrefcount)

def time(x,y):
    return x * y;
print time('N1',4)

def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res

seq1 = ['s','a', 'b', 'c']
seq2 = ['a','b','c']
print intersect(seq1,seq2)
print [x for x in seq1 if x in seq2]
y,z = 1, 2
def all_global():
    global x
    x = y + z

all_global();
print x
def maker(N):
    def action(X):
        return X ** N
    return action;
action = maker(2)
print action
print action(2)

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda  x,i=i:i ** x)
    return acts
acts = makeActions()
print acts[0](2)
print acts[1](2)
def multiple(x,y):
    x = 2
    y = [3,4]
    return x, y
x = 2
y = [3,4]
a,b = multiple(x,y)
print a,b
def fun(a,b,c):
    print(a,b,c)
fun(b=1,c=3,a=2)
fun(c=1,b=2,a=3)
def f(a, *pargs, **kargs):
    print(a,pargs,kargs)
f(1,2,4,x=1,y=2)
def fun(*args):
    print(args)
fun(1,2,3,4)
args = {'a':1, 'b':2, 'c':3}
args['d'] = 4
def fun(**args):
    print(args)
fun(**args)
args = (1,2)
args +=(3,4)
def fun(*arg):
    print arg
fun(*args)
def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = args
    return res
def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y
print(minmax(lessthan,4,2,3,4,5,3,4))
