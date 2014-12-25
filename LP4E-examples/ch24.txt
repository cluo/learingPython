__all__ = ["Error", "encode", "decode"]     # Export these only

from __future__ import featurename



### file: runme.py

def tester():
    print("It's Christmas in Heaven...")

if __name__ == '__main__':           # Only when run
    tester()                         # Not when imported



% python
>>> import runme
>>> runme.tester()
It's Christmas in Heaven...



% python runme.py
It's Christmas in Heaven...



### file: min.py 

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

print(minmax(lessthan, 4, 2, 1, 5, 6, 3))        # Self-test code
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))



### file: min.py (modified)

print('I am:', __name__)

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res

def lessthan(x, y): return x < y
def grtrthan(x, y): return x > y

if __name__ == '__main__':
    print(minmax(lessthan, 4, 2, 1, 5, 6, 3))    # Self-test code
    print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))



% python min.py
I am: __main__
1
6



>>> import min
I am: min
>>> min.minmax(min.lessthan, 's', 'p', 'a', 'm')
'a'



### file: formats.py

"""
Various specialized string display formatting utilities.
Test me with canned self-test or command-line arguments.
"""

def commas(N):
    """
    format positive integer-like N for display with
    commas between digit groupings: xxx,yyy,zzz
    """
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

def money(N, width=0):
    """
    format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: $  -xxx,yyy.zz
    """
    sign   = '-' if N < 0 else ''
    N      = abs(N)
    whole  = commas(int(N))
    fract  = ('%.2f' % N)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format) 

if __name__ == '__main__':
    def selftest():
        tests  = 0, 1        # fails: -1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))
        
        print('')
        tests  = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2**32 + .2345)
        tests += (2 ** 100), -(2 ** 100)
        for test in tests:
            print('%s [%s]' % (money(test, 17), test))

    import sys
    if len(sys.argv) == 1:
        selftest()
    else:                                      
        print(money(float(sys.argv[1]), int(sys.argv[2])))



C:\misc> python formats.py 999999999 0
$999,999,999.00

C:\misc> python formats.py -999999999 0
$-999,999,999.00

C:\misc> python formats.py 123456789012345 0
$123,456,789,012,345.00

C:\misc> python formats.py -123456789012345 25
$  -123,456,789,012,345.00

C:\misc> python formats.py 123.456 0
$123.46

C:\misc> python formats.py -123.454 0
$-123.45

C:\misc> python formats.py
...canned tests: try this yourself...



>>> from formats import money, commas
>>> money(123.456)
'$123.46'
>>> money(-9999999.99, 15)
'$  -9,999,999.99'
>>> X = 99999999999999999999
>>> '%s (%s)' % (commas(X), X)
'99,999,999,999,999,999,999 (99999999999999999999)'



>>> import formats
>>> help(formats)
Help on module formats:

NAME
    formats

FILE
    c:\misc\formats.py

DESCRIPTION
    Various specialized string display formatting utilities.
    Test me with canned self-test or command-line arguments.

FUNCTIONS
    commas(N)
        format positive integer-like N for display with
        commas between digit groupings: xxx,yyy,zzz

    money(N, width=0)
        format number N for display with commas, 2 decimal digits,
        leading $ and sign, and optional padding: $  -xxx,yyy.zz



>>> import sys
>>> sys.path
['', 'C:\\users', 'C:\\Windows\\system32\\python30.zip', ...more deleted...]

>>> sys.path.append('C:\\sourcedir')         # Extend module search path
>>> import string                            # All imports search the new dir last



>>> sys.path = [r'd:\temp']                  # Change module search path
>>> sys.path.append('c:\\lp4e\\examples')    # For this process only
>>> sys.path
['d:\\temp', 'c:\\lp4e\\examples']

>>> import string
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named string



import modulename as name

import modulename
name = modulename
del modulename                                # Don't keep original name

from modulename import attrname as name

import reallylongmodulename as name           # Use shorter nickname
name.func()

from module1 import utility as util1          # Can have only 1 "utility"
from module2 import utility as util2
util1(); util2()

import dir1.dir2.mod as mod                   # Only list full path once
mod.func()



M.name                                        # Qualify object
M.__dict__['name']                            # Index namespace dictionary manually
sys.modules['M'].name                         # Index loaded-modules table manually
getattr(M, 'name')                            # Call built-in fetch function



### file: mydir.py

"""
mydir.py: a module that lists the namespaces of other modules
"""

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0
    for attr in module.__dict__:              # Scan namespace keys
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<built-in name>')          # Skip __file__, etc.
        else:
            print(getattr(module, attr))      # Same as .__dict__[attr]
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)

if __name__ == '__main__':
    import mydir
    listing(mydir)                            # Self-test code: list myself



>>> import mydir
>>> help(mydir)

C:\misc> c:\Python30\python mydir.py

>>> import mydir
>>> import tkinter
>>> mydir.listing(tkinter)
------------------------------------------------------------
name: tkinter file: c:\PYTHON30\lib\tkinter\__init__.py
------------------------------------------------------------
...



>>> import "string"
  File "<stdin>", line 1
    import "string"
                  ^
SyntaxError: invalid syntax



x = "string"
import x



>>> modname = "string"
>>> exec("import " + modname)      # Run a string of code
>>> string                         # Imported in this namespace
<module 'string' from 'c:\Python30\lib\string.py'>



>>> modname = "string"
>>> string = __import__(modname)
>>> string
<module 'string' from 'c:\Python30\lib\string.py'>



import B                   # Not reloaded when A is
import C                   # Just an import of an already loaded module

% python
>>> . . .
>>> from imp import reload
>>> reload(A)



### file: reloadall.py

"""
reloadall.py: transitively reload nested modules 
"""

import types
from imp import reload                               # from required in 3.0

def status(module):
    print('reloading ' + module.__name__)

def transitive_reload(module, visited):
    if not module in visited:                        # Trap cycles, duplicates
        status(module)                               # Reload this module
        reload(module)                               # And visit children
        visited[module] = None
        for attrobj in module.__dict__.values():     # For all attrs
            if type(attrobj) == types.ModuleType:    # Recur if module
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

if __name__ == '__main__':
    import reloadall                                 # Test code: reload myself
    reload_all(reloadall)                            # Should reload this, types



C:\misc> c:\Python30\python reloadall.py
reloading reloadall
reloading types



>>> from reloadall import reload_all
>>> import os, tkinter

>>> reload_all(os)
reloading os
reloading copyreg
reloading ntpath
reloading genericpath
reloading stat
reloading sys
reloading errno

>>> reload_all(tkinter)
reloading tkinter
reloading _tkinter
reloading tkinter._fix
reloading sys
reloading ctypes
reloading os
reloading copyreg
reloading ntpath
reloading genericpath
reloading stat
reloading errno
reloading ctypes._endian
reloading tkinter.constants



### file names in comments

import b                          # a.py
X = 1

import c                          # b.py
Y = 2

Z = 3                             # c.py


C:\misc> C:\Python30\python
>>> import a
>>> a.X, a.b.Y, a.b.c.Z
(1, 2, 3)

# Change all three files' assignment values and save

>>> from imp import reload
>>> reload(a)                     # Normal reload is top level only
<module 'a' from 'a.py'>
>>> a.X, a.b.Y, a.b.c.Z
(111, 2, 3)

>>> from reloadall import reload_all
>>> reload_all(a)
reloading a
reloading b
reloading c
>>> a.X, a.b.Y, a.b.c.Z           # Reloads all nested modules too
(111, 222, 333)



func1()                           # Error: "func1" not yet assigned

def func1():
    print(func2())                # OK: "func2" looked up later

func1()                           # Error: "func2" not yet assigned

def func2():
    return "Hello"

func1()                           # Okay: "func1" and "func2" assigned



# nested1.py
X = 99
def printer(): print(X)


# nested2.py
from nested1 import X, printer    # Copy names out
X = 88                            # Changes my "X" only!
printer()                         # nested1's X is still 99


% python nested2.py
99


# nested3.py
import nested1                    # Get module as a whole
nested1.X = 88                    # OK: change nested1's X
nested1.printer()

% python nested3.py
88



>>> from module1 import *          # Bad: may overwrite my names silently
>>> from module2 import *          # Worse: no way to tell what we get!
>>> from module3 import *
>>> . . .

>>> func()                         # Huh???



from module import X          # X may not reflect any module reloads!
 . . .
from imp import reload
reload(module)                # Changes module, but not my names
X                             # Still references old object


import module                 # Get module, not names
 . . .
from imp import reload
reload(module)                # Changes module in-place
module.X                      # Get current X: reflects module reloads



from module import function
function(1, 2, 3)

from imp import reload
reload(module)

from imp import reload
import module
reload(module)
function(1, 2, 3)

from imp import reload
import module
reload(module)
from module import function        # Or give up, and use module.function()
function(1, 2, 3)



### file names in comments

# recur1.py
X = 1
import recur2                             # Run recur2 now if it doesn't exist
Y = 2


# recur2.py
from recur1 import X                      # OK: "X" already assigned
from recur1 import Y                      # Error: "Y" not yet assigned


C:\misc> C:\Python30\python
>>> import recur1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "recur1.py", line 2, in <module>
    import recur2
  File "recur2.py", line 2, in <module>
    from recur1 import Y
ImportError: cannot import name Y








