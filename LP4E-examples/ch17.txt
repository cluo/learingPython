X = 99

def func():
    X = 88



# Global scope
X = 99                # X and func assigned in module: global

def func(Y):          # Y and Z assigned in function: locals
    # Local scope
    Z = X + Y         # X is a global
    return Z

func(1)               # func in module: result=100



>>> import builtins
>>> dir(builtins)



>>> zip                         # The normal way
<class 'zip'>

>>> import builtins             # The hard way
>>> builtins.zip
<class 'zip'>



def hider():
    open = 'spam'              # Local variable, hides built-in
    ...
    open('data.txt')           # This won't open a file now in this scope!



X = 88                         # Global X

def func():
    X = 99                     # Local X: hides global

func()
print(X)                       # Prints 88: unchanged



X = 88                         # Global X

def func():
    global X
    X = 99                     # Global X: outside def

func()
print(X)                       # Prints 99



y, z = 1, 2                    # Global variables in module
def all_global():
    global x                   # Declare globals assigned
    x = y + z                  # No need to declare y, z: LEGB rule



X = 99
def func1():
    global X
    X = 88

def func2():
    global X
    X = 77



# first.py
X = 99                    # This code doesn't know about second.py

# second.py
import first
print(first.X)            # Okay: references a name in another file
first.X = 88              # But changing it can be too subtle and implicit



# first.py
X = 99

def setX(new):
    global X
    X = new

# second.py
import first
first.setX(88)



# thismod.py

var = 99                              # Global variable == module attribute

def local():
    var = 0                           # Change local var

def glob1():
    global var                        # Declare global (normal)
    var += 1                          # Change global var

def glob2():
    var = 0                           # Change local var
    import thismod                    # Import myself
    thismod.var += 1                  # Change global var

def glob3():
    var = 0                           # Change local var
    import sys                        # Import system table
    glob = sys.modules['thismod']     # Get module object (or use __name__)
    glob.var += 1                     # Change global var

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)



>>> import thismod
>>> thismod.test()
99
102
>>> thismod.var
102



X = 99                   # Global scope name: not used

def f1():
    X = 88               # Enclosing def local
    def f2():
        print(X)         # Reference made in nested def
    f2()

f1()                     # Prints 88: enclosing def local



def f1():
    X = 88
    def f2():
        print(X)         # Remembers X in enclosing def scope
    return f2            # Return f2 but don't call it

action = f1()            # Make, return function
action()                 # Call it now: prints 88



>>> def maker(N):
...     def action(X):                    # Make and return action
...         return X ** N                 # action retains N from enclosing scope
...     return action
...

>>> f = maker(2)                          # Pass 2 to N
>>> f
<function action at 0x014720B0>

>>> f(3)                                  # Pass 3 to X, N remembers 2: 3 ** 2
9
>>> f(4)                                  # 4 ** 2
16

>>> g = maker(3)                          # g remembers 3, f remembers 2
>>> g(3)                                  # 3 ** 3
27
>>> f(3)                                  # 3 ** 2
9



def f1():
    x = 88
    def f2(x=x):                # Remember enclosing scope X with defaults
        print(x)
    f2()

f1()                            # Prints 88



>>> def f1():
...     x = 88                  # Pass x along instead of nesting
...     f2(x)                   # Forward reference okay
...
>>> def f2(x):
...     print(x)
...
>>> f1()
88



def func():
    x = 4
    action = (lambda n: x ** n)          # x remembered from enclosing def
    return action

x = func()
print(x(2))                              # Prints 16, 4 ** 2



def func():
    x = 4
    action = (lambda n, x=x: x ** n)     # Pass x in manually
    return action



>>> def makeActions():
...     acts = []
...     for i in range(5):                       # Tries to remember each i
...         acts.append(lambda x: i ** x)        # All remember same last i!
...     return acts
...
>>> acts = makeActions()
>>> acts[0]
<function <lambda> at 0x012B16B0>



>>> acts[0](2)                                   # All are 4 ** 2, value of last i
16
>>> acts[2](2)                                   # This should be 2 ** 2
16
>>> acts[4](2)                                   # This should be 4 ** 2
16



>>> def makeActions():
...     acts = []
...     for i in range(5):                       # Use defaults instead
...         acts.append(lambda x, i=i: i ** x)   # Remember current i
...     return acts
...
>>> acts = makeActions()
>>> acts[0](2)                                   # 0 ** 2
0
>>> acts[2](2)                                   # 2 ** 2
4
>>> acts[4](2)                                   # 4 ** 2
16



>>> def f1():
...     x = 99
...     def f2():
...         def f3():
...             print(x)        # Found in f1's local scope!
...         f3()
...     f2()
...
>>> f1()
99



def func():
    nonlocal name1, name2, ...



C:\\misc>c:\python30\python

>>> def tester(start):
...     state = start                      # Referencing nonlocals works normally 
...     def nested(label):
...         print(label, state)            # Remembers state in enclosing scope
...     return nested
...
>>> F = tester(0)
>>> F('spam')
spam 0
>>> F('ham')
ham 0



>>> def tester(start):
...     state = start
...     def nested(label):
...         print(label, state)
...         state += 1                     # Cannot change by default (or in 2.6)
...     return nested
...
>>> F = tester(0)
>>> F('spam')
UnboundLocalError: local variable 'state' referenced before assignment



>>> def tester(start):                     
...     state = start                      # Each call gets its own state
...     def nested(label):
...         nonlocal state                 # Remembers state in enclosing scope
...         print(label, state)
...         state += 1                     # Allowed to change it if nonlocal
...     return nested
...
>>> F = tester(0)
>>> F('spam')                              # Increments state on each call
spam 0
>>> F('ham')
ham 1
>>> F('eggs')
eggs 2


>>> G = tester(42)                # Make a new tester that starts at 42
>>> G('spam')
spam 42

>>> G('eggs')                     # My state information updated to 43
eggs 43

>>> F('bacon')                    # But F's is where it left off: at 3
bacon 3                           # Each call has different state information



>>> def tester(start):
...     def nested(label):
...         nonlocal state        # Nonlocals must already exist in enclosing def!
...         state = 0
...         print(label, state)
...     return nested
...
SyntaxError: no binding for nonlocal 'state' found

>>> def tester(start):
...     def nested(label):
...         global state          # Globals don't have to exist yet when declared
...         state = 0             # This creates the name in the module now
...         print(label, state)
...     return nested
...
>>> F = tester(0)
>>> F('abc')
abc 0
>>> state
0



>>> spam = 99
>>> def tester():
...     def nested():
...         nonlocal spam               # Must be in a def, not the module!
...         print('Current=', spam)
...         spam += 1
...     return nested
...
SyntaxError: no binding for nonlocal 'spam' found




def tester(start):
    state = start                       # Each call gets its own state 
    def nested(label):
        nonlocal state                  # Remembers state in enclosing scope
        print(label, state)
        state += 1                      # Allowed to change it if nonlocal
    return nested

F = tester(0)                           
F('spam')



>>> def tester(start):
...     global state                    # Move it out to the module to change it
...     state = start                   # global allows changes in module scope
...     def nested(label):
...         global state
...         print(label, state)
...         state += 1
...     return nested
...
>>> F = tester(0)
>>> F('spam')                           # Each call increments shared global state
spam 0
>>> F('eggs')
eggs 1


>>> G = tester(42)        # Resets state's single copy in global scope
>>> G('toast')           
toast 42

>>> G('bacon')
bacon 43

>>> F('ham')              # Oops -- my counter has been overwritten!
ham 44



>>> class tester:                          # Class-based alternative (see Part VI)
...     def __init__(self, start):         # On object construction,
...         self.state = start             # save state explicitly in new object
...     def nested(self, label):
...         print(label, self.state)       # Reference state explicitly
...         self.state += 1                # Changes are always allowed
...
>>> F = tester(0)                          # Create instance, invoke __init__
>>> F.nested('spam')                       # F is passed to self
spam 0
>>> F.nested('ham')
ham 1

>>> G = tester(42)                         # Each instance gets new copy of state
>>> G.nested('toast')                      # Changing one does not impact others
toast 42
>>> G.nested('bacon')
bacon 43

>>> F.nested('eggs')                       # F's state is where it left off
eggs 2
>>> F.state                                # State may be accessed outside class
3



>>> class tester:
...     def __init__(self, start):
...         self.state = start
...     def __call__(self, label):            # Intercept direct instance calls
...         print(label, self.state)          # So .nested() not required
...         self.state += 1
...
>>> H = tester(99)
>>> H('juice')                                # Invokes __call__
juice 99
>>> H('pancakes')
pancakes 100



>>> def tester(start):
...     def nested(label):
...         print(label, nested.state)      # nested is in enclosing scope
...         nested.state += 1               # Change attr, not nested itself
...     nested.state = start                # Initial state after func defined
...     return nested
...
>>> F = tester(0)
>>> F('spam')            # F is a 'nested' with state attached
spam 0                   # each generated function has its own state
>>> F('ham')
ham 1
>>> F.state              # Can access state outside functions too
2
>>>
>>> G = tester(42)       # G has its own state, doesn't overwrite F's
>>> G('eggs')
eggs 42
>>> F('ham')
ham 2



# NOTE: per this book's updates page (http://www.rmi.net/~lutz/lp4e-updates.html),
# it's also possible to retain state by changing a mutable object in-place through
# its name in the enclosing scopem without a "nonlocal"; this is a bit more obscurem
# but an option in Python 2.X; the following is not in the book, but shows how:

>>> def tester(start):
...     def nested(label):
...         print(label, state[0])
...         state[0] += 1              # changes object, not name
...     state = [start]
...     return nested
...
>>> F = tester(0)                      # per-call state retained again:
>>> F('spam')                          # each tester() has new local scope
('spam', 0)
>>> F('eggs')                          # but no F.state accessible here
('eggs', 1)
>>>
>>> G = tester(42)
>>> G('ham')
('ham', 42)
>>> G('bacon')
('bacon', 43)
>>>
>>> F('sausage')
('sausage', 2)




#### quiz code


>>> X = 'Spam'
>>> def func():
...     print(X)
...
>>> func()



>>> X = 'Spam'
>>> def func():
...     X = 'NI!'
...
>>> func()
>>> print(X)



>>> X = 'Spam'
>>> def func():
...     X = 'NI'
...     print(X)
...
>>> func()
>>> print(X)



>>> X = 'Spam'
>>> def func():
...     global X
...     X = 'NI'
...
>>> func()
>>> print(X)



>>> X = 'Spam'
>>> def func():
...     X = 'NI'
...     def nested():
...         print(X)
...     nested()
...
>>> func()
>>> X



>>> def func():
...     X = 'NI'
...     def nested():
...         nonlocal X
...         X = 'Spam'
...     nested()
...     print(X)
...
>>> func()







