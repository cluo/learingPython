>>> def mysum(L):
...     if not L:
...         return 0
...     else:
...         return L[0] + mysum(L[1:])           # Call myself
	
>>> mysum([1, 2, 3, 4, 5])
15



>>> def mysum(L):
...     print(L)                                 # Trace recursive levels
...     if not L:                                # L shorter at each level
...         return 0
...     else:
...         return L[0] + mysum(L[1:])
...
>>> mysum([1, 2, 3, 4, 5])
[1, 2, 3, 4, 5]
[2, 3, 4, 5]
[3, 4, 5]
[4, 5]
[5]
[]
15



def mysum(L): 
    return 0 if not L else L[0] + mysum(L[1:])           # Use ternary expression

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])  # Any type, assume one

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)    # Use 3.0 ext seq assign



>>> mysum([1])                              # mysum([]) fails in last 2
1
>>> mysum([1, 2, 3, 4, 5])
15
>>> mysum(('s', 'p', 'a', 'm'))             # But various types now work
'spam'
>>> mysum(['spam', 'ham', 'eggs'])
'spamhameggs'



>>> def mysum(L):
...     if not L: return 0
...     return nonempty(L)                  # Call a function that calls me
...
>>> def nonempty(L):
...     return L[0] + mysum(L[1:])          # Indirectly recursive
...
>>> mysum([1.1, 2.2, 3.3, 4.4])
11.0



>>> L = [1, 2, 3, 4, 5]
>>> sum = 0
>>> while L:
...     sum += L[0]
...     L = L[1:]
...
>>> sum
15



>>> L = [1, 2, 3, 4, 5]
>>> sum = 0
>>> for x in L: sum += x
...
>>> sum
15



[1, [2, [3, 4], 5], 6, [7, 8]]                   # Arbitrarily nested sublists



def sumtree(L):
    tot = 0
    for x in L:                                  # For each item at this level
        if not isinstance(x, list):
            tot += x                             # Add numbers directly
        else:
            tot += sumtree(x)                    # Recur for sublists
    return tot

L = [1, [2, [3, 4], 5], 6, [7, 8]]               # Arbitrary nesting
print(sumtree(L))                                # Prints 36


# Pathological cases

print(sumtree([1, [2, [3, [4, [5]]]]]))          # Prints 15 (right-heavy)

print(sumtree([[[[[1], 2], 3], 4], 5]))          # Prints 15 (left-heavy)



>>> def echo(message):                   # Name echo assigned to function object
...     print(message)
...
>>> echo('Direct call')                  # Call object through original name
Direct call

>>> x = echo                             # Now x references the function too
>>> x('Indirect call!')                  # Call object through name by adding ()
Indirect call!



>>> def indirect(func, arg):
...     func(arg)                        # Call the passed-in object by adding ()
...
>>> indirect(echo, 'Argument call!')     # Pass the function to another function
Argument call!



>>> schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]
>>> for (func, arg) in schedule:
...     func(arg)                        # Call functions embedded in containers
...
Spam!
Ham!



>>> def make(label):                     # Make a function but don't call it
...     def echo(message):
...         print(label + ':' + message)
...     return echo
...
>>> F = make('Spam')                     # Label in enclosing scope is retained
>>> F('Ham!')                            # Call the function that make returned
Spam:Ham!
>>> F('Eggs!')
Spam:Eggs!



>>> def func(a):
...     b = 'spam'
...     return b * a
...
>>> func(8)
'spamspamspamspamspamspamspamspam'



>>> func.__name__
'func'
>>> dir(func)
['__annotations__', '__call__', '__class__', '__closure__', '__code__',
...more omitted... 
'__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



>>> func.__code__
<code object func at 0x0257C9B0, file "<stdin>", line 1>

>>> dir(func.__code__)
['__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', 
...more omitted...
'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 
'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab',
'co_name', 'co_names', 'co_nlocals', 'co_stacksize', 'co_varnames']

>>> func.__code__.co_varnames
('a', 'b')
>>> func.__code__.co_argcount
1



>>> func
<function func at 0x0257C738>
>>> func.count = 0
>>> func.count += 1
>>> func.count
1
>>> func.handles = 'Button-Press'
>>> func.handles
'Button-Press'
>>> dir(func)
['__annotations__', '__call__', '__class__', '__closure__', '__code__',
...more omitted...
__str__', '__subclasshook__', 'count', 'handles']



>>> def func(a, b, c):
...     return a + b + c
...
>>> func(1, 2, 3)
6



>>> def func(a: 'spam', b: (1, 10), c: float) -> int:
...     return a + b + c
...
>>> func(1, 2, 3)
6



>>> func.__annotations__
{'a': 'spam', 'c': <class 'float'>, 'b': (1, 10), 'return': <class 'int'>}



>>> def func(a: 'spam', b, c: 99):
...     return a + b + c
...
>>> func(1, 2, 3)
6
>>> func.__annotations__
{'a': 'spam', 'c': 99}

>>> for arg in func.__annotations__:
...    print(arg, '=>', func.__annotations__[arg])
...
a => spam
c => 99



>>> def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
...     return a + b + c
...
>>> func(1, 2, 3)
6
>>> func()                       # 4 + 5 + 6   (all defaults)
15
>>> func(1, c=10)                # 1 + 5 + 10  (keywords work normally)
16
>>> func.__annotations__
{'a': 'spam', 'c': <class 'float'>, 'b': (1, 10), 'return': <class 'int'>}



>>> def func(a:'spam'=4, b:(1,10)=5, c:float=6)->int:
...     return a + b + c
...
>>> func(1, 2)                   # 1 + 2 + 6
9
>>> func.__annotations__
{'a': 'spam', 'c': <class 'float'>, 'b': (1, 10), 'return': <class 'int'>}



>>> def func(x, y, z): return x + y + z
...
>>> func(2, 3, 4)
9



>>> f = lambda x, y, z: x + y + z
>>> f(2, 3, 4)
9



>>> x = (lambda a="fee", b="fie", c="foe": a + b + c)
>>> x("wee")
'weefiefoe'



>>> def knights():
...     title = 'Sir'
...     action = (lambda x: title + ' ' + x)        # Title in enclosing def
...     return action                               # Return a function
...
>>> act = knights()
>>> act('robin')
'Sir robin'



L = [lambda x: x ** 2,               # Inline function definition
     lambda x: x ** 3,
     lambda x: x ** 4]               # A list of 3 callable functions

for f in L:
    print(f(2))                      # Prints 4, 8, 16

print(L[0](3))                       # Prints 9



def f1(x): return x ** 2 
def f2(x): return x ** 3             # Define named functions
def f3(x): return x ** 4

L = [f1, f2, f3]                     # Reference by name

for f in L:
    print(f(2))                      # Prints 4, 8, 16

print(L[0](3))                       # Prints 9



>>> key = 'got'
>>> {'already': (lambda: 2 + 2),
...  'got':     (lambda: 2 * 4),
...  'one':     (lambda: 2 ** 6)}[key]()
8



>>> def f1(): return 2 + 2
...
>>> def f2(): return 2 * 4
...
>>> def f3(): return 2 ** 6
...
>>> key = 'one'
>>> {'already': f1, 'got': f2, 'one': f3}[key]()
64



>>> lower = (lambda x, y: x if x < y else y)
>>> lower('bb', 'aa')
'aa'
>>> lower('aa', 'bb')
'aa'



>>> import sys
>>> showall = lambda x: list(map(sys.stdout.write, x))        # Use list() in 3.0

>>> t = showall(['spam\n', 'toast\n', 'eggs\n'])
spam
toast
eggs

>>> showall = lambda x: [sys.stdout.write(line) for line in x]

>>> t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))
bright
side
of
life



>>> def action(x):
...     return (lambda y: x + y)         # Make and return function, remember x
...
>>> act = action(99)
>>> act
<function <lambda> at 0x00A16A88>
>>> act(2)                               # Call what action returned
101



>>> action = (lambda x: (lambda y: x + y))
>>> act = action(99)
>>> act(3)
102
>>> ((lambda x: (lambda y: x + y))(99))(4)
103



import sys
from tkinter import Button, mainloop     # Tkinter in 2.6
x = Button(
        text ='Press me',
        command=(lambda:sys.stdout.write('Spam\n')))
x.pack()
mainloop()



class MyGui:
    def makewidgets(self):
        Button(command=(lambda: self.onPress("spam")))
    def onPress(self, message):
        ...use message...



>>> counters = [1, 2, 3, 4]
>>>
>>> updated = []
>>> for x in counters:
...     updated.append(x + 10)                 # Add 10 to each item
...
>>> updated
[11, 12, 13, 14]



>>> def inc(x): return x + 10                  # Function to be run
...
>>> list(map(inc, counters))                   # Collect results
[11, 12, 13, 14]



>>> list(map((lambda x: x + 3), counters))     # Function expression
[4, 5, 6, 7]



>>> def mymap(func, seq):
...     res = []
...     for x in seq: res.append(func(x))
...     return res



>>> list(map(inc, [1, 2, 3]))             # Built-in is an iterator
[11, 12, 13]
>>> mymap(inc, [1, 2, 3])                 # Ours builds a list (see generators)
[11, 12, 13]



>>> pow(3, 4)                             # 3**4
81
>>> list(map(pow, [1, 2, 3], [2, 3, 4]))  # 1**2, 2**3, 3**4
[1, 8, 81]



>>> list(range(-5, 5))                                   # An iterator in 3.0
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

>>> list(filter((lambda x: x > 0), range(-5, 5)))        # An iterator in 3.0
[1, 2, 3, 4]



>>> res = []
>>> for x in range(-5, 5):
...     if x > 0:
...         res.append(x)
...
>>> res
[1, 2, 3, 4]



>>> from functools import reduce      # Import in 3.0, not in 2.6

>>> reduce((lambda x, y: x + y), [1, 2, 3, 4])
10
>>> reduce((lambda x, y: x * y), [1, 2, 3, 4])
24



>>> L = [1,2,3,4]
>>> res = L[0]
>>> for x in L[1:]:
...     res = res + x
...
>>> res
10



>>> def myreduce(function, sequence):
...     tally = sequence[0]
...     for next in sequence[1:]:
...         tally = function(tally, next)
...     return tally
...
>>> myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5])
15
>>> myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5])
120



>>> import operator, functools
>>> functools.reduce(operator.add, [2, 4, 6])        # Function-based +
12
>>> functools.reduce((lambda x, y: x + y), [2, 4, 6])
12



