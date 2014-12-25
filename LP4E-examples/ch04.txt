>>> 123 + 222                     # Integer addition
345
>>> 1.5 * 4                       # Floating-point multiplication
6.0
>>> 2 ** 100                      # 2 to the power 100
1267650600228229401496703205376



>>> len(str(2 ** 1000000))        # How many digits in a really BIG number?
301030



>>> 3.1415 * 2                    # repr: as code
6.2830000000000004
>>> print(3.1415 * 2)             # str: user-friendly
6.283



>>> import math
>>> math.pi
3.1415926535897931
>>> math.sqrt(85)
9.2195444572928871



>>> import random
>>> random.random()
0.59268735266273953
>>> random.choice([1, 2, 3, 4])
1



>>> S = 'Spam'
>>> len(S)               # Length
4
>>> S[0]                 # The first item in S, indexing by zero-based position
'S'
>>> S[1]                 # The second item from the left
'p'



>>> S[-1]                # The last item from the end in S
'm'
>>> S[-2]                # The second to last item from the end
'a'



>>> S[-1]                # The last item in S
'm'
>>> S[len(S)-1]          # Negative indexing, the hard way
'm'



>>> S                    # A 4-character string
'Spam'
>>> S[1:3]               # Slice of S from offsets 1 through 2 (not 3)
'pa'



>>> S[1:]                # Everything past the first (1:len(S))
'pam'
>>> S                    # S itself hasn't changed
'Spam'
>>> S[0:3]               # Everything but the last
'Spa'
>>> S[:3]                # Same as S[0:3]
'Spa'
>>> S[:-1]               # Everything but the last again, but simpler (0:-1)
'Spa'
>>> S[:]                 # All of S as a top-level copy (0:len(S))
'Spam'



>>> S
'Spam'
>>> S + 'xyz'            # Concatenation
'Spamxyz'
>>> S                    # S is unchanged
'Spam'
>>> S * 8                # Repetition
'SpamSpamSpamSpamSpamSpamSpamSpam'



>>> S
'Spam'
>>> S[0] = 'z'           # Immutable objects cannot be changed
...error text omitted...
TypeError: 'str' object does not support item assignment

>>> S = 'z' + S[1:]      # But we can run expressions to make new objects
>>> S
'zpam'



>>> S.find('pa')            # Find the offset of a substring
1
>>> S
'Spam'
>>> S.replace('pa', 'XYZ')  # Replace occurrences of a substring with another
'SXYZm'
>>> S
'Spam'



>>> line = 'aaa,bbb,ccccc,dd'
>>> line.split(',')            # Split on a delimiter into a list of substrings
['aaa', 'bbb', 'ccccc', 'dd']

>>> S = 'spam'
>>> S.upper()                  # Upper- and lowercase conversions
'SPAM'
>>> S.isalpha()                # Content tests: isalpha, isdigit, etc.
True

>>> line = 'aaa,bbb,ccccc,dd\n'
>>> line = line.rstrip()       # Remove whitespace characters on the right side
>>> line
'aaa,bbb,ccccc,dd'



>>> '%s, eggs, and %s' % ('spam', 'SPAM!')        # Formatting expression (all)
'spam, eggs, and SPAM!'

>>> '{0}, eggs, and {1}'.format('spam', 'SPAM!')  # Formatting method (2.6, 3.0)
'spam, eggs, and SPAM!'



>>> dir(S)
>>> help(S.replace)



>>> S = 'A\nB\tC'            # \n is end-of-line, \t is tab
>>> len(S)                   # Each stands for just one character
5
>>> ord('\n')                # \n is a byte with the binary value 10 in ASCII
10
>>> S = 'A\0B\0C'            # \0, a binary zero byte, does not terminate string
>>> len(S)
5



>>> msg = """ aaaaaaaaaaaaa
bbb'''bbbbbbbbbb""bbbbbbb'bbbb
cccccccccccccc"""
>>> msg
'\naaaaaaaaaaaaa\nbbb\'\'\'bbbbbbbbbb""bbbbbbb\'bbbb\ncccccccccccccc'



>>> import re
>>> match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
>>> match.group(1)
'Python '



>>> match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
>>> match.groups()
('usr', 'home', 'lumberjack')



>>> L = [123, 'spam', 1.23]       # A list of three different-type objects
>>> len(L)                        # Number of items in the list
3



>>> L[0]                          # Indexing by position
123
>>> L[:-1]                        # Slicing a list returns a new list
[123, 'spam']
>>> L + [4, 5, 6]                 # Concatenation makes a new list too
[123, 'spam', 1.23, 4, 5, 6]
>>> L                             # We're not changing the original list
[123, 'spam', 1.23]



>>> L.append('NI')                # Growing: add object at end of list
>>> L
[123, 'spam', 1.23, 'NI']
>>> L.pop(2)                      # Shrinking: delete an item in the middle
1.23
>>> L                             # "del L[2]" deletes from a list too
[123, 'spam', 'NI']



>>> M = ['bb', 'aa', 'cc']
>>> M.sort()
>>> M
['aa', 'bb', 'cc']
>>> M.reverse()
>>> M
['cc', 'bb', 'aa']



>>> L
[123, 'spam', 'NI']
>>> L[99]
...error text omitted...
IndexError: list index out of range



>>> L[99] = 1
...error text omitted...
IndexError: list assignment index out of range



>>> M = [[1, 2, 3],          # A 3 × 3 matrix, as nested lists
         [4, 5, 6],          # Code can span lines if bracketed
         [7, 8, 9]]
>>> M
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]



>>> M[1]                     # Get row 2
[4, 5, 6]
>>> M[1][2]                  # Get row 2, then get item 3 within the row
6



>>> col2 = [row[1] for row in M]     # Collect the items in column 2
>>> col2
[2, 5, 8]
>>> M                                # The matrix is unchanged
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]



>>> [row[1] + 1 for row in M]        # Add 1 to each item in column 2
[3, 6, 9]
>>> [row[1] for row in M if row[1] % 2 == 0]      # Filter out odd items
[2, 8]



>>> diag = [M[i][i] for i in [0, 1, 2]]     # Collect a diagonal from matrix
>>> diag
[1, 5, 9]
>>> doubles = [c * 2 for c in 'spam']       # Repeat characters in a string
>>> doubles
['ss', 'pp', 'aa', 'mm']



# Note: see later in the book for more on the iteration protocol; its
# full realization is: G = (...); I = iter(G); I.next() until StopIteration;
# generators are their own iterator (iter(G) returns G itself), so the iter(G)
# call described later in this chapter is not required in the following; 

>>> G = (sum(row) for row in M)             # Create a generator of row sums
>>> next(G)
6
>>> next(G)                                 # Run the iteration protocol
15



>>> list(map(sum, M))                       # Map sum over items in M
[6, 15, 24]



>>> {sum(row) for row in M}                 # Create a set of row sums
{24, 6, 15}
>>> {i : sum(M[i]) for i in range(3)}       # Creates key/value table of row sums
{0: 6, 1: 15, 2: 24}



>>> [ord(x) for x in 'spaam']               # List of character ordinals
[115, 112, 97, 97, 109]
>>> {ord(x) for x in 'spaam'}               # Sets remove duplicates
{112, 97, 115, 109}
>>> {x: ord(x) for x in 'spaam'}            # Dictionary keys are unique
{'a': 97, 'p': 112, 's': 115, 'm': 109}



>>> D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

>>> D['food']                  # Fetch value of key 'food'
'Spam'
>>> D['quantity'] += 1         # Add 1 to 'quantity' value
>>> D
{'food': 'Spam', 'color': 'pink', 'quantity': 5}



>>> D = {}
>>> D['name'] = 'Bob'          # Create keys by assignment
>>> D['job'] = 'dev'
>>> D['age'] = 40
>>> D
{'age': 40, 'job': 'dev', 'name': 'Bob'}
>>> print(D['name'])
Bob



>>> rec = {'name': {'first': 'Bob', 'last': 'Smith'},
           'job':  ['dev', 'mgr'],
           'age':  40.5}



>>> rec['name']                     # 'name' is a nested dictionary
{'last': 'Smith', 'first': 'Bob'}
>>> rec['name']['last']             # Index the nested dictionary
'Smith'
>>> rec['job']                      # 'job' is a nested list
['dev', 'mgr']
>>> rec['job'][-1]                  # Index the nested list
'mgr'
>>> rec['job'].append('janitor')    # Expand Bob's job description in-place
>>> rec
{'age': 40.5, 'job': ['dev', 'mgr', 'janitor'], 'name': {'last': 'Smith',
'first': 'Bob'}}



>>> rec = 0 # Now the object's space is reclaimed



>>> D = {'a': 1, 'b': 2, 'c': 3}
>>> D
{'a': 1, 'c': 3, 'b': 2}



>>> Ks = list(D.keys())            # Unordered keys list
>>> Ks                             # A list in 2.6, "view" in 3.0: use list()
['a', 'c', 'b']
>>> Ks.sort()                      # Sorted keys list
>>> Ks
['a', 'b', 'c']
>>> for key in Ks:                 # Iterate though sorted keys
        print(key, '=>', D[key])   # <== press Enter twice here

a => 1
b => 2
c => 3



>>> D
{'a': 1, 'c': 3, 'b': 2}
>>> for key in sorted(D):
        print(key, '=>', D[key])

a => 1
b => 2
c => 3



>>> for c in 'spam':
        print(c.upper())

S
P
A
M



>>> x = 4
>>> while x > 0:
        print('spam!' * x)
        x -= 1

spam!spam!spam!spam!
spam!spam!spam!
spam!spam!
spam!



>>> squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
>>> squares
[1, 4, 9, 16, 25]



>>> squares = []
>>> for x in [1, 2, 3, 4, 5]:       # This is what a list comprehension does
        squares.append(x ** 2)      # Both run the iteration protocol internally

>>> squares
[1, 4, 9, 16, 25]



>>> D
{'a': 1, 'c': 3, 'b': 2}
>>> D['e'] = 99                      # Assigning new keys grows dictionaries
>>> D
{'a': 1, 'c': 3, 'b': 2, 'e': 99}
>>> D['f']                           # Referencing a nonexistent key is an error
...error text omitted...
KeyError: 'f'



>>> 'f' in D
False
>>> if not 'f' in D:
        print('missing')

missing



>>> value = D.get('x', 0)                  # Index but with a default
>>> value
0
>>> value = D['x'] if 'x' in D else 0      # if/else expression form
>>> value
0



>>> T = (1, 2, 3, 4)                       # A 4-item tuple
>>> len(T)                                 # Length
4
>> T + (5, 6)                              # Concatenation
(1, 2, 3, 4, 5, 6)
>>> T[0]                                   # Indexing, slicing, and more
1


>>> T.index(4)                             # Tuple methods: 4 appears at offset 3
3
>>> T.count(4)                             # 4 appears once
1


>>> T[0] = 2                               # Tuples are immutable
...error text omitted...
TypeError: 'tuple' object does not support item assignment



>>> T = ('spam', 3.0, [11, 22, 33])
>>> T[1]
3.0
>>> T[2][1]
22



>>> f = open('data.txt', 'w')    # Make a new file in output mode
>>> f.write('Hello\n')           # Write strings of bytes to it
6
>>> f.write('world\n')           # Returns number of bytes written in Python 3.0
6
>>> f.close()                    # Close to flush output buffers to disk



>>> f = open('data.txt')         # 'r' is the default processing mode
>>> text = f.read()              # Read entire file into a string
>>> text
'Hello\nworld\n'
>>> print(text)                  # print interprets control characters
Hello
world
>>> text.split()                 # File content is always a string
['Hello', 'world']


>>> dir(f)
>>> help(f.seek)



# Note: the following won't work unless you've already created a binary 
# data file in your working directory; to see how to do so, see the 
# files coverage of Chaptrer 9 later in this book. 

>>> data = open('data.bin', 'rb').read()     # Open binary file
>>> data                                     # bytes string holds binary data
b'\x00\x00\x00\x07spam\x00\x08'
>>> data[4:8]
b'spam'



>>> X = set('spam')                # Make a set out of a sequence in 2.6 and 3.0
>>> Y = {'h', 'a', 'm'}            # Make a set with new 3.0 set literals
>>> X, Y
({'a', 'p', 's', 'm'}, {'a', 'h', 'm'})
>>> X & Y                          # Intersection
{'a', 'm'}
>>> X | Y                          # Union
{'a', 'p', 's', 'h', 'm'}
>>> X – Y                          # Difference
{'p', 's'}
>>> {x ** 2 for x in [1, 2, 3, 4]} # Set comprehensions in 3.0
{16, 1, 4, 9}
>>> T.append(4)
AttributeError: 'tuple' object has no attribute 'append'



>>> 1 / 3                              # Floating-point (use .0 in Python 2.6)
0.33333333333333331
>>> (2/3) + (1/2)
1.1666666666666665

>>> import decimal                     # Decimals: fixed precision
>>> d = decimal.Decimal('3.141')
>>> d + 1
Decimal('4.141')

>>> decimal.getcontext().prec = 2
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.33')

>>> from fractions import Fraction     # Fractions: numerator+denominator
>>> f = Fraction(2, 3)
>>> f + 1
Fraction(5, 3)
>>> f + Fraction(1, 2)
Fraction(7, 6)



>>> 1 > 2, 1 < 2                       # Booleans
(False, True)
>>> bool('spam')
True
>>> X = None                           # None placeholder
>>> print(X)
None
>>> L = [None] * 100                   # Initialize a list of 100 Nones
>>> L
[None, None, None, None, None, None, None, None, None, None, None, None,
None, None, None, None, None, None, None, None, ...a list of 100 Nones...]



# In Python 2.6:
>>> type(L)                     # Types: type of L is list type object
<type 'list'>
>>> type(type(L))               # Even types are objects
<type 'type'>

# In Python 3.0:
>>> type(L)                     # 3.0: types are classes, and vice versa
<class 'list'>
>>> type(type(L))               # See Chapter 31 for more on class types
<class 'type'>



>>> if type(L) == type([]):     # Type testing, if you must...
        print('yes')

yes
>>> if type(L) == list:         # Using the type name
        print('yes')

yes
>>> if isinstance(L, list):     # Object-oriented tests
        print('yes')

yes



>>> class Worker:
        def __init__(self, name, pay):       # Initialize when created
            self.name = name                 # self is the new object
            self.pay = pay
        def lastName(self):
            return self.name.split()[-1]     # Split string on blanks
        def giveRaise(self, percent):
            self.pay *= (1.0 + percent)      # Update pay in-place


>>> bob = Worker('Bob Smith', 50000)         # Make two instances
>>> sue = Worker('Sue Jones', 60000)         # Each has name and pay attrs
>>> bob.lastName()                           # Call method: bob is self
'Smith'
>>> sue.lastName()                           # sue is the self subject
'Jones'
>>> sue.giveRaise(.10)                       # Updates sue's pay
>>> sue.pay
66000.0
