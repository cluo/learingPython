>>> def f(a):                 # a is assigned to (references) passed object
...     a = 99                # Changes local variable a only
...
>>> b = 88
>>> f(b)                      # a and b both reference same 88 initially 
>>> print(b)                  # b is not changed
88



>>> def changer(a, b):        # Arguments assigned references to objects
...     a = 2                 # Changes local name's value only
...     b[0] = 'spam'         # Changes shared object in-place
...
>>> X = 1
>>> L = [1, 2]                # Caller
>>> changer(X, L)             # Pass immutable and mutable objects
>>> X, L                      # X is unchanged, L is different!
(1, ['spam', 2])



>>> X = 1
>>> a = X               # They share the same object
>>> a = 2               # Resets 'a' only, 'X' is still 1
>>> print(X)
1



>>> L = [1, 2]
>>> b = L               # They share the same object
>>> b[0] = 'spam'       # In-place change: 'L' sees the change too
>>> print(L)
['spam', 2]



L = [1, 2]
changer(X, L[:])        # Pass a copy, so our 'L' does not change


def changer(a, b):
   b = b[:]             # Copy input list so we don't impact caller
   a = 2
   b[0] = 'spam'        # Changes our list copy only


L = [1, 2]
changer(X, tuple(L))    # Pass a tuple, so changes are errors



>>> def multiple(x, y):
...     x = 2               # Changes local names only
...     y = [3, 4]
...     return x, y         # Return new values in a tuple
...
>>> X = 1
>>> L = [1, 2]
>>> X, L = multiple(X, L)   # Assign results to caller's names
>>> X, L
(2, [3, 4])



def f((a, (b, c))): 

def f(T): (a, (b, c)) = T



>>> def f(a, b, c): print(a, b, c)
...


>>> f(1, 2, 3)
1 2 3


>>> f(c=3, b=2, a=1)
1 2 3


>>> f(1, c=3, b=2)
1 2 3


func(name='Bob', age=40, job='dev')



>>> def f(a, b=2, c=3): print(a, b, c)
...


>>> f(1)
1 2 3
>>> f(a=1)
1 2 3


>>> f(1, 4)
1 4 3
>>> f(1, 4, 5)
1 4 5


>>> f(1, c=6)
1 2 6



def func(spam, eggs, toast=0, ham=0):   # First 2 required
    print((spam, eggs, toast, ham))

func(1, 2)                              # Output: (1, 2, 0, 0)
func(1, ham=1, eggs=0)                  # Output: (1, 0, 0, 1)
func(spam=1, eggs=0)                    # Output: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)           # Output: (3, 2, 1, 0)
func(1, 2, 3, 4)                        # Output: (1, 2, 3, 4)



>>> def f(*args): print(args)
...


>>> f()
()
>>> f(1)
(1,)
>>> f(1, 2, 3, 4)
(1, 2, 3, 4)


>>> def f(**args): print(args)
...
>>> f()
{}
>>> f(a=1, b=2)
{'a': 1, 'b': 2}


>>> def f(a, *pargs, **kargs): print(a, pargs, kargs)
...
>>> f(1, 2, 3, x=1, y=2)
1 (2, 3) {'y': 2, 'x': 1}



>>> def func(a, b, c, d): print(a, b, c, d)
...
>>> args = (1, 2)
>>> args += (3, 4)
>>> func(*args)
1 2 3 4

>>> args = {'a': 1, 'b': 2, 'c': 3}
>>> args['d'] = 4
>>> func(**args)
1 2 3 4



>>> func(*(1, 2), **{'d': 4, 'c': 4})
1 2 4 4

>>> func(1, *(2, 3), **{'d': 4})
1 2 3 4

>>> func(1, c=3, *(2,), **{'d': 4})
1 2 3 4

>>> func(1, *(2, 3), d=4)
1 2 3 4

>>> f(1, *(2,), c=3, **{'d':4})
1 2 3 4



if <test>:
    action, args = func1, (1,)             # Call func1 with 1 arg in this case
else:
    action, args = func2, (1, 2, 3)        # Call func2 with 3 args here
...
action(*args)                              # Dispatch generically



>>> args = (2,3) 
>>> args += (4,)
>>> args
(2, 3, 4)
>>> func(*args)



def tracer(func, *pargs, **kargs):         # Accept arbitrary arguments
    print('calling:', func.__name__)
    return func(*pargs, **kargs)           # Pass along arbitrary arguments

def func(a, b, c, d):
    return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))



func(*pargs, **kargs)             # Newer call syntax: func(*sequence, **dict)

apply(func, pargs, kargs)         # Defunct built-in:  apply(func, sequence, dict)


>>> def echo(*args, **kwargs): print(args, kwargs)
...
>>> echo(1, 2, a=3, b=4)
(1, 2) {'a': 3, 'b': 4}


>>> pargs = (1, 2)
>>> kargs = {'a':3, 'b':4}

>>> apply(echo, pargs, kargs)
(1, 2) {'a': 3, 'b': 4}

>>> echo(*pargs, **kargs)
(1, 2) {'a': 3, 'b': 4}


>>> echo(0, c=5, *pargs, **kargs)      # Normal, keyword, *sequence, **dictionary
(0, 1, 2) {'a': 3, 'c': 5, 'b': 4}



>>> def kwonly(a, *b, c):
...     print(a, b, c)
...
>>> kwonly(1, 2, c=3)
1 (2,) 3
>>> kwonly(a=1, c=3)
1 () 3
>>> kwonly(1, 2, 3)
TypeError: kwonly() needs keyword-only argument c



>>> def kwonly(a, *, b, c):
...     print(a, b, c)
...
>>> kwonly(1, c=3, b=2)
1 2 3
>>> kwonly(c=3, b=2, a=1)
1 2 3
>>> kwonly(1, 2, 3)
TypeError: kwonly() takes exactly 1 positional argument (3 given)
>>> kwonly(1)
TypeError: kwonly() needs keyword-only argument b



>>> def kwonly(a, *, b='spam', c='ham'):
...     print(a, b, c)
...
>>> kwonly(1)
1 spam ham
>>> kwonly(1, c=3)
1 spam 3
>>> kwonly(a=1)
1 spam ham
>>> kwonly(c=3, b=2, a=1)
1 2 3
>>> kwonly(1, 2)
TypeError: kwonly() takes exactly 1 positional argument (2 given)



>>> def kwonly(a, *, b, c='spam'):
...     print(a, b, c)
...
>>> kwonly(1, b='eggs')
1 eggs spam
>>> kwonly(1, c='eggs')
TypeError: kwonly() needs keyword-only argument b
>>> kwonly(1, 2)
TypeError: kwonly() takes exactly 1 positional argument (2 given)

>>> def kwonly(a, *, b=1, c, d=2): 
...     print(a, b, c, d)
...
>>> kwonly(3, c=4)
3 1 4 2
>>> kwonly(3, c=4, b=5)
3 5 4 2
>>> kwonly(3)
TypeError: kwonly() needs keyword-only argument c
>>> kwonly(1, 2, 3)
TypeError: kwonly() takes exactly 1 positional argument (3 given)



>>> def kwonly(a, **pargs, b, c):
SyntaxError: invalid syntax
>>> def kwonly(a, **, b, c):
SyntaxError: invalid syntax


>>> def f(a, *b, **d, c=6): print(a, b, c, d)          # Keyword-only before **!
SyntaxError: invalid syntax

>>> def f(a, *b, c=6, **d): print(a, b, c, d)          # Collect args in header
...
>>> f(1, 2, 3, x=4, y=5)                               # Default used
1 (2, 3) 6 {'y': 5, 'x': 4}

>>> f(1, 2, 3, x=4, y=5, c=7)                          # Override default
1 (2, 3) 7 {'y': 5, 'x': 4}

>>> f(1, 2, 3, c=7, x=4, y=5)                          # Anywhere in keywords
1 (2, 3) 7 {'y': 5, 'x': 4}

>>> def f(a, c=6, *b, **d): print(a, b, c, d)          # c is not keyword-only!
...
>>> f(1, 2, 3, x=4)
1 (3,) 2 {'x': 4}



>>> def f(a, *b, c=6, **d): print(a, b, c, d)          # KW-only between * and **
...
>>> f(1, *(2, 3), **dict(x=4, y=5))                    # Unpack args at call
1 (2, 3) 6 {'y': 5, 'x': 4}

>>> f(1, *(2, 3), **dict(x=4, y=5), c=7)               # Keywords before **args!
SyntaxError: invalid syntax

>>> f(1, *(2, 3), c=7, **dict(x=4, y=5))               # Override default
1 (2, 3) 7 {'y': 5, 'x': 4}

>>> f(1, c=7, *(2, 3), **dict(x=4, y=5))               # After or before *
1 (2, 3) 7 {'y': 5, 'x': 4}

>>> f(1, *(2, 3), **dict(x=4, y=5, c=7))               # Keyword-only in **
1 (2, 3) 7 {'y': 5, 'x': 4}



process(X, Y, Z)                    # use flag's default
process(X, Y, notify=True)          # override flag default

def process(*args, notify=False): ...



### file: mins.py

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    tmp = list(args)            # Or, in Python 2.4+: return sorted(args)[0]
    tmp.sort()
    return tmp[0]

print(min1(3,4,1,2))
print(min2("bb", "aa"))
print(min3([2,2], [1,1], [3,3]))



### file: minmax.py

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y                # See also: lambda
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))       # Self-test code
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))



### file: inter2.py

def intersect(*args):
    res = []
    for x in args[0]:                  # Scan first sequence
        for other in args[1:]:         # For all other args
            if x not in other: break   # Item in each one?
        else:                          # No: break out of loop
            res.append(x)              # Yes: add items to end
    return res

def union(*args):
    res = []
    for seq in args:                   # For all args
        for x in seq:                  # For all nodes
            if not x in res:
                res.append(x)          # Add new items to result
    return res



>>> from inter2 import intersect, union
>>> s1, s2, s3 = "SPAM", "SCAM", "SLAM"

>>> intersect(s1, s2), union(s1, s2)           # Two operands
(['S', 'A', 'M'], ['S', 'P', 'A', 'M', 'C'])

>>> intersect([1,2,3], (1,4))                  # Mixed types
[1]

>>> intersect(s1, s2, s3)                      # Three operands
['S', 'A', 'M']

>>> union(s1, s2, s3)
['S', 'P', 'A', 'M', 'C', 'L']



### file: print30.py (first version)

"""
emulate most of the 3.0 print function for use in 2.X
call signature: print30(*args, sep=' ', end='\n', file=None)
"""
import sys

def print30(*args, **kargs):
    sep  = kargs.get('sep', ' ')             # Keyword arg defaults
    end  = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first  = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)



### file: testprint30.py

from print30 import print30
print30(1, 2, 3)
print30(1, 2, 3, sep='')                     # Suppress separator
print30(1, 2, 3, sep='...')
print30(1, [2], (3,), sep='...')             # Various object types

print30(4, 5, 6, sep='', end='')             # Suppress newline
print30(7, 8, 9)
print30()                                    # Add newline (or blank line)

import sys
print30(1, 2, 3, sep='??', end='.\n', file=sys.stderr)    # Redirect to file



### file print30.py, modified

# Use keyword-only args

def print30(*args, sep=' ', end='\n', file=sys.stdout):
    output = ''
    first  = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)



>>> print30(99, name='bob')
TypeError: print30() got an unexpected keyword argument 'name'



### file print30.py, modified

# Use keyword args deletion with defaults

def print30(*args, **kargs):
    sep  = kargs.pop('sep', ' ')
    end  = kargs.pop('end', '\n')
    file = kargs.pop('file', sys.stdout)
    if kargs: raise TypeError('extra keywords: %s' % kargs)
    output = ''
    first  = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)



>>> print30(99, name='bob')
TypeError: extra keywords: {'name': 'bob'}



# the following are incomplete examples

from tkinter import *
widget = Button(text="Press me", command=someFunction)

sorted(iterable, key=None, reverse=False)




#### quiz code


>>> def func(a, b=4, c=5):
...     print(a, b, c)
...
>>> func(1, 2)



>>> def func(a, b, c=5):
...     print(a, b, c)
...
>>> func(1, c=3, b=2)



>>> def func(a, *pargs):
...     print(a, pargs)
...
>>> func(1, 2, 3)



>>> def func(a, **kargs):
...     print(a, kargs)
...
>>> func(a=1, c=3, b=2)



>>> def func(a, b, c=3, d=4): print(a, b, c, d)
...
>>> func(1, *(5,6))












