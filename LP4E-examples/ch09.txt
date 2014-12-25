>>> (1, 2) + (3, 4)          # Concatenation
(1, 2, 3, 4)

>>> (1, 2) * 4               # Repetition
(1, 2, 1, 2, 1, 2, 1, 2)

>>> T = (1, 2, 3, 4)         # Indexing, slicing
>>> T[0], T[1:3]
(1, (2, 3))



>>> x = (40)        # An integer!
>>> x
40
>>> y = (40,)       # A tuple containing an integer
>>> y
(40,)



>>> T = ('cc', 'aa', 'dd', 'bb')
>>> tmp = list(T)                     # Make a list from a tuple's items
>>> tmp.sort()                        # Sort the list
>>> tmp
['aa', 'bb', 'cc', 'dd']
>>> T = tuple(tmp)                    # Make a tuple from the list's items
>>> T
('aa', 'bb', 'cc', 'dd')

>>> sorted(T)                         # Or use the sorted built-in
['aa', 'bb', 'cc', 'dd']



>>> T = (1, 2, 3, 4, 5)
>>> L = [x + 20 for x in T]
>>> L
[21, 22, 23, 24, 25]



>>> T = (1, 2, 3, 2, 4, 2)       # Tuple methods in 2.6 and 3.0
>>> T.index(2)                   # Offset of first appearance of 2
1
>>> T.index(2, 2)                # Offset of appearance after offset 2
3 
>>> T.count(2)                   # How many 2s are there?
3



>>> T = (1, [2, 3], 4)
>>> T[1] = 'spam'                # This fails: can't change tuple itself
TypeError: object doesn't support item assignment

>>> T[1][0] = 'spam'             # This works: can change mutables inside
>>> T
(1, ['spam', 3], 4)



>>> myfile = open('myfile.txt', 'w')          # Open for text output: create/empty
>>> myfile.write('hello text file\n')         # Write a line of text: string
16
>>> myfile.write('goodbye text file\n')
18
>>> myfile.close()                            # Flush output buffers to disk

>>> myfile = open('myfile.txt')               # Open for text input: 'r' is default
>>> myfile.readline()                         # Read the lines back
'hello text file\n'
>>> myfile.readline()
'goodbye text file\n'
>>> myfile.readline()                         # Empty string: end of file
''


>>> open('myfile.txt').read()                 # Read all at once into string
'hello text file\ngoodbye text file\n'

>>> print(open('myfile.txt').read())          # User-friendly display
hello text file
goodbye text file

>>> for line in open('myfile'):               # Use file iterators, not reads
...     print(line, end='')
...
hello text file
goodbye text file



# NOTE: there was an unfortunate error in the following in 
# the first printing (a "data = data[4:8]" line was lost in 
# a bad cut-and-paste); I've corrected the code here

>>> data = open('data.bin', 'rb').read()      # Open binary file: rb=read binary
>>> data                                      # bytes string holds binary data
b'\x00\x00\x00\x07spam\x00\x08'
>>> data[4:8]                                 # Act like strings
b'spam'
>>> data[4:8][0]                              # But really are small 8-bit integers
115
>>> bin(data[4:8][0])                         # Python 3.0 bin() function
'0b1110011'



>>> X, Y, Z = 43, 44, 45                    # Native Python objects
>>> S = 'Spam'                              # Must be strings to store in file
>>> D = {'a': 1, 'b': 2}
>>> L = [1, 2, 3]
>>>
>>> F = open('datafile.txt', 'w')           # Create output file
>>> F.write(S + '\n')                       # Terminate lines with \n
>>> F.write('%s,%s,%s\n' % (X, Y, Z))       # Convert numbers to strings
>>> F.write(str(L) + '$' + str(D) + '\n')   # Convert and separate with $
>>> F.close()


>>> chars = open('datafile.txt').read()           # Raw string display
>>> chars
"Spam\n43,44,45\n[1, 2, 3]${'a': 1, 'b': 2}\n"
>>> print(chars)                                  # User-friendly display
Spam
43,44,45
[1, 2, 3]${'a': 1, 'b': 2}



>>> F = open('datafile.txt')           # Open again
>>> line = F.readline()                # Read one line
>>> line
'Spam\n'
>>> line.rstrip()                      # Remove end-of-line
'Spam'



>>> line = F.readline()                # Next line from file
>>> line                               # It's a string here
'43,44,45\n'
>>> parts = line.split(',')            # Split (parse) on commas
>>> parts
['43', '44', '45\n']



>>> int(parts[1])                      # Convert from string to int
44
>>> numbers = [int(P) for P in parts]  # Convert all in list at once
>>> numbers
[43, 44, 45]



>>> line = F.readline()
>>> line
"[1, 2, 3]${'a': 1, 'b': 2}\n"
>>> parts = line.split('$')            # Split (parse) on $
>>> parts
['[1, 2, 3]', "{'a': 1, 'b': 2}\n"]
>>> eval(parts[0])                     # Convert to any object type
[1, 2, 3]
>>> objects = [eval(P) for P in parts] # Do same for all in list
>>> objects
[[1, 2, 3], {'a': 1, 'b': 2}]



>>> D = {'a': 1, 'b': 2}
>>> F = open('datafile.pkl', 'wb')
>>> import pickle
>>> pickle.dump(D, F)                  # Pickle any object to file
>>> F.close()

>>> F = open('datafile.pkl', 'rb')
>>> E = pickle.load(F)                 # Load any object from file
>>> E
{'a': 1, 'b': 2}

>>> open('datafile.pkl', 'rb').read()  # Format is prone to change!
b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02K\x02u.'



>>> F = open('data.bin', 'wb')                   # Open binary output file
>>> import struct
>>> data = struct.pack('>i4sh', 7, 'spam', 8)    # Make packed binary data
>>> data
b'\x00\x00\x00\x07spam\x00\x08'
>>> F.write(data)                                # Write byte string
>>> F.close()



>>> F = open('data.bin', 'rb')
>>> data = F.read()                              # Get packed binary data
>>> data
b'\x00\x00\x00\x07spam\x00\x08'
>>> values = struct.unpack('>i4sh', data)        # Convert to Python objects
>>> values
(7, 'spam', 8)



with open(r'C:\misc\data.txt') as myfile:        # See Chapter 33 for details
    for line in myfile:
        ...use line here...



myfile = open(r'C:\misc\data.txt')
try:
    for line in myfile:
        ...use line here...
finally:
    myfile.close()



class MySequence:
    def __getitem__(self, index):
        # Called on self[index], others
    def __add__(self, other):
        # Called on self + other



>>> L = ['abc', [(1, 2), ([3], 4)], 5]
>>> L[1]
[(1, 2), ([3], 4)]
>>> L[1][1]
([3], 4)
>>> L[1][1][0]
[3]
>>> L[1][1][0][0]
3



>>> X = [1, 2, 3]
>>> L = ['a', X, 'b']          # Embed references to X's object
>>> D = {'x':X, 'y':2}

>>> X[1] = 'surprise'          # Changes all three references!
>>> L
['a', [1, 'surprise', 3], 'b']
>>> D
{'x': [1, 'surprise', 3], 'y': 2}



>>> L = [1,2,3]
>>> D = {'a':1, 'b':2}

>>> A = L[:]            # Instead of A = L (or list(L))
>>> B = D.copy()        # Instead of B = D (ditto for sets)

>>> A[1] = 'Ni'
>>> B['c'] = 'spam'
>>>
>>> L, D
([1, 2, 3], {'a': 1, 'b': 2})
>>> A, B
([1, 'Ni', 3], {'a': 1, 'c': 'spam', 'b': 2})



>>> X = [1, 2, 3]
>>> L = ['a', X[:], 'b']     # Embed copies of X's object
>>> D = {'x':X[:], 'y':2}



>>> L1 = [1, ('a', 3)]         # Same value, unique objects
>>> L2 = [1, ('a', 3)]
>>> L1 == L2, L1 is L2         # Equivalent? Same object?
(True, False)

>>> S1 = 'spam'
>>> S2 = 'spam'

>>> S1 == S2, S1 is S2
(True, True)

>>> S1 = 'a longer string'
>>> S2 = 'a longer string'
>>> S1 == S2, S1 is S2
(True, False)

>>> L1 = [1, ('a', 3)]
>>> L2 = [1, ('a', 2)]
>>> L1 < L2, L1 == L2, L1 > L2     # Less, equal, greater: tuple of results
(False, False, True)



C:\misc> c:\python26\python
>>> D1 = {'a':1, 'b':2}
>>> D2 = {'a':1, 'b':3}
>>> D1 == D2
False
>>> D1 < D2
True


C:\misc> c:\python30\python
>>> D1 = {'a':1, 'b':2}
>>> D2 = {'a':1, 'b':3}
>>> D1 == D2
False
>>> D1 < D2
TypeError: unorderable types: dict() < dict()

>>> list(D1.items())
[('a', 1), ('b', 2)]
>>> sorted(D1.items())
[('a', 1), ('b', 2)]

>>> sorted(D1.items()) < sorted(D2.items())
True
>>> sorted(D1.items()) > sorted(D2.items())
False



>>> L = [None] * 100
>>>
>>> L
[None, None, None, None, None, None, None, ... ]



>>> bool(1)
True
>>> bool('spam')
True
>>> bool({})
False



type([1]) == type([])             # Type of another list
type([1]) == list                 # List type name
isinstance([1], list)             # List or customization thereof

import types                      # types has names for other types
def f(): pass
type(f) == types.FunctionType



>>> L = [1, 2, 3]
>>> M = ['X', L, 'Y']      # Embed a reference to L
>>> M
['X', [1, 2, 3], 'Y']

>>> L[1] = 0               # Changes M too
>>> M
['X', [1, 0, 3], 'Y']


>>> L = [1, 2, 3]
>>> M = ['X', L[:], 'Y']   # Embed a copy of L
>>> L[1] = 0               # Changes only L, not M
>>> L
[1, 0, 3]
>>> M
['X', [1, 2, 3], 'Y']



>>> L = [4, 5, 6]
>>> X = L * 4              # Like [4, 5, 6] + [4, 5, 6] + ...
>>> Y = [L] * 4            # [L] + [L] + ... = [L, L,...]
>>> X
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
>>> Y
[[4, 5, 6], [4, 5, 6], [4, 5, 6], [4, 5, 6]]

>>> L[1] = 0               # Impacts Y but not X
>>> X
[4, 5, 6, 4, 5, 6, 4, 5, 6, 4, 5, 6]
>>> Y
[[4, 0, 6], [4, 0, 6], [4, 0, 6], [4, 0, 6]]



>>> L = ['grail']         # Append reference to same object
>>> L.append(L)           # Generates cycle in object: [...]
>>> L
['grail', [...]]



T = (1, 2, 3)
T[2] = 4                 # Error!
T = T[:2] + (4,)         # OK: (1, 2, 4)




#### lab code

2 ** 16
2 / 5, 2 / 5.0
"spam" + "eggs"
S = "ham"
"eggs " + S
S * 5
S[:0]
"green %s and %s" % ("eggs", S)
'green {0} and {1}'.format('eggs', S)
('x',)[0]
('x', 'y')[1]
L = [1,2,3] + [4,5,6]
L, L[:], L[:0], L[-2], L[-2:]
([1,2,3] + [4,5,6])[2:4]
[L[2], L[3]]
L.reverse(); L
L.sort(); L
L.index(4)
{'a':1, 'b':2}['b']
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0
D['x'] + D['w']
D[(1,2,3)] = 4
list(D.keys()), list(D.values()), (1,2,3) in D
[[]], ["",[],(),{},None]



>>> X = 'spam'
>>> Y = 'eggs'
>>> X, Y = Y, X


>>> D = {}
>>> D[1] = 'a'
>>> D[2] = 'b'

>>> D[(1, 2, 3)] = 'c'
>>> D
{1: 'a', 2: 'b', (1, 2, 3): 'c'}



