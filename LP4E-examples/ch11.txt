>>> nudge = 1
>>> wink  = 2
>>> A, B = nudge, wink             # Tuple assignment
>>> A, B                           # Like A = nudge; B = wink
(1, 2)
>>> [C, D] = [nudge, wink]         # List assignment
>>> C, D
(1, 2)



>>> nudge = 1
>>> wink  = 2
>>> nudge, wink = wink, nudge      # Tuples: swaps values
>>> nudge, wink                    # Like T = nudge; nudge = wink; wink = T
(2, 1)



>>> [a, b, c] = (1, 2, 3)          # Assign tuple of values to list of names
>>> a, c
(1, 3)
>>> (a, b, c) = "ABC"              # Assign string of characters to tuple
>>> a, c
('A', 'C')



>>> string = 'SPAM'
>>> a, b, c, d = string                            # Same number on both sides
>>> a, d
('S', 'M')

>>> a, b, c = string                               # Error if not
...error text omitted...
ValueError: too many values to unpack



>>> a, b, c = string[0], string[1], string[2:]     # Index and slice
>>> a, b, c
('S', 'P', 'AM')

>>> a, b, c = list(string[:2]) + [string[2:]]      # Slice and concatenate
>>> a, b, c
('S', 'P', 'AM')

>>> a, b = string[:2]                              # Same, but simpler
>>> c = string[2:]
>>> a, b, c
('S', 'P', 'AM')

>>> (a, b), c = string[:2], string[2:]             # Nested sequences
>>> a, b, c
('S', 'P', 'AM')



>>> ((a, b), c) = ('SP', 'AM')                     # Paired by shape and position
>>> a, b, c
('S', 'P', 'AM')



for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ...…          # Simple tuple assignment

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ...…    # Nested tuple assignment

def f(((a, b), c)):              # For arguments too in Python 2.6, but not 3.0
f(((1, 2), 3))

>>> red, green, blue = range(3)
>>> red, blue
(0, 2)

>>> range(3)                             # Use list(range(3)) in Python 3.0
[0, 1, 2]



>>> L = [1, 2, 3, 4]
>>> while L:
...     front, L = L[0], L[1:]           # See next section for 3.0 alternative
...     print(front, L)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []



C:\misc> c:\python30\python
>>> seq = [1, 2, 3, 4]
>>> a, b, c, d = seq
>>> print(a, b, c, d)
1 2 3 4

>>> a, b = seq
ValueError: too many values to unpack



>>> a, *b = seq
>>> a
1
>>> b
[2, 3, 4]



>>> *a, b = seq
>>> a
[1, 2, 3]
>>> b
4



>>> a, *b, c = seq
>>> a
1
>>> b
[2, 3]
>>> c
4



>>> a, b, *c = seq
>>> a
1
>>> b
2
>>> c
[3, 4]



>>> a, *b = 'spam'
>>> a, b
('s', ['p', 'a', 'm'])

>>> a, *b, c = 'spam'
>>> a, b, c
('s', ['p', 'a'], 'm')



>>> S = 'spam'

>>> S[0], S[1:]       # Slices are type-specific, * assignment always returns a list
('s', 'pam')

>>> S[0], S[1:3], S[3]     
('s', 'pa', 'm')



>>> L = [1, 2, 3, 4]
>>> while L:
...     front, *L = L                    # Get first, rest without slicing
...     print(front, L)
...
1 [2, 3, 4]
2 [3, 4]
3 [4]
4 []



>>> seq
[1, 2, 3, 4]

>>> a, b, c, *d = seq
>>> print(a, b, c, d)
1 2 3 [4]



>>> a, b, c, d, *e = seq
>>> print(a, b, c, d, e)
1 2 3 4 []

>>> a, b, *e, c, d = seq
>>> print(a, b, c, d, e)
1 2 3 4 []



>>> a, *b, c, *d = seq
SyntaxError: two starred expressions in assignment

>>> a, b = seq
ValueError: too many values to unpack

>>> *a = seq
SyntaxError: starred assignment target must be in a list or tuple

>>> *a, = seq
>>> a
[1, 2, 3, 4]



>>> seq
[1, 2, 3, 4]

>>> a, *b = seq                        # First, rest
>>> a, b
(1, [2, 3, 4])

>>> a, b = seq[0], seq[1:]             # First, rest: traditional
>>> a, b
(1, [2, 3, 4])



>>> *a, b = seq                        # Rest, last
>>> a, b
([1, 2, 3], 4)

>>> a, b = seq[:-1], seq[-1]           # Rest, last: traditional
>>> a, b
([1, 2, 3], 4)



for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]: 
    ...

a, *b, c = (1, 2, 3, 4)                            # b gets [2, 3]

for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:           # a, b, c = (1, 2, 3), ...

for all in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    a, b, c = all[0], all[1:3], all[3]



>>> a = b = c = 'spam'
>>> a, b, c
('spam', 'spam', 'spam')



>>> c = 'spam'
>>> b = c
>>> a = b



>>> a = b = 0
>>> b = b + 1
>>> a, b
(0, 1)


>>> a = b = []
>>> b.append(42)
>>> a, b
([42], [42])



>>> a = []
>>> b = []
>>> b.append(42)
>>> a, b
([], [42])



>>> x = 1
>>> x = x + 1                   # Traditional
>>> x
2
>>> x += 1                      # Augmented
>>> x
3



>>> S = "spam"
>>> S += "SPAM"                 # Implied concatenation
>>> S
'spamSPAM'



>>> L = [1, 2]
>>> L = L + [3]                 # Concatenate: slower
>>> L
[1, 2, 3]
>>> L.append(4)                 # Faster, but in-place
>>> L
[1, 2, 3, 4]



>>> L = L + [5, 6]              # Concatenate: slower
>>> L
[1, 2, 3, 4, 5, 6]
>>> L.extend([7, 8])            # Faster, but in-place
>>> L
[1, 2, 3, 4, 5, 6, 7, 8]



>>> L += [9, 10]                # Mapped to L.extend([9, 10])
>>> L
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



>>> L = [1, 2]
>>> M = L                       # L and M reference the same object
>>> L = L + [3, 4]              # Concatenation makes a new object
>>> L, M                        # Changes L but not M
([1, 2, 3, 4], [1, 2])

>>> L = [1, 2]
>>> M = L
>>> L += [3, 4]                 # But += really means extend
>>> L, M                        # M sees the in-place change too!
([1, 2, 3, 4], [1, 2, 3, 4])



>>> x = 0               # x bound to an integer object
>>> x = "Hello"         # Now it's a string
>>> x = [1, 2, 3]       # And now it's a list



>>> x = print('spam')         # print is a function call expression in 3.0
spam
>>> print(x)                  # But it is coded as an expression statement
None



>>> L = [1, 2]
>>> L.append(3)               # Append is an in-place change
>>> L
[1, 2, 3]


>>> L = L.append(4)           # But append returns None, not L
>>> print(L)                  # So we lose our list!
None



C:\misc> c:\python30\python
>>>
>>> print()                                      # Display a blank line

>>> x = 'spam'
>>> y = 99
>>> z = ['eggs']
>>>
>>> print(x, y, z)                               # Print 3 objects per defaults
spam 99 ['eggs']



>>> print(x, y, z, sep='')                       # Suppress separator
spam99['eggs']
>>>
>>> print(x, y, z, sep=', ')                     # Custom separator
spam, 99, ['eggs']



>>> print(x, y, z, end='')                        # Suppress line break
spam 99 ['eggs']>>>
>>>
>>> print(x, y, z, end=''); print(x, y, z)        # Two prints, same output line
spam 99 ['eggs']spam 99 ['eggs']
>>> print(x, y, z, end='...\n')                   # Custom line end
spam 99 ['eggs']...
>>>



>>> print(x, y, z, sep='...', end='!\n')          # Multiple keywords
spam...99...['eggs']!
>>> print(x, y, z, end='!\n', sep='...')          # Order doesn't matter
spam...99...['eggs']!



>>> print(x, y, z, sep='...', file=open('data.txt', 'w'))      # Print to a file
>>> print(x, y, z)                                             # Back to stdout
spam 99 ['eggs']
>>> print(open('data.txt').read())                             # Display file text
spam...99...['eggs']



>>> text = '%s: %-.4f, %05d' % ('Result', 3.14159, 42)
>>> print(text)
Resulprint(X, Y)                            # Or, in 2.6: print X, Yt: 3.1416, 00042
>>> print('%s: %-.4f, %05d' % ('Result', 3.14159, 42))
Result: 3.1416, 00042



C:\misc> c:\python26\python
>>>
>>> x = 'a'
>>> y = 'b'
>>> print x, y
a b


>>> print x, y,; print x, y
a b a b


>>> print x + y
ab
>>> print '%s...%s' % (x, y)
a...b



>>> print('hello world')               # Print a string object in 3.0
hello world

>>> print 'hello world'                # Print a string object in 2.6
hello world

>>> 'hello world'                      # Interactive echoes
'hello world'

>>> import sys                         # Printing the hard way
>>> sys.stdout.write('hello world\n')
hello world



print(X, Y)                            # Or, in 2.6: print X, Y

import sys
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')

import sys
sys.stdout = open('log.txt', 'a')       # Redirects prints to a file
...
print(x, y, x)                          # Shows up in log.txt



C:\misc> c:\python30\python
>>> import sys
>>> temp = sys.stdout                   # Save for restoring later
>>> sys.stdout = open('log.txt', 'a')   # Redirect prints to a file
>>> print('spam')                       # Prints go to file, not here
>>> print(1, 2, 3)
>>> sys.stdout.close()                  # Flush output to disk
>>> sys.stdout = temp                   # Restore original stream

>>> print('back here')                  # Prints show up here again
back here
>>> print(open('log.txt').read())       # Result of earlier prints
spam
1 2 3



log =  open('log.txt', 'a')             # 3.0
print(x, y, z, file=log)                # Print to a file-like object
print(a, b, c)                          # Print to original stdout

log =  open('log.txt', 'a')             # 2.6
print >> log, x, y, z                   # Print to a file-like object
print a, b, c                           # Print to original stdout



C:\misc> c:\python30\python
>>> log = open('log.txt', 'w')
>>> print(1, 2, 3, file=log)            # 2.6: print >> log, 1, 2, 3
>>> print(4, 5, 6, file=log)
>>> log.close()
>>> print(7, 8, 9)                      # 2.6: print 7, 8, 9
7 8 9
>>> print(open('log.txt').read())
1 2 3
4 5 6



>>> import sys
>>> sys.stderr.write(('Bad!' * 8) + '\n')
Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad!

>>> print('Bad!' * 8, file=sys.stderr)     # 2.6: print >> sys.stderr, 'Bad' * 8
Bad!Bad!Bad!Bad!Bad!Bad!Bad!Bad!



>>> X = 1; Y = 2
>>> print(X, Y)                                            # Print: the easy way
1 2
>>> import sys                                             # Print: the hard way
>>> sys.stdout.write(str(X) + ' ' + str(Y) + '\n')
1 2
4
>>> print(X, Y, file=open('temp1', 'w'))                   # Redirect text to file

>>> open('temp2', 'w').write(str(X) + ' ' + str(Y) + '\n') # Send to file manually
4
>>> print(open('temp1', 'rb').read())                      # Binary mode for bytes
b'1 2\r\n'
>>> print(open('temp2', 'rb').read())
b'1 2\r\n'



from __future__ import print_function


C:\misc> c:\python30\python
>>> print('spam')                       # 3.0 print function call syntax
spam
>>> print('spam', 'ham', 'eggs')        # These are mutiple argments
spam ham eggs


C:\misc> c:\python26\python 
>>> print('spam')                       # 2.6 print statement, enclosing parens
spam
>>> print('spam', 'ham', 'eggs')          # This is really a tuple object!
('spam', 'ham', 'eggs')


>>> print('%s %s %s' % ('spam', 'ham', 'eggs'))
spam ham eggs
>>> print('{0} {1} {2}'.format('spam', 'ham', 'eggs'))
spam ham eggs



class FileFaker:
    def write(self, string):
        # Do something with printed text in string

import sys
sys.stdout = FileFaker()
print(someObjects)              # Sends to class write method

myobj = FileFaker()             # 3.0: Redirect to object for one print
print(someObjects, file=myobj)  # Does not reset sys.stdout

myobj = FileFaker()             # 2.6: same effect
print >> myobj, someObjects     # Does not reset sys.stdout

python script.py < inputfile > outputfile
python script.py | filterProgram












