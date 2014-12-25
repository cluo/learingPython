### file: module1.py

def printer(x):                   # Module attribute
    print(x)



>>> import module1                         # Get module as a whole
>>> module1.printer('Hello world!')        # Qualify to get names
Hello world!



>>> from module1 import printer            # Copy out one variable
>>> printer('Hello world!')                # No need to qualify name
Hello world!



>>> from module1 import *                   # Copy out all variables
>>> printer('Hello world!')
Hello world!



### file: simple.py

print('hello')
spam = 1                   # Initialize variable



>>> import simple          # First import: loads and runs file's code
hello
>>> simple.spam            # Assignment makes an attribute
1



>>> simple.spam = 2        # Change attribute in module
>>> import simple          # Just fetches already loaded module
>>> simple.spam            # Code wasn't rerun: attribute unchanged
2



### file: small.py

x = 1
y = [1, 2]



>>> from small import x, y         # Copy two names out
>>> x = 42                         # Changes local x only
>>> y[0] = 42                      # Changes shared mutable in-place



>>> import small                   # Get module name (from doesn't)
>>> small.x                        # Small's x is not my x
1
>>> small.y                        # But we share a changed mutable
[42, 2]



>>> from small import x, y         # Copy two names out
>>> x = 42                         # Changes my x only

>>> import small                   # Get module name
>>> small.x = 42                   # Changes x in other module



from module import name1, name2     # Copy these two names out (only)

import module                       # Fetch the module object
name1 = module.name1                # Copy names out by assignment
name2 = module.name2
del module                          # Get rid of the module name



# M.py

def func():
    ...do something...

# N.py

def func():
    ...do something else...


# O.py

from M import func
from N import func        # This overwites the one we got from M
func()                    # Calls N.func only


# O.py

import M, N               # Get the whole modules, not their names
M.func()                  # We can call both names now
N.func()                  # The module names make them unique



### file: module2.py

print('starting to load...')
import sys
name = 42

def func(): pass

class klass: pass

print('done loading.')



>>> import module2
starting to load...
done loading.

>>> module2.sys
<module 'sys' (built-in)>

>>> module2.name
42

>>> module2.func
<function func at 0x026D3BB8>

>>> module2.klass
<class 'module2.klass'>



>>> list(module2.__dict__.keys())
['name', '__builtins__', '__file__', '__package__', 'sys', 'klass', 'func', 
'__name__', '__doc__']



## file: moda.py

X = 88                        # My X: global to this file only
def f():
    global X                  # Change this file's X
    X = 99                    # Cannot see names in other modules



### file: modb.py

X = 11                        # My X: global to this file only

import moda                   # Gain access to names in moda
moda.f()                      # Sets moda.X, not this file's X
print(X, moda.X)



% python modb.py
11 99



### file: mod3.py

X = 3


### file: mod2.py

X = 2
import mod3

print(X, end=' ')             # My global X
print(mod3.X)                 # mod3’s X


### file: mod1.py

X = 1
import mod2

print(X, end=' ')             # My global X
print(mod2.X, end=' ')        # mod2's X
print(mod2.mod3.X)            # Nested mod3's X



% python mod1.py
2 3
1 2 3



### file: changer.py

message = "First version"
def printer():
    print(message)



>>> import changer
>>> changer.printer()
First version



### file: changer.py (edited and saved)

message = "After editing"
def printer():
    print('reloaded:', message)



>>> import changer
>>> changer.printer()                 # No effect: uses loaded module
First version
>>> from imp import reload
>>> reload(changer)                   # Forces new code to load/run
<module 'changer' from 'changer.py'>
>>> changer.printer()                 # Runs the new version now
reloaded: After editing




