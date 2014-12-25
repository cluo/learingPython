### file: number.py

class Number:
    def __init__(self, start):                  # On Number(start)
        self.data = start
    def __sub__(self, other):                   # On instance - other
        return Number(self.data - other)        # Result is a new instance

>>> from number import Number                   # Fetch class from module
>>> X = Number(5)                               # Number.__init__(X, 5)
>>> Y = X – 2                                   # Number.__sub__(X, 2)
>>> Y.data                                      # Y is new Number instance
3



>>> class Indexer:
...     def __getitem__(self, index):
...         return index ** 2
...
>>> X = Indexer()
>>> X[2]                                # X[i] calls X.__getitem__(i) 
4

>>> for i in range(5):
...     print(X[i], end=' ')            # Runs __getitem__(X, i) each time
...
0 1 4 9 16



>>> L = [5, 6, 7, 8, 9]
>>> L[2:4]                              # Slice with slice syntax
[7, 8]
>>> L[1:]
[6, 7, 8, 9]
>>> L[:-1]
[5, 6, 7, 8]
>>> L[::2]
[5, 7, 9]



>>> L[slice(2, 4)]                      # Slice with slice objects
[7, 8]
>>> L[slice(1, None)]
[6, 7, 8, 9]
>>> L[slice(None, -1)]
[5, 6, 7, 8]
>>> L[slice(None, None, 2)]
[5, 7, 9]



>>> class Indexer:
...     data = [5, 6, 7, 8, 9]
...     def __getitem__(self, index):   # Called for index or slice
...         print('getitem:', index)
...         return self.data[index]     # Perform index or slice
...
>>> X = Indexer()
>>> X[0]                                # Indexing sends __getitem__ an integer
getitem: 0
5
>>> X[1]
getitem: 1
6
>>> X[-1]
getitem: -1
9



>>> X[2:4]                              # Slicing sends __getitem__ a slice object
getitem: slice(2, 4, None)
[7, 8]
>>> X[1:]
getitem: slice(1, None, None)
[6, 7, 8, 9]
>>> X[:-1]
getitem: slice(None, -1, None)
[5, 6, 7, 8]
>>> X[::2]
getitem: slice(None, None, 2)
[5, 7, 9]



def __setitem__(self, index, value):    # Intercept index or slice assignment
    ...
    self.data[index] = value            # Assign index or slice



 >>> class C:
...     def __index__(self):
...         return 255
...
>>> X = C()
>>> hex(X)               # Integer value
'0xff'
>>> bin(X)
'0b11111111'
>>> oct(X)
'0o377'

>>> ('C' * 256)[255]
'C'
>>> ('C' * 256)[X]       # As index (not X[i])
'C'
>>> ('C' * 256)[X:]      # As index (not X[i:])
'C'



>>> class stepper:
...     def __getitem__(self, i):
...         return self.data[i]
...
>>> X = stepper()                     # X is a stepper object
>>> X.data = "Spam"
>>>
>>> X[1]                              # Indexing calls __getitem__
'p'
>>> for item in X:                    # for loops call __getitem__
...     print(item, end=' ')          # for indexes items 0..N
...
S p a m



>>> 'p' in X                          # All call __getitem__ too
True

>>> [c for c in X]                    # List comprehension
['S', 'p', 'a', 'm']

>>> list(map(str.upper, X))           # map calls (use list() in 3.0)
['S', 'P', 'A', 'M']

>>> (a, b, c, d) = X                  # Sequence assignments
>>> a, c, d
('S', 'a', 'm')

>>> list(X), tuple(X), ''.join(X)
(['S', 'p', 'a', 'm'], ('S', 'p', 'a', 'm'), 'Spam')

>>> X
<__main__.stepper object at 0x00A8D5D0>



### file: iters.py

class Squares:
    def __init__(self, start, stop):    # Save state when created
        self.value = start - 1
        self.stop  = stop
    def __iter__(self):                 # Get iterator object on iter()
        return self
    def __next__(self):                 # Return a square on each iteration
        if self.value == self.stop:     # Also called by next() built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2



>>> from iters import Squares
>>> for i in Squares(1, 5):             # for calls iter(), which calls __iter__()
...     print(i, end=' ')               # Each iteration calls __next__()
...
1 4 9 16 25



>>> X = Squares(1, 5)                   # Iterate manually: what loops do
>>> I = iter(X)                         # iter() calls __iter__
>>> next(I)                             # next() calls __next__
1
>>> next(I)
4
...more omitted...
>>> next(I)
25
>>> next(I)                             # Can catch this in try statement 
StopIteration



>>> X = Squares(1, 5)
>>> X[1]
AttributeError: Squares instance has no attribute '__getitem__'



>>> X = Squares(1, 5)
>>> [n for n in X]                # Exhausts items
[1, 4, 9, 16, 25]
>>> [n for n in X]                # Now it's empty
[]
>>> [n for n in Squares(1, 5)]    # Make a new iterator object
[1, 4, 9, 16, 25]
>>> list(Squares(1, 3))
[1, 4, 9]



>>> def gsquares(start, stop):
...     for i in range(start, stop+1):
...         yield i ** 2
...
>>> for i in gsquares(1, 5):
...     print(i, end=' ')
...
1 4 9 16 25



>>> [x ** 2 for x in range(1, 6)]
[1, 4, 9, 16, 25]



>>> S = 'ace'
>>> for x in S:
...     for y in S:
...         print(x + y, end=' ')
...
aa ac ae ca cc ce ea ec ee



### file: skipper.py

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped                    # Iterator state information
        self.offset  = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):      # Terminate iterations
            raise StopIteration
        else:
            item = self.wrapped[self.offset]      # else return and skip
            self.offset += 2
            return item

class SkipObject:
    def __init__(self, wrapped):                  # Save item to be used
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)         # New iterator each time

if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)                   # Make container object
    I = iter(skipper)                             # Make an iterator on it
    print(next(I), next(I), next(I))              # Visit offsets 0, 2, 4

    for x in skipper:               # for calls __iter__ automatically
        for y in skipper:           # Nested fors call __iter__ again each time
            print(x + y, end=' ')   # Each iterator has its own state, offset



>>> S = 'abcdef'
>>> for x in S[::2]:
...     for y in S[::2]:            # New objects on each iteration
...         print(x + y, end=' ')
...
aa ac ae ca cc ce ea ec ee



>>> S = 'abcdef'
>>> S = S[::2]
>>> S
'ace'
>>> for x in S:
...     for y in S:                 # Same object, new iterators
...         print(x + y, end=' ')
...
aa ac ae ca cc ce ea ec ee



class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):                 # Fallback for iteration
        print('get[%s]:' % i, end='')         # Also for index, slice
        return self.data[i]
    def __iter__(self):                       # Preferred for iteration
        print('iter=> ', end='')              # Allows only 1 active iterator
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x):                # Preferred for 'in'
        print('contains: ', end='')
        return x in self.data

	
X = Iters([1, 2, 3, 4, 5])          # Make instance
print(3 in X)                       # Membership
for i in X:                         # For loops
    print(i, end=' | ')

print()
print([i ** 2 for i in X])          # Other iteration contexts
print( list(map(bin, X)) )

I = iter(X)                         # Manual iteration (what other contexts do)
while True:
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break



>>> X = Iters('spam')               # Indexing
>>> X[0]                            # __getitem__(0)
get[0]:'s'

>>> 'spam'[1:]                      # Slice syntax
'pam'
>>> 'spam'[slice(1, None)]          # Slice object
'pam'

>>> X[1:]                           # __getitem__(slice(..))
get[slice(1, None, None)]:'pam'
>>> X[:-1]
get[slice(None, -1, None)]:'spa'



>>> class empty:
...     def __getattr__(self, attrname):
...         if attrname == "age":
...             return 40
...         else:
...             raise AttributeError, attrname
...
>>> X = empty()
>>> X.age
40
>>> X.name
...error text omitted...
AttributeError: name



>>> class accesscontrol:
...     def __setattr__(self, attr, value):
...         if attr == 'age':
...             self.__dict__[attr] = value
...         else:
...             raise AttributeError, attr + ' not allowed'
...
>>> X = accesscontrol()
>>> X.age = 40                                  # Calls __setattr__
>>> X.age
40
>>> X.name = 'mel'
...text omitted...
AttributeError: name not allowed



class PrivateExc(Exception): pass                   # More on exceptions later

class Privacy:
    def __setattr__(self, attrname, value):         # On self.attrname = value
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value         # self.attrname = value loops!
class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

x = Test1()
y = Test2()

x.name = 'Bob'
y.name = 'Sue'                                      # Fails

y.age  = 30
x.age  = 40                                         # Fails



>>> class adder:
...     def __init__(self, value=0):
...         self.data = value                    # Initialize data
...     def __add__(self, other):
...         self.data += other                   # Add other in-place (bad!)
...
>>> x = adder()                                  # Default displays
>>> print(x)
<__main__.adder object at 0x025D66B0>
>>> x
<__main__.adder object at 0x025D66B0>



>>> class addrepr(adder):                        # Inherit __init__, __add__
...     def __repr__(self):                      # Add string representation
...         return 'addrepr(%s)' % self.data     # Convert to as-code string
...
>>> x = addrepr(2)                               # Runs __init__
>>> x + 1                                        # Runs __add__
>>> x                                            # Runs __repr__
addrepr(3)
>>> print(x)                                     # Runs __repr__
addrepr(3)
>>> str(x), repr(x)                              # Runs __repr__ for both
('addrepr(3)', 'addrepr(3)')



>>> class addstr(adder):
...     def __str__(self):                       # __str__ but no __repr__
...         return '[Value: %s]' % self.data     # Convert to nice string
...
>>> x = addstr(3)
>>> x + 1
>>> x                                            # Default __repr__
<__main__.addstr object at 0x00B35EF0>
>>> print(x)                                     # Runs __str__
[Value: 4]
>>> str(x), repr(x)
('[Value: 4]', '<__main__.addstr object at 0x00B35EF0>')



>>> class addboth(adder):
...     def __str__(self):
...         return '[Value: %s]' % self.data     # User-friendly string
...     def __repr__(self):
...         return 'addboth(%s)' % self.data     # As-code string
...
>>> x = addboth(4)
>>> x + 1
>>> x                                            # Runs __repr__
addboth(5)
>>> print(x)                                     # Runs __str__
[Value: 5]
>>> str(x), repr(x)
('[Value: 5]', 'addboth(5)')



>>> class Printer:
...     def __init__(self, val):
...         self.val = val
...     def __str__(self):                  # Used for instance itself
...         return str(self.val)            # Convert to a string result
...
>>> objs = [Printer(2), Printer(3)]
>>> for x in objs: print(x)                 # __str__ run when instance printed
...                                         # But not when instance in a list!
2
3
>>> print(objs)
[<__main__.Printer object at 0x025D06F0>, <__main__.Printer object at ...more...
>>> objs
[<__main__.Printer object at 0x025D06F0>, <__main__.Printer object at ...more...



>>> class Printer:
...     def __init__(self, val):
...         self.val = val
...     def __repr__(self):                 # __repr__ used by print if no __str__
...         return str(self.val)            # __repr__ used if echoed or nested
...
>>> objs = [Printer(2), Printer(3)]
>>> for x in objs: print(x)                 # No __str__: runs __repr__
...
2
3
>>> print(objs)                             # Runs __repr__, not ___str__
[2, 3]
>>> objs
[2, 3]



>>> class Commuter:
...     def __init__(self, val):
...         self.val = val
...     def __add__(self, other):
...         print('add', self.val, other)
...         return self.val + other
...     def __radd__(self, other):
...         print('radd', self.val, other)
...         return other + self.val
...
>>> x = Commuter(88)
>>> y = Commuter(99)

>>> x + 1                         # __add__: instance + noninstance       
add 88 1
89
>>> 1 + y                         # __radd__: noninstance + instance
radd 99 1
100
>>> x + y                         # __add__: instance + instance, triggers __radd__
add 88 <__main__.Commuter object at 0x02630910>
radd 99 88
187



>>> class Commuter:                        # Propagate class type in results
...     def __init__(self, val):
...         self.val = val
...     def __add__(self, other):
...         if isinstance(other, Commuter): other = other.val
...         return Commuter(self.val + other)
...     def __radd__(self, other):
...         return Commuter(other + self.val)
...     def __str__(self):
...         return '<Commuter: %s>' % self.val
...
>>> x = Commuter(88)
>>> y = Commuter(99)
>>> print(x + 10)                          # Result is another Commuter instance
<Commuter: 98>
>>> print(10 + y)
<Commuter: 109>

>>> z = x + y                              # Not nested: doesn't recur to __radd__
>>> print(z)
<Commuter: 187>
>>> print(z + 10)
<Commuter: 197>
>>> print(z + z)
<Commuter: 374>



>>> class Number:
...     def __init__(self, val):
...         self.val = val
...     def __iadd__(self, other):             # __iadd__ explicit: x += y
...         self.val += other                  # Usually returns self
...         return self
...
>>> x = Number(5)
>>> x += 1
>>> x += 1
>>> x.val
7
>>> class Number:
...     def __init__(self, val):
...         self.val = val
...     def __add__(self, other):              # __add__ fallback: x = (x + y)
...         return Number(self.val + other)    # Propagates class type
...
>>> x = Number(5)
>>> x += 1
>>> x += 1
>>> x.val
7



>>> class Callee:
...     def __call__(self, *pargs, **kargs):   # Intercept instance calls
...         print('Called:', pargs, kargs)     # Accept arbitrary arguments
...		
>>> C = Callee()
>>> C(1, 2, 3)                                 # C is a callable object
Called: (1, 2, 3) {}
>>> C(1, 2, 3, x=4, y=5)
Called: (1, 2, 3) {'y': 5, 'x': 4}



class C:
    def __call__(self, a, b, c=5, d=6): ...        # Normals and defaults

class C:
    def __call__(self, *pargs, **kargs): ...       # Collect arbitrary arguments

class C:
    def __call__(self, *pargs, d=6, **kargs): ...  # 3.0 keyword-only argument

X = C()
X(1, 2)                             # Omit defaults
X(1, 2, 3, 4)                       # Positionals
X(a=1, b=2, d=4)                    # Keywords
X(*[1, 2], **dict(c=3, d=4))        # Unpack arbitrary arguments
X(1, *(2,), c=3, **dict(d=4))       # Mixed modes



>>> class Prod:
...     def __init__(self, value):             # Accept just one argument
...         self.value = value
...     def __call__(self, other):
...         return self.value * other
...
>>> x = Prod(2)                                # "Remembers" 2 in state
>>> x(3)                                       # 3 (passed) * 2 (state)
6
>>> x(4)
8



>>> class Prod:
...     def __init__(self, value):
...         self.value = value
...     def comp(self, other):
...         return self.value * other
...
>>> x = Prod(3)
>>> x.comp(3)
9
>>> x.comp(4)
12



class Callback:
    def __init__(self, color):               # Function + state information
        self.color = color
    def __call__(self):                      # Support calls with no arguments
        print('turn', self.color)


cb1 = Callback('blue')                       # Remember blue
cb2 = Callback('green')

B1 = Button(command=cb1)                     # Register handlers
B2 = Button(command=cb2)                     # Register handlers


cb1()                                        # On events: prints 'blue'
cb2()                                        # Prints 'green'



cb3 = (lambda color='red': 'turn ' + color)  # Or: defaults
print(cb3())



class Callback:
    def __init__(self, color):               # Class with state information
        self.color = color
    def changeColor(self):                   # A normal named method
        print('turn', self.color)

cb1 = Callback('blue')
cb2 = Callback('yellow')

B1 = Button(command=cb1.changeColor)         # Reference, but don't call
B2 = Button(command=cb2.changeColor)         # Remembers function+self



object = Callback('blue')
cb = object.changeColor                      # Registered event handler
cb()                                         # On event prints 'blue'



class C:
    data = 'spam'                          
    def __gt__(self, other):               # 3.0 and 2.6 version
        return self.data > other
    def __lt__(self, other):
        return self.data < other

X = C()
print(X > 'ham')         # True  (runs __gt__)
print(X < 'ham')         # False (runs __lt__)



class C:
    data = 'spam'                          # 2.6 only
    def __cmp__(self, other):              # __cmp__ not used in 3.0
        return cmp(self.data, other)       # cmp() not defined in 3.0

X = C()
print(X > 'ham')         # True  (runs __cmp__)
print(X < 'ham')         # False (runs __cmp__)



class C:
    data = 'spam'
    def __cmp__(self, other):
        return (self.data > other) - (self.data < other)



>>> class Truth:
...    def __bool__(self): return True
...
>>> X = Truth()
>>> if X: print('yes!')
...
yes!

>>> class Truth:
...    def __bool__(self): return False
...
>>> X = Truth()
>>> bool(X)
False



>>> class Truth:
...    def __len__(self): return 0
...
>>> X = Truth()
>>> if not X: print('no!')
...
no!



>>> class Truth:
...    def __bool__(self): return True            # 3.0 tries __bool__ first
...    def __len__(self): return 0                # 2.6 tries __len__ first
...
>>> X = Truth()
>>> if X: print('yes!')
...
yes!



>>> class Truth:
...     pass
...
>>> X = Truth()
>>> bool(X)
True



C:\misc> c:\python30\python
>>> class C:
...     def __bool__(self):
...         print('in bool')
...         return False
...
>>> X = C()
>>> bool(X)
in bool
False
>>> if X: print(99)
...
in bool


C:\misc> c:\python26\python
>>> class C:
...     def __bool__(self):      
...         print('in bool')
...         return False
...
>>> X = C()
>>> bool(X)
True
>>> if X: print(99)
...
99


C:\misc> c:\python26\python
>>> class C:
...     def __nonzero__(self):
...         print('in nonzero')
...         return False
...
>>> X = C()
>>> bool(X)
in nonzero
False
>>> if X: print(99)
...
in nonzero



>>> class Life:
...     def __init__(self, name='unknown'):
...         print('Hello', name)
...         self.name = name
...     def __del__(self):
...         print('Goodbye', self.name)
...
>>> brian = Life('Brian')
Hello Brian
>>> brian = 'loretta'
Goodbye Brian



 