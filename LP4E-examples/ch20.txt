>>> ord('s')
115


>>> res = []
>>> for x in 'spam':
...     res.append(ord(x))
...
>>> res
[115, 112, 97, 109]


>>> res = list(map(ord, 'spam'))          # Apply function to sequence
>>> res
[115, 112, 97, 109]


>>> res = [ord(x) for x in 'spam']        # Apply expression to sequence
>>> res
[115, 112, 97, 109]




>>> [x ** 2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


>>> list(map((lambda x: x ** 2), range(10)))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



>>> [x for x in range(5) if x % 2 == 0]
[0, 2, 4]

>>> list(filter((lambda x: x % 2 == 0), range(5)))
[0, 2, 4]

>>> res = []
>>> for x in range(5):
...     if x % 2 == 0:
...         res.append(x)
...
>>> res
[0, 2, 4]



>>> [x ** 2 for x in range(10) if x % 2 == 0]
[0, 4, 16, 36, 64]


>>> list( map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10))) )
[0, 4, 16, 36, 64]



>>> res = [x + y for x in [0, 1, 2] for y in [100, 200, 300]]
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302]


>>> res = []
>>> for x in [0, 1, 2]:
...     for y in [100, 200, 300]:
...         res.append(x + y)
...
>>> res
[100, 200, 300, 101, 201, 301, 102, 202, 302]



>>> [x + y for x in 'spam' for y in 'SPAM']
['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM',
'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM']



>>> [(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1]
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]



>>> res = []
>>> for x in range(5):
...     if x % 2 == 0:
...         for y in range(5):
...             if y % 2 == 1:
...                 res.append((x, y))
...
>>> res
[(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]



>>> M = [[1, 2, 3],
...      [4, 5, 6],
...      [7, 8, 9]]

>>> N = [[2, 2, 2],
...      [3, 3, 3],
...      [4, 4, 4]]


>>> M[1] 
[4, 5, 6]

>>> M[1][2]
6


>>> [row[1] for row in M]
[2, 5, 8]

>>> [M[row][1] for row in (0, 1, 2)]
[2, 5, 8]


>>> [M[i][i] for i in range(len(M))]
[1, 5, 9]


>>> [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[2, 4, 6, 12, 15, 18, 28, 32, 36]

>>> [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]



>>> res = []
>>> for row in range(3):
...     tmp = []
...     for col in range(3):
...         tmp.append(M[row][col] * N[row][col])
...     res.append(tmp)
...
>>> res
[[2, 4, 6], [12, 15, 18], [28, 32, 36]]



>>> open('myfile').readlines()
['aaa\n', 'bbb\n', 'ccc\n']

>>> [line.rstrip() for line in open('myfile').readlines()]
['aaa', 'bbb', 'ccc']

>>> [line.rstrip() for line in open('myfile')]
['aaa', 'bbb', 'ccc']

>>> list(map((lambda line: line.rstrip()), open('myfile')))
['aaa', 'bbb', 'ccc']

>>> listoftuple = [('bob', 35, 'mgr'), ('mel', 40, 'dev')]

>>> [age for (name, age, job) in listoftuple]
[35, 40]

>>> list(map((lambda row: row[1]), listoftuple))
[35, 40]

# 2.6 only
>>> list(map((lambda (name, age, job): age), listoftuple))  
[35, 40]



>>> def gensquares(N):
...     for i in range(N):
...         yield i ** 2        # Resume here later
...



>>> for i in gensquares(5):     # Resume the function
...     print(i, end=' : ')     # Print last yielded value
...
0 : 1 : 4 : 9 : 16 :
>>>



>>> x = gensquares(4)
>>> x
<generator object at 0x0086C378>



>>> next(x)                     # Same as x.__next__() in 3.0
0
>>> next(x)                     # Use x.next() or next() in 2.6
1
>>> next(x)
4
>>> next(x)
9
>>> next(x)

Traceback (most recent call last):
...more text omitted...
StopIteration



>>> def buildsquares(n):
...     res = []
...     for i in range(n): res.append(i ** 2)
...     return res
...
>>> for x in buildsquares(5): print(x, end=' : ')
...
0 : 1 : 4 : 9 : 16 :



>>> for x in [n ** 2 for n in range(5)]:
...     print(x, end=' : ')
...
0 : 1 : 4 : 9 : 16 :

>>> for x in map((lambda n: n ** 2), range(5)):
...     print(x, end=' : ')
...
0 : 1 : 4 : 9 : 16 :



>>> def gen():
...    for i in range(10):
...        X = yield i
...        print(X)
...
>>> G = gen()
>>> next(G)              # Must call next() first, to start generator
0
>>> G.send(77)           # Advance, and send value to yield expression
77
1
>>> G.send(88)
88
2
>>> next(G)              # next() and X.__next__() send None 
None
3



>>> [x ** 2 for x in range(4)]          # List comprehension: build a list
[0, 1, 4, 9]

>>> (x ** 2 for x in range(4))          # Generator expression: make an iterable
<generator object at 0x011DC648>



>>> list(x ** 2 for x in range(4))      # List comprehension equivalence
[0, 1, 4, 9]



>>> G = (x ** 2 for x in range(4))
>>> next(G)
0
>>> next(G)
1
>>> next(G)
4
>>> next(G)
9
>>> next(G)

Traceback (most recent call last):
...more text omitted...
StopIteration



>>> for num in (x ** 2 for x in range(4)):
...     print('%s, %s' % (num, num / 2.0))
...
0, 0.0
1, 0.5
4, 2.0
9, 4.5



>>> sum(x ** 2 for x in range(4))
14

>>> sorted(x ** 2 for x in range(4))
[0, 1, 4, 9]

>>> sorted((x ** 2 for x in range(4)), reverse=True)
[9, 4, 1, 0]

>>> import math
>>> list( map(math.sqrt, (x ** 2 for x in range(4))) )
[0.0, 1.0, 2.0, 3.0]



>>> G = (c * 4 for c in 'SPAM')           # Generator expression
>>> list(G)                               # Force generator to produce all results
['SSSS', 'PPPP', 'AAAA', 'MMMM']



>>> def timesfour(S):                     # Generator function
...     for c in S:
...         yield c * 4
...
>>> G = timesfour('spam')
>>> list(G)                               # Iterate automatically
['ssss', 'pppp', 'aaaa', 'mmmm']



>>> G = (c * 4 for c in 'SPAM')   
>>> I = iter(G)                           # Iterate manually
>>> next(I)
'SSSS'
>>> next(I)
'PPPP'

>>> G = timesfour('spam')
>>> I = iter(G)
>>> next(I)
'ssss'
>>> next(I)
'pppp'



>>> G = (c * 4 for c in 'SPAM')
>>> iter(G) is G                          # My iterator is myself: G has __next__
True



>>> G = (c * 4 for c in 'SPAM')           # Make a new generator
>>> I1 = iter(G)                          # Iterate manually
>>> next(I1)
'SSSS'
>>> next(I1)
'PPPP'
>>> I2 = iter(G)                          # Second iterator at same position!
>>> next(I2)
'AAAA'



>>> list(I1)                              # Collect the rest of I1's items
['MMMM']
>>> next(I2)                              # Other iterators exhausted too
StopIteration

>>> I3 = iter(G)                          # Ditto for new iterators
>>> next(I3)
StopIteration

>>> I3 = iter(c * 4 for c in 'SPAM')      # New generator to start over
>>> next(I3)
'SSSS'



>>> def timesfour(S):
...     for c in S:
...         yield c * 4
...
>>> G = timesfour('spam')                 # Generator functions work the same way
>>> iter(G) is G
True
>>> I1, I2 = iter(G), iter(G)
>>> next(I1)
'ssss'
>>> next(I1)
'pppp'
>>> next(I2)                              # I2 at same position as I1
'aaaa'



>>> L = [1, 2, 3, 4]
>>> I1, I2 = iter(L), iter(L)
>>> next(I1)
1
>>> next(I1)
2
>>> next(I2)                              # Lists support multiple iterators
1
>>> del L[2:]                             # Changes reflected in iterators
>>> next(I1)
StopIteration



>>> S1 = 'abc'
>>> S2 = 'xyz123'
>>> list(zip(S1, S2))                     # zip pairs items from iterables
[('a', 'x'), ('b', 'y'), ('c', 'z')]           

# zip pairs items, truncates at shortest

>>> list(zip([-2, -1, 0, 1, 2]))               # Single sequence: 1-ary tuples
[(-2,), (-1,), (0,), (1,), (2,)]

>>> list(zip([1, 2, 3], [2, 3, 4, 5]))         # N sequences: N-ary tuples
[(1, 2), (2, 3), (3, 4)]

# map passes paired itenms to a function, truncates

>>> list(map(abs, [-2, -1, 0, 1, 2]))          # Single sequence: 1-ary function
[2, 1, 0, 1, 2]

>>> list(map(pow, [1, 2, 3], [2, 3, 4, 5]))    # N sequences: N-ary function
[1, 8, 81]



# map(func, seqs...) workalike with zip

def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))



# Using a list comprehension

def mymap(func, *seqs):
    return [func(*args) for args in zip(*seqs)]

print(mymap(abs, [-2, -1, 0, 1, 2]))
print(mymap(pow, [1, 2, 3], [2, 3, 4, 5]))



# Using generators: yield and (...)

def mymap(func, *seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)

def mymap(func, *seqs):
    return (func(*args) for args in zip(*seqs))



print(list(mymap(abs, [-2, -1, 0, 1, 2])))
print(list(mymap(pow, [1, 2, 3], [2, 3, 4, 5])))



C:\misc> c:\python26\python
>>> map(None, [1, 2, 3], [2, 3, 4, 5])
[(1, 2), (2, 3), (3, 4), (None, 5)]
>>> map(None, 'abc', 'xyz123')
[('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]



# zip(seqs...) and 2.6 map(None, seqs...) workalikes

def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res  = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs, pad=None):	
    seqs = [list(S) for S in seqs]
    res  = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res

S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))



# Using generators: yield

def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    while all(seqs):
        yield tuple(S.pop(0) for S in seqs)
        
def mymapPad(*seqs, pad=None):
    seqs = [list(S) for S in seqs]
    while any(seqs):
        yield tuple((S.pop(0) if S else pad) for S in seqs)

S1, S2 = 'abc', 'xyz123'
print(list(myzip(S1, S2)))
print(list(mymapPad(S1, S2)))
print(list(mymapPad(S1, S2, pad=99)))



# Alternate implementation with lengths

def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return [tuple(S[i] for S in seqs) for i in range(minlen)]

def mymapPad(*seqs, pad=None):
    maxlen = max(len(S) for S in seqs)
    index  = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]

S1, S2 = 'abc', 'xyz123'
print(myzip(S1, S2))
print(mymapPad(S1, S2))
print(mymapPad(S1, S2, pad=99))



# Using generators: (...)

def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

print(list(myzip(S1, S2)))



def myzip(*args):
    iters = map(iter, args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


>>> list(myzip('abc', 'lmnop'))
[('a', 'l'), ('b', 'm'), ('c', 'n')]


def myzip(*args):
    iters = list(map(iter, args))
    …rest as is…



>>> D = {'a':1, 'b':2, 'c':3}
>>> x = iter(D)
>>> next(x)
'a'
>>> next(x)
'c'



>>> for key in D:
...     print(key, D[key])
...
a 1
c 3
b 2



>>> for line in open('temp.txt'):
...     print(line, end='')
...
Tis but
a flesh wound.



>>> [x * x for x in range(10)]            # List comprehension: builds list
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]      # like list(generator expr)

>>> (x * x for x in range(10))            # Generator expression: produces items
<generator object at 0x009E7328>          # Parens are often optional

>>> {x * x for x in range(10)}            # Set comprehension, new in 3.0 
{0, 1, 4, 81, 64, 9, 16, 49, 25, 36}      # {x, y} is a set in 3.0 too

>>> {x: x * x for x in range(10)}         # Dictionary comprehension, new in 3.0
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81} 



>>> {x * x for x in range(10)}                # Comprehension
{0, 1, 4, 81, 64, 9, 16, 49, 25, 36}
>>> set(x * x for x in range(10))             # Generator and type name
{0, 1, 4, 81, 64, 9, 16, 49, 25, 36}

>>> {x: x * x for x in range(10)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
>>> dict((x, x * x) for x in range(10))
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



>>> res = set()
>>> for x in range(10):                        # Set comprehension equivalent
...     res.add(x * x)
...
>>> res
{0, 1, 4, 81, 64, 9, 16, 49, 25, 36}

>>> res = {}
>>> for x in range(10):                        # Dict comprehension equivalent
...     res[x] = x * x
...
>>> res
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}



>>> G = ((x, x * x) for x in range(10))
>>> next(G)
(0, 0)
>>> next(G)
(1, 1)



>>> [x * x for x in range(10) if x % 2 == 0]           # Lists are ordered
[0, 4, 16, 36, 64]
>>> {x * x for x in range(10) if x % 2 == 0}           # But sets are not
{0, 16, 4, 64, 36}
>>> {x: x * x for x in range(10) if x % 2 == 0}        # Neither are dict keys
{0: 0, 8: 64, 2: 4, 4: 16, 6: 36}



>>> [x + y for x in [1, 2, 3] for y in [4, 5, 6]]      # Lists keep duplicates
[5, 6, 7, 6, 7, 8, 7, 8, 9]
>>> {x + y for x in [1, 2, 3] for y in [4, 5, 6]}      # But sets do not
{8, 9, 5, 6, 7}
>>> {x: y for x in [1, 2, 3] for y in [4, 5, 6]}       # Neither do dict keys
{1: 6, 2: 6, 3: 6}



>>> {x + y for x in 'ab' for y in 'cd'}
{'bd', 'ac', 'ad', 'bc'}

>>> {x + y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'}
{'bd': (98, 100), 'ac': (97, 99), 'ad': (97, 100), 'bc': (98, 99)}

>>> {k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
{'sausagesausage', 'spamspam'}

>>> {k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'}
{'SAUSAGE': 'sausagesausage', 'SPAM': 'spamspam'}



### File: mytimer.py

import time
reps = 1000
repslist = range(reps)
 
def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)



### File: timeseqs.py

import sys, mytimer                              # Import timer function
reps = 10000
repslist = range(reps)                           # Hoist range out in 2.6

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist))              # Use list() in 3.0 only

def genExpr():
    return list(abs(x) for x in repslist)        # list() forces results

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = mytimer.timer(test)
    print ('-' * 33)
    print ('%-9s: %.5f => [%s...%s]' %
           (test.__name__, elapsed, result[0], result[-1]))



C:\misc> c:\python30\python timeseqs.py



### File: timeseqs.py (modification)
...
...
def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res

def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 10), repslist))          # list() in 3.0 only

def genExpr():
    return list(x + 10 for x in repslist)                   # list() in 2.6 + 3.0

def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())
...
...



C:\misc> c:\python30\python timeseqs.py



### File: mytimer.py (2.6 and 3.0) (modified)

"""
timer(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3) 
_reps times, and returns total time for all runs, with final result; 

best(spam, 1, 2, a=3, b=4, _reps=50) runs best-of-N timer to filter out 
any system load variation, and returns best time among _reps tests
"""

import time, sys
if sys.platform[:3] == 'win':
    timefunc = time.clock               # Use time.clock on Windows
else:
    timefunc = time.time                # Better resolution on some Unix platforms

def trace(*args): pass                  # Or: print args

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)    # Passed-in or default reps
    trace(func, pargs, kargs, _reps)
    repslist = range(_reps)             # Hoist range out for 2.6 lists
    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)                       

def best(func, *pargs, **kargs):                
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
    return (best, ret)



# File timeseqs.py (modifications)

import sys, mytimer
reps = 10000
repslist = range(reps)                           

def forLoop(): ...

def listComp(): ...

def mapCall(): ...
 
def genExpr(): ...
        
def genFunc(): ...

print(sys.version)
for tester in (mytimer.timer, mytimer.best):
    print('<%s>' % tester.__name__)
    for test in (forLoop, listComp, mapCall, genExpr, genFunc):
        elapsed, result = tester(test)
        print ('-' * 35)
        print ('%-9s: %.5f => [%s...%s]' %
               (test.__name__, elapsed, result[0], result[-1]))



C:\misc> c:\python30\python timeseqs.py



### File: mytimer.py (3.X only) (modified again)

"""
Use 3.0 keyword-only default arguments, instead of ** and dict pops.
No need to hoist range() out of test in 3.0: a generator, not a list
"""

import time, sys
trace = lambda *args: None  # or print
timefunc = time.clock if sys.platform == 'win32' else time.time
  
def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    start = timefunc()
    for i in range(_reps):
        ret = func(*pargs, **kargs) 
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func, *pargs, _reps=50, **kargs):
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
    return (best, ret)



C:\misc> c:\python30\python timeseqs.py



C:\misc> c:\python30\python
>>> from mytimer import timer, best
>>>
>>> def power(X, Y): return X ** Y            # Test function
...
>>> timer(power, 2, 32)                       # Total time, last result
(0.002625403507987747, 4294967296)
>>> timer(power, 2, 32, _reps=1000000)        # Override defult reps
(1.1822605247314932, 4294967296)
>>> timer(power, 2, 100000)[0]                # 2 ** 100,000 tot time @1,000 reps
2.2496919999608878

>>> best(power, 2, 32)                        # Best time, last result
(5.58730229727189e-06, 4294967296)
>>> best(power, 2, 100000)[0]                 # 2 ** 100,000 best time
0.0019937589833460834
>>> best(power, 2, 100000, _reps=500)[0]      # Override default reps
0.0019845399345541637



>>> timer(power, 2, 1000000, _reps=1)[0]      # 2 ** 1,000,000: total time
0.088112804839710179
>>> timer(power, 2, 1000000, _reps=10)[0]
0.40922470593329763

>>> best(power, 2, 1000000, _reps=1)[0]       # 2 ** 1,000,000: best time
0.086550036387279761
>>> best(power, 2, 1000000, _reps=10)[0]      # 10 is sometimes as good as 50
0.029616752967200455
>>> best(power, 2, 1000000, _reps=50)[0]      # Best resolution
0.029486918030102061



# NOTE: the indentation of the 2nd line was shifted in production

    print('<%s>' % tester.__name__)            # From expression

    print('<{0}>'.format(tester.__name__))     # To method call

        print ('%-9s: %.5f => [%s...%s]' %
               (test.__name__, elapsed, result[0], result[-1]))

        print('{0:<9}: {1:.5f} => [{2}...{3}]'.format(
                test.__name__, elapsed, result[0], result[-1]))



>>> X = 99
>>> def selector():       # X used but not assigned
...     print(X)          # X found in global scope
...
>>> selector()
99



>>> def selector():
...     print(X)          # Does not yet exist!
...     X = 88            # X classified as a local name (everywhere)
...                       # Can also happen for "import X", "def X"...
>>> selector()
...error text omitted...
UnboundLocalError: local variable 'X' referenced before assignment



>>> def selector():
...     global X           # Force X to be global (everywhere)
...     print(X)
...     X = 88
...
>>> selector()
99



>>> X = 99
>>> def selector():
...     import __main__         # Import enclosing module
...     print(__main__.X)       # Qualify to get to global version of name
...     X = 88                  # Unqualified X classified as local
...     print(X)                # Prints local version of name
...
>>> selector()
99
88



>>> def saver(x=[]):               # Saves away a list object
...     x.append(1)                # Changes same object each time!
...     print(x)
...
>>> saver([2])                     # Default not used
[2, 1]
>>> saver()                        # Default used
[1]
>>> saver()                        # Grows on each call!
[1, 1]
>>> saver()
[1, 1, 1]



>>> def saver(x=None):
...     if x is None:             # No argument passed?
...         x = []                # Run code to make a new list
...     x.append(1)               # Changes new list object
...     print(x)
...
>>> saver([2])
[2, 1]
>>> saver()                       # Doesn't grow here
[1]
>>> saver()
[1]



>>> def saver():
...     saver.x.append(1)
...     print(saver.x)
...
>>> saver.x = []
>>> saver()
[1]
>>> saver()
[1, 1]
>>> saver()
[1, 1, 1]



>>> def proc(x):
...     print(x)                 # No return is a None return
...
>>> x = proc('testing 123...')
testing 123...
>>> print(x)
None



>>> list = [1, 2, 3]
>>> list = list.append(4)        # append is a "procedure"
>>> print(list)                  # append changes list in-place
None



#### lab code



def f1(a, b): print(a, b)            # Normal args
def f2(a, *b): print(a, b)           # Positional varargs

def f3(a, **b): print(a, b)          # Keyword varargs

def f4(a, *b, **c): print(a, b, c)   # Mixed modes

def f5(a, b=2, c=3): print(a, b, c)  # Defaults

def f6(a, b=2, *c): print(a, b, c)   # Defaults and positional varargs



>>> f1(1, 2)
>>> f1(b=2, a=1)

>>> f2(1, 2, 3)
>>> f3(1, x=2, y=3)
>>> f4(1, 2, 3, x=2, y=3)

>>> f5(1)
>>> f5(1, 4)

>>> f6(1)
>>> f6(1, 3, 4)



x = y // 2                           # For some y > 1
while x > 1:
    if y % x == 0:                   # Remainder
        print(y, 'has factor', x)
        break                        # Skip else
    x -= 1
else:                                # Normal exit
    print(y, 'is prime')

