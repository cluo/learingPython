>>> while True:
...    print('Type Ctrl-C to stop me!')



>>> x = 'spam'
>>> while x:                  # While x is not empty
...     print(x, end=' ')
...     x = x[1:]             # Strip first character off x
...
spam pam am m



>>> a=0; b=10
>>> while a < b:              # One way to code counter loops
...     print(a, end=' ')
...     a += 1                # Or, a = a + 1
...
0 1 2 3 4 5 6 7 8 9



while True:
    ...loop body...
    if exitTest(): break



while True: pass                     # Type Ctrl-C to stop me!


def func1():
    pass                           # Add real code here later

def func2():
    pass


def func1(): 
    ...                # Alternative to pass

def func2():
    ...

func1()                # Does nothing if called


def func1(): ...       # Works on same line too
def func2(): ...

>>> X = ...            # Alternative to None
>>> X
Ellipsis



x = 10
while x:
    x = x-1                        # Or, x -= 1
    if x % 2 != 0: continue        # Odd? -- skip print
    print(x, end=' ')



x = 10
while x:
    x = x-1
    if x % 2 == 0:                 # Even? -- print
        print(x, end=' ')



>>> while True:
...     name = input('Enter name:')
...     if name == 'stop': break
...     age  = input('Enter age: ')
...     print('Hello', name, '=>', int(age) ** 2)
...



x = y // 2                                # For some y > 1
while x > 1:
    if y % x == 0:                        # Remainder
        print(y, 'has factor', x)
        break                             # Skip else
    x -= 1
else:                                     # Normal exit
    print(y, 'is prime')



found = False
while x and not found:
    if match(x[0]):                  # Value at front?
        print('Ni')
        found = True
    else:
        x = x[1:]                    # Slice off front and repeat
if not found:
    print('not found')



while x:                             # Exit when x empty
    if match(x[0]):
        print('Ni')
        break                        # Exit, go around else
    x = x[1:]
else:
    print('Not found')               # Only here if exhausted x



while True:
    x = next()
    if not x: break
    ...process x...

x = True
while x:
    x = next()
    if x:
        ...process x...

x = next()
while x:
    ...process x...
    x = next()



>>> for x in ["spam", "eggs", "ham"]:
...     print(x, end=' ')
...
spam eggs ham



>>> sum = 0
>>> for x in [1, 2, 3, 4]:
...     sum = sum + x
...
>>> sum
10
>>> prod = 1
>>> for item in [1, 2, 3, 4]: prod *= item
...
>>> prod
24



>>> S = "lumberjack"
>>> T = ("and", "I'm", "okay")

>>> for x in S: print(x, end=' ')     # Iterate over a string
...
l u m b e r j a c k

>>> for x in T: print(x, end=' ')     # Iterate over a tuple
...
and I'm okay



>>> T = [(1, 2), (3, 4), (5, 6)]
>>> for (a, b) in T:                   # Tuple assignment at work
...     print(a, b)
...
1 2
3 4
5 6



>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> for key in D:
...    print(key, '=>', D[key])             # Use dict keys iterator and index
...
a => 1
c => 3
b => 2

>>> list(D.items())
[('a', 1), ('c', 3), ('b', 2)]

>>> for (key, value) in D.items():
...    print(key, '=>', value)              # Iterate over both keys and values
...
a => 1
c => 3
b => 2



>>> T
[(1, 2), (3, 4), (5, 6)]

>>> for both in T:
...     a, b = both                         # Manual assignment equivalent
...     print(a, b)
...
1 2
3 4
5 6



>>> ((a, b), c) = ((1, 2), 3)               # Nested sequences work too 
>>> a, b, c
(1, 2, 3)

>>> for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: print(a, b, c)
...
1 2 3
4 5 6



>>> for ((a, b), c) in [([1, 2], 3), ['XY', 6]]: print(a, b, c)
...
1 2 3
X Y 6



>>> a, b, c = (1, 2, 3)                               # Tuple assignment
>>> a, b, c
(1, 2, 3)

>>> for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:          # Used in for loop
...     print(a, b, c)
...
1 2 3
4 5 6



>>> a, *b, c = (1, 2, 3, 4)                           # Extended seq assignment
>>> a, b, c
(1, [2, 3], 4)

>>> for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
...     print(a, b, c)
...
1 [2, 3] 4
5 [6, 7] 8



>>> for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:          # Manual slicing in 2.6
...     a, b, c = all[0], all[1:3], all[3]
...     print(a, b, c)
...
1 (2, 3) 4
5 (6, 7) 8



>>> items = ["aaa", 111, (4, 5), 2.01]   # A set of objects
>>> tests = [(4, 5), 3.14]               # Keys to search for
>>>
>>> for key in tests:                    # For all keys
...     for item in items:               # For all items
...         if item == key:              # Check for match
...             print(key, "was found")
...             break
...     else:
...         print(key, "not found!")
...
(4, 5) was found
3.14 not found!



>>> for key in tests:                    # For all keys
...     if key in items:                 # Let Python check for a match
...         print(key, "was found")
...     else:
...         print(key, "not found!")
...
(4, 5) was found
3.14 not found!



>>> seq1 = "spam"
>>> seq2 = "scam"
>>>
>>> res = []                             # Start empty
>>> for x in seq1:                       # Scan first sequence
...     if x in seq2:                    # Common item?
...         res.append(x)                # Add to result end
...
>>> res
['s', 'a', 'm']



file = open('test.txt', 'r')   # Read contents into a string
print(file.read())

file = open('test.txt')
while True:
    char = file.read(1)         # Read by character
    if not char: break
    print(char)

for char in open('test.txt').read():
    print(char)

file = open('test.txt')
while True:
    line = file.readline()      # Read line by line
    if not line: break
    print(line, end='')         # Line already has a \n

file = open('test.txt', 'rb')
while True:
    chunk = file.read(10)       # Read byte chunks: up to 10 bytes
    if not chunk: break
    print(chunk)

for line in open('test.txt').readlines():
    print(line, end='')

for line in open('test.txt'):   # Use iterators: best text input mode
    print(line, end='')



>>> list(range(5)), list(range(2, 5)), list(range(0, 10, 2))
([0, 1, 2, 3, 4], [2, 3, 4], [0, 2, 4, 6, 8])



>>> list(range(-5, 5))
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

>>> list(range(5, -5, -1))
[5, 4, 3, 2, 1, 0, -1, -2, -3, -4]



>>> for i in range(3):
...     print(i, 'Pythons')
...
0 Pythons
1 Pythons
2 Pythons



>>> X = 'spam'
>>> for item in X: print(item, end=' ')           # Simple iteration
...
s p a m



>>> i = 0
>>> while i < len(X):                             # while loop iteration
...     print(X[i], end=' ')
...     i += 1
...
s p a m



>>> X
'spam'
>>> len(X)                                        # Length of string
4
>>> list(range(len(X)))                           # All legal offsets into X
[0, 1, 2, 3]
>>>
>>> for i in range(len(X)): print(X[i], end=' ')  # Manual for indexing
...
s p a m



>>> for item in X: print(item)                    # Simple iteration
...



>>> S = 'abcdefghijk'
>>> list(range(0, len(S), 2))
[0, 2, 4, 6, 8, 10]

>>> for i in range(0, len(S), 2): print(S[i], end=' ')
...
a c e g i k



>>> S = 'abcdefghijk'
>>> for c in S[::2]: print(c, end=' ')
...
a c e g i k



>>> L = [1, 2, 3, 4, 5]

>>> for x in L:
...     x += 1
...
>>> L
[1, 2, 3, 4, 5]
>>> x
6



>>> L = [1, 2, 3, 4, 5]

>>> for i in range(len(L)):          # Add one to each item in L
...     L[i] += 1                    # Or L[i] = L[i] + 1
...
>>> L
[2, 3, 4, 5, 6]



>>> i = 0
>>> while i < len(L):
...     L[i] += 1
...     i += 1
...
>>> L
[3, 4, 5, 6, 7]



[x+1 for x in L]



>>> L1 = [1,2,3,4]
>>> L2 = [5,6,7,8]



>>> zip(L1, L2)
<zip object at 0x026523C8>
>>> list(zip(L1, L2))                       # list() required in 3.0, not 2.6
[(1, 5), (2, 6), (3, 7), (4, 8)]



>>> for (x, y) in zip(L1, L2):
...     print(x, y, '--', x+y)
...
1 5 -- 6
2 6 -- 8
3 7 -- 10
4 8 -- 12



>>> T1, T2, T3 = (1,2,3), (4,5,6), (7,8,9)
>>> T3
(7, 8, 9)
>>> list(zip(T1, T2, T3))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]



>>> S1 = 'abc'
>>> S2 = 'xyz123'
>>>
>>> list(zip(S1, S2))
[('a', 'x'), ('b', 'y'), ('c', 'z')]



>>> S1 = 'abc'
>>> S2 = 'xyz123'

>>> map(None, S1, S2)                        # 2.X only
[('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None,'3')]



>>> list(map(ord, 'spam'))
[115, 112, 97, 109]



>>> res = []
>>> for c in 'spam': res.append(ord(c))
>>> res
[115, 112, 97, 109]



>>> D1 = {'spam':1, 'eggs':3, 'toast':5}
>>> D1
{'toast': 5, 'eggs': 3, 'spam': 1}

>>> D1 = {}
>>> D1['spam']  = 1
>>> D1['eggs']  = 3
>>> D1['toast'] = 5



>>> keys = ['spam', 'eggs', 'toast']
>>> vals = [1, 3, 5]



>>> list(zip(keys, vals))
[('spam', 1), ('eggs', 3), ('toast', 5)]

>>> D2 = {}
>>> for (k, v) in zip(keys, vals): D2[k] = v
...
>>> D2
{'toast': 5, 'eggs': 3, 'spam': 1}



>>> keys = ['spam', 'eggs', 'toast']
>>> vals = [1, 3, 5]

>>> D3 = dict(zip(keys, vals))
>>> D3
{'toast': 5, 'eggs': 3, 'spam': 1}


>>> S = 'spam'
>>> offset = 0
>>> for item in S:
...     print(item, 'appears at offset', offset)
...     offset += 1
...
s appears at offset 0
p appears at offset 1
a appears at offset 2
m appears at offset 3



>>> S = 'spam'
>>> for (offset, item) in enumerate(S):
...     print(item, 'appears at offset', offset)
...
s appears at offset 0
p appears at offset 1
a appears at offset 2
m appears at offset 3



>>> E = enumerate(S)
>>> E
<enumerate object at 0x02765AA8>
>>> next(E)
(0, 's')
>>> next(E)
(1, 'p')
>>> next(E)
(2, 'a')



>>> [c * i for (i, c) in enumerate(S)]
['', 'p', 'aa', 'mmm']



