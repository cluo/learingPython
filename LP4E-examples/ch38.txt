# NOTE: for the last 2 chapters, I am mostly including working 
# code examples here; to expand pseudocode listings early in 
# the chapters, type their code parts in your editor.



def decorator(cls):                             # On @ decoration
    class Wrapper:
        def __init__(self, *args):              # On instance creation
            self.wrapped = cls(*args)
        def __getattr__(self, name):            # On attribute fetch
            return getattr(self.wrapped, name)
    return Wrapper

@decorator
class C:                             # C = decorator(C)
    def __init__(self, x, y):        # Run by Wrapper.__init__
        self.attr = 'spam'       

x = C(6, 7)                          # Really calls Wrapper(6, 7) 
print(x.attr)                        # Runs Wrapper.__getattr__, prints "spam"




def d1(F): return F
def d2(F): return F
def d3(F): return F

@d1
@d2
@d3
def func():               # func = d1(d2(d3(func)))
    print('spam')

func()                    # Prints "spam"




def d1(F): return lambda: 'X' + F()
def d2(F): return lambda: 'Y' + F()
def d3(F): return lambda: 'Z' + F()

@d1
@d2
@d3
def func():               # func = d1(d2(d3(func)))
    return 'spam'

print(func())             # Prints "XYZspam"




### file: decorator1.py

class tracer:
    def __init__(self, func):             # On @ decoration: save original func
        self.calls = 0
        self.func = func
    def __call__(self, *args):            # On later calls: run original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):           # spam = tracer(spam)
    print(a + b + c)         # Wraps spam in a decorator object




>>> from decorator1 import spam

>>> spam(1, 2, 3)            # Really calls the tracer wrapper object
call 1 to spam
6

>>> spam('a', 'b', 'c')      # Invokes __call__ in class
call 2 to spam
abc

>>> spam.calls               # Number calls in wrapper state information
2
>>> spam
<decorator1.tracer object at 0x02D9A730>




calls = 0
def tracer(func, *args):
    global calls 
    calls += 1
    print('call %s to %s' % (calls, func.__name__))
    func(*args)

def spam(a, b, c):
    print(a, b, c)

>>> spam(1, 2, 3)            # Normal non-traced call: accidental?
1 2 3

>>> tracer(spam, 1, 2, 3)    # Special traced call without decorators
call 1 to spam
1 2 3




class tracer:                                # State via instance attributes
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):          # Same as: spam = tracer(spam)
    print(a + b + c)        # Triggers tracer.__init__

@tracer
def eggs(x, y):             # Same as: eggs = tracer(eggs)
    print(x ** y)           # Wraps eggs in a tracer object

spam(1, 2, 3)               # Really calls tracer instance: runs tracer.__call__
spam(a=4, b=5, c=6)         # spam is an instance attribute

eggs(2, 16)                 # Really calls tracer instance, self.func is eggs
eggs(4, y=4)                # self.calls is per-function here (need 3.0 nonlocal)




calls = 0
def tracer(func):                         # State via enclosing scope and global
    def wrapper(*args, **kwargs):         # Instead of class attributes
        global calls                      # calls is global, not per-function
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):        # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):           # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)             # Really calls wrapper, bound to func        
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, bound to eggs
eggs(4, y=4)              # Global calls is not per-function here!




def tracer(func):                        # State via enclosing scope and nonlocal
    calls = 0                            # Instead of class attrs or global
    def wrapper(*args, **kwargs):        # calls is per-function, not global
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):        # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):           # Same as: eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)             # Really calls wrapper, bound to func        
spam(a=4, b=5, c=6)       # wrapper calls spam

eggs(2, 16)               # Really calls wrapper, bound to eggs
eggs(4, y=4)              # Nonlocal calls _is_ not per-function here




def tracer(func):                        # State via enclosing scope and func attr
    def wrapper(*args, **kwargs):        # calls is per-function, not global
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper




class tracer:
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)


@tracer
def spam(a, b, c):                           # spam = tracer(spam)
    print(a + b + c)                         # Triggers tracer.__init__

spam(1, 2, 3)                                # Runs tracer.__call__        
spam(a=4, b=5, c=6)                          # spam is an instance attribute

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @tracer
    def giveRaise(self, percent):            # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)

    @tracer
    def lastName(self):                      # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)             # tracer remembers method funcs
bob.giveRaise(.25)                           # Runs tracer.__call__(???, .25)
print(bob.lastName())                        # Runs tracer.__call__(???)




# A decorator for both functions and methods

def tracer(func):                        # Use function, not class with __call__
    calls = 0                            # Else "self" is decorator instance only!
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall


# Applies to simple functions

@tracer
def spam(a, b, c):                       # spam = tracer(spam)
    print(a + b + c)                     # onCall remembers spam

spam(1, 2, 3)                            # Runs onCall(1, 2, 3) 
spam(a=4, b=5, c=6)


# Applies to class method functions too!

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @tracer
    def giveRaise(self, percent):        # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)      # onCall remembers giveRaise

    @tracer
    def lastName(self):                  # lastName = tracer(lastName)
        return self.name.split()[-1]

print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                       # Runs onCall(sue, .10)
print(sue.pay)
print(bob.lastName(), sue.lastName())    # Runs onCall(bob), lastName in scopes




class Descriptor(object):
    def __get__(self, instance, owner): ...

class Subject:
    attr = Descriptor()

X = Subject()
X.attr         # Roughly runs Descriptor.__get__(Subject.attr, X, Subject)




class tracer(object):
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):      # On method attribute fetch
        return wrapper(self, instance)

class wrapper:
    def __init__(self, desc, subj):          # Save both instances
        self.desc = desc                     # Route calls back to  decr
        self.subj = subj
    def __call__(self, *args, **kwargs): 
        return self.desc(self.subj, *args, **kwargs)  # Runs tracer.__call__

@tracer
def spam(a, b, c):                           # spam = tracer(spam)
    ...same as prior...                      # Uses __call__ only

class Person:
    @tracer
    def giveRaise(self, percent):            # giveRaise = tracer(giverRaise)
        ...same as prior...                  # Makes giveRaise a descriptor




class tracer(object):
    def __init__(self, func):                # On @ decorator
        self.calls = 0                       # Save func for later call
        self.func  = func
    def __call__(self, *args, **kwargs):     # On call to original func
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):                # On method fetch
        def wrapper(*args, **kwargs):                  # Retain both inst
            return self(instance, *args, **kwargs)     # Runs __call__
        return wrapper




import time

class timer:
    def __init__(self, func):
        self.func    = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start   = time.clock()
        result  = self.func(*args, **kargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return map((lambda x: x * 2), range(N))

result = listcomp(5)                # Time for this call, all calls, return value
listcomp(50000)
listcomp(500000)
listcomp(1000000)   
print(result)
print('allTime = %s' % listcomp.alltime)      # Total time for all listcomp calls

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime)       # Total time for all mapcall calls

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))




...
import sys

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

if sys.version_info[0] == 2:
    @timer
    def mapcall(N):
        return map((lambda x: x * 2), range(N))
else:
    @timer
    def mapcall(N):
        return list(map((lambda x: x * 2), range(N)))
    ...




def timer(label=''):
    def decorator(func):
        def onCall(*args):          # args passed to function
            ...                     # func retained in enclsing scope
            print(label, ...        # label retained in enclosing scope
        return onCall
    return decorator                # Returns that actual decorator

@timer('==>')                       # Like listcomp = timer('==>')(listcomp) 
def listcomp(N): ...                # listcomp is rebound to decorator

listcomp(...)                       # Really calls decorator




### file: mytools.py

import time

def timer(label='', trace=True):                  # On decorator args: retain args
    class Timer:
        def __init__(self, func):                 # On @: retain decorated func
            self.func    = func
            self.alltime = 0
        def __call__(self, *args, **kargs):       # On calls: call original
            start   = time.clock()
            result  = self.func(*args, **kargs)
            elapsed = time.clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer




## file: testseqs.py

from mytools import timer

@timer(label='[CCC]==>')
def listcomp(N):                           # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]       # listcomp(...) triggers Timer.__call__

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return map((lambda x: x * 2), range(N))

for func in (listcomp, mapcall):
    print('')
    result = func(5)        # Time for this call, all calls, return value
    func(50000)
    func(500000)
    func(1000000)
    print(result)  
    print('allTime = %s' % func.alltime)   # Total time for all calls

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))




>>> from mytools import timer
>>> @timer(trace=False)                    # No tracing, collect total time
... def listcomp(N):
...     return [x * 2 for x in range(N)]
...
>>> x = listcomp(5000)
>>> x = listcomp(5000)
>>> x = listcomp(5000)
>>> listcomp
<mytools.Timer instance at 0x025C77B0>
>>> listcomp.alltime
0.0051938863738243413

>>> @timer(trace=True, label='\t=>')       # Turn on tracing
... def listcomp(N):
...     return [x * 2 for x in range(N)]
...
>>> x = listcomp(5000)
        => listcomp: 0.00155, 0.00155
>>> x = listcomp(5000)
        => listcomp: 0.00156, 0.00311
>>> x = listcomp(5000)
        => listcomp: 0.00174, 0.00486
>>> listcomp.alltime
0.0048562736325408196




instances = {}
def getInstance(aClass, *args):                 # Manage global table
    if aClass not in instances:                 # Add **kargs for keywords
        instances[aClass] = aClass(*args)       # One dict entry per class
    return instances[aClass]

def singleton(aClass):                          # On @ decoration
    def onCall(*args):                          # On instance creation
        return getInstance(aClass, *args)
    return onCall




@singleton                                      # Person = singleton(Person)
class Person:                                   # Rebinds Person to onCall
     def __init__(self, name, hours, rate):     # onCall remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate
     def pay(self):
        return self.hours * self.rate

@singleton                                      # Spam = singleton(Spam)
class Spam:                                     # Rebinds Spam to onCall
    def __init__(self, val):                    # onCall remembers Spam
        self.attr = val

bob = Person('Bob', 40, 10)                     # Really calls onCall
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)                     # Same, single object
print(sue.name, sue.pay())

X = Spam(42)                                    # One Person, one Spam
Y = Spam(99)
print(X.attr, Y.attr)




def singleton(aClass):                          # On @ decoration
    instance = None
    def onCall(*args):                          # On instance creation
        nonlocal instance                       # 3.0 and later nonlocal
        if instance == None:
            instance = aClass(*args)            # One scope per class 
        return instance
    return onCall




class singleton: 
    def __init__(self, aClass):                 # On @ decoration
        self.aClass = aClass
        self.instance = None
    def __call__(self, *args):                  # On instance creation
        if self.instance == None:
            self.instance = self.aClass(*args)  # One instance per class 
        return self.instance




class Wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object
    def __getattr__(self, attrname):
        print('Trace:', attrname)                # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch

>>> x = Wrapper([1,2,3])                         # Wrap a list
>>> x.append(4)                                  # Delegate to list method
Trace: append
>>> x.wrapped                                    # Print my member
[1, 2, 3, 4]

>>> x = Wrapper({"a": 1, "b": 2})                # Wrap a dictionary
>>> list(x.keys())                               # Delegate to dictionary method
Trace: keys                                      # Use list() in 3.0
['a', 'b']




def Tracer(aClass):                                   # On @decorator
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)     # Use enclosing scope name 
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)               # Catches all but own attrs
            self.fetches += 1 
            return getattr(self.wrapped, attrname)    # Delegate to wrapped obj
    return Wrapper

@Tracer                   
class Spam:                                    # Spam = Tracer(Spam)
    def display(self):                         # Spam is rebound to Wrapper
        print('Spam!' * 8)

@Tracer
class Person:                                  # Person = Tracer(Person)
    def __init__(self, name, hours, rate):     # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                       
    def pay(self):                             # Accesses outside class traced
        return self.hours * self.rate          # In-method accesses not traced

food = Spam()                                  # Triggers Wrapper()
food.display()                                 # Triggers __getattr__
print([food.fetches])

bob = Person('Bob', 40, 50)                    # bob is really a Wrapper
print(bob.name)                                # Wrapper embeds a Person
print(bob.pay())

print('')
sue = Person('Sue', rate=100, hours=60)        # sue is a different Wrapper
print(sue.name)                                # with a different Person
print(sue.pay())

print(bob.name)                                # bob has different state
print(bob.pay())
print([bob.fetches, sue.fetches])              # Wrapper attrs not traced




>>> from tracer import Tracer     # Decorator moved to a module file

>>> @Tracer
... class MyList(list): pass      # MyList = Tracer(MyList)

>>> x = MyList([1, 2, 3])         # Triggers Wrapper()
>>> x.append(4)                   # Triggers __getattr__, append
Trace: append
>>> x.wrapped
[1, 2, 3, 4]

>>> WrapList = Tracer(list)       # Or perform decoration manually 
>>> x = WrapList([4, 5, 6])       # Else subclass statement required
>>> x.append(7)
Trace: append
>>> x.wrapped
[4, 5, 6, 7]




@Tracer                                          # Decorator approach
class Person: ...
bob = Person('Bob', 40, 50)                   
sue = Person('Sue', rate=100, hours=60)

class Person: ...                                # Non-decorator approach
bob = Wrapper(Person('Bob', 40, 50))
sue = Wrapper(Person('Sue', rate=100, hours=60))




class Tracer:
    def __init__(self, aClass):               # On @decorator
        self.aClass = aClass                  # Use instance attribute
    def __call__(self, *args):                # On instance creation
        self.wrapped = self.aClass(*args)     # ONE (LAST) INSTANCE PER CLASS!
        return self
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

@Tracer                                       # Triggers __init__
class Spam:                                   # Like: Spam = Tracer(Spam)
    def display(self):
        print('Spam!' * 8)

...
food = Spam()                                 # Triggers __call__
food.display()                                # Triggers __getattr__




@Tracer
class Person:                                 # Person = Tracer(Person)
    def __init__(self, name):                 # Wrapper bound to Person
        self.name = name

bob = Person('Bob')                           # bob is really a Wrapper
print(bob.name)                               # Wrapper embeds a Person
Sue = Person('Sue')
print(sue.name)                               # sue overwrites bob
print(bob.name)                               # OOPS: now bob's name is 'Sue'!




class Spam:                                   # Non-decorator version 
    ...                                       # Any class will do
food = Wrapper(Spam())                        # Special creation syntax

@Tracer
class Spam:                                   # Decorator version
    ...                                       # Requires @ syntax at class
food = Spam()                                 # Normal creation syntax




instances = {}
def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]

bob = getInstance(Person, 'Bob', 40, 10)    # Versus: bob = Person('Bob', 40, 10)




instances = {}
def getInstance(object):
    aClass = object.__class__
    if aClass not in instances:
        instances[aClass] = object
    return instances[aClass]

bob = getInstance(Person('Bob', 40, 10))    # Versus: bob = Person('Bob', 40, 10)




def func(x, y):                   # Nondecorator version                      
    ...                           # def tracer(func, args): ... func(*args)
result = tracer(func, (1, 2))     # Special call syntax

@tracer                       
def func(x, y):                   # Decorator version
    ...                           # Rebinds name: func = tracer(func)
result = func(1, 2)               # Normal call syntax




# Registering decorated objects to an API

registry = {}
def register(obj):                          # Both class and func decorator
    registry[obj.__name__] = obj            # Add to registry
    return obj                              # Return obj itself, not a wrapper

@register
def spam(x):
    return(x ** 2)                          # spam = register(spam)

@register
def ham(x):
    return(x ** 3)  

@register
class Eggs:                                 # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)

print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))

print('\nManual calls:')
print(spam(2))                              # Invoke objects manually
print(ham(2))                               # Later calls not intercepted
X = Eggs(2)
print(X)

print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](3))    # Invoke from registry




# Augmenting decorated objects directly

>>> def decorate(func):
...     func.marked = True          # Assign function attribute for later use 
...     return func
...
>>> @decorate
... def spam(a, b):
...     return a + b
...
>>> spam.marked
True

>>> def annotate(text):             # Same, but value is decorator argument
...     def decorate(func):
...         func.label = text
...         return func
...     return decorate
...
>>> @annotate('spam data')
... def spam(a, b):                 # spam = annotate(...)(spam)
...     return a + b
...
>>> spam(1, 2), spam.label
(3, 'spam data')





"""
Privacy for attributes fetched from class instances.
See self-test code at end of file for a usage example.
Decorator same as: Doubler = Private('data', 'size')(Doubler).
Private returns onDecorator, onDecorator returns onInstance,
and each onInstance instance embeds a Doubler instance.
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):                          # privates in enclosing scope
    def onDecorator(aClass):                     # aClass in enclosing scope
        class onInstance:                        # wrapped in instance attribute
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):         # My attrs don't call getattr
                trace('get:', attr)              # Others assumed in wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)
            def __setattr__(self, attr, value):             # Outside accesses
                trace('set:', attr, value)                  # Others run normally
                if attr == 'wrapped':                       # Allow my attrs
                    self.__dict__[attr] = value             # Avoid looping
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)      # Wrapped obj attrs
        return onInstance                                   # Or use __dict__
    return onDecorator


if __name__ == '__main__':
    traceMe = True
    
    @Private('data', 'size')                   # Doubler = Private(..)(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label                 # Accesses inside the subject class
            self.data  = start                 # Not intercepted: run normally
        def size(self):
            return len(self.data)              # Methods run with no checking
        def double(self):                      # Because privacy not inherited
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

    X = Doubler('X is', [1, 2, 3])
    Y = Doubler('Y is', [-10, -20, -30])

    # The followng all succeed
    print(X.label)                             # Accesses outside subject class
    X.display(); X.double(); X.display()       # Intercepted: validated, delegated
    print(Y.label)
    Y.display(); Y.double()
    Y.label = 'Spam'
    Y.display()

    # The following all fail properly
    """
    print(X.size())          # prints "TypeError: private attribute fetch: size"
    print(X.data)
    X.data = [1, 1, 1]
    X.size = lambda S: 0
    print(Y.data)
    print(Y.size())
    """




### file: access.py

"""
Class decorator with Private and Public attribute declarations.
Controls access to attributes stored on an instance, or inherited
by it from its classes. Private declares attribute names that 
cannot be fetched or assigned outside the decorated class, and 
Public declares all the names that can. Caveat: this works in
3.0 for normally named attributes only: __X__ operator overloading
methods implicitly run for built-in operations do not trigger 
either __getattr__ or __getattribute__ in new-style classes.
Add __X__ methods here to intercept and delegate built-ins.
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)
            def __getattr__(self, attr):
                trace('get:', attr)
                if failIf(attr):
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.__wrapped, attr)
            def __setattr__(self, attr, value):
                trace('set:', attr, value)
                if attr == '_onInstance__wrapped':
                    self.__dict__[attr] = value
                elif failIf(attr):
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.__wrapped, attr, value)
        return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))




>>> from access import Private, Public

>>> @Private('age')                             # Person = Private('age')(Person)
... class Person:                               # Person = onInstance with state
...     def __init__(self, name, age):
...         self.name = name
...         self.age  = age                     # Inside accesses run normally
...
>>> X = Person('Bob', 40)
>>> X.name                                      # Outside accesses validated
'Bob'
>>> X.name = 'Sue'
>>> X.name
'Sue'
>>> X.age
TypeError: private attribute fetch: age
>>> X.age = 'Tom'
TypeError: private attribute change: age

>>> @Public('name')
... class Person:
...     def __init__(self, name, age):
...         self.name = name
...         self.age  = age
...
>>> X = Person('bob', 40)                       # X is an onInstance
>>> X.name                                      # onInstance embeds Person
'bob'
>>> X.name = 'Sue'
>>> X.name
'Sue'
>>> X.age
TypeError: private attribute fetch: age
>>> X.age = 'Tom'
TypeError: private attribute change: age




C:\misc> c:\python26\python
>>> from access import Private
>>> @Private('age')
... class Person:
...     def __init__(self):
...         self.age = 42
...     def __str__(self):
...         return 'Person: ' + str(self.age)
...     def __add__(self, yrs):
...         self.age += yrs
...
>>> X = Person()
>>> X.age                                   # Name validations fail correctly
TypeError: private attribute fetch: age
>>> print(X)                                # __getattr__ => runs Person.__str__
Person: 42
>>> X + 10                                  # __getattr__ => runs Person.__add__
>>> print(X)                                # __getattr__ => runs Person.__str__
Person: 52



C:\misc> c:\python30\python
>>> from access import Private
>>> @Private('age')
... class Person:
...     def __init__(self):
...         self.age = 42
...     def __str__(self):
...         return 'Person: ' + str(self.age)
...     def __add__(self, yrs):
...         self.age += yrs
...
>>> X = Person()                            # Name validations still work
>>> X.age                                   # But 3.0 fails to delegate built-ins!
TypeError: private attribute fetch: age
>>> print(X)
<access.onInstance object at 0x025E0790>
>>> X + 10
TypeError: unsupported operand type(s) for +: 'onInstance' and 'int'
>>> print(X)
<access.onInstance object at 0x025E0790>




def accessControl(failIf):
    def onDecorator(aClass):
        class onInstance:
            def __init__(self, *args, **kargs):
                self.__wrapped = aClass(*args, **kargs)

            # Intercept and delegate operator overloading methods
            def __str__(self):
                return str(self.__wrapped)
            def __add__(self, other):
                return self.__wrapped + other
            def __getitem__(self, index):
                return self.__wrapped[index]         # If needed
            def __call__(self, *args, **kargs):
                return self.__wrapped(*arg, *kargs)  # If needed
            ...plus any others needed...

            # Intercept and delegate named attributes
            def __getattr__(self, attr):
                ...
            def __setattr__(self, attr, value):
                ...
        return onInstance
    return onDecorator




# trace support as before

def accessControl(failIf):
    def onDecorator(aClass):
        def getattributes(self, attr):
            trace('get:', attr)
            if failIf(attr):
                raise TypeError('private attribute fetch: ' + attr)
            else:
                return object.__getattribute__(self, attr)
        aClass.__getattribute__ = getattributes
        return aClass
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))




class Person:
    def giveRaise(self, percent):                # Validate with inline code
        if percent < 0.0 or percent > 1.0:
            raise TypeError, 'percent invalid'
        self.pay = int(self.pay * (1 + percent))

class Person:                                    # Validate with asserts
    def giveRaise(self, percent):            
        assert percent >= 0.0 and percent <= 1.0, 'percent invalid'
        self.pay = int(self.pay * (1 + percent))



class Person:
    @rangetest(percent=(0.0, 1.0))               # Use decorator to validate
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))




### file: devtools.py

def rangetest(*argchecks):                  # Validate positional arg ranges
    def onDecorator(func):
        if not __debug__:                   # True if "python -O main.py args..."
            return func                     # No-op: call original directly
        else:                               # Else wrapper while debugging
            def onCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument %s not in %s..%s' % (ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)
            return onCall
    return onDecorator




### File: devtools_test.py

from devtools import rangetest
print(__debug__)                             # False if "python –O main.py"

@rangetest((1, 0, 120))                      # persinfo = rangetest(..)(persinfo)
def persinfo(name, age):                     # age must be in 0..120
    print('%s is %s years old' % (name, age))

@rangetest([0, 1, 12], [1, 1, 31], [2, 0, 2009])
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

class Person:  
    def __init__(self, name, job, pay):
        self.job  = job
        self.pay  = pay
                                             
    @rangetest([1, 0.0, 1.0])                # giveRaise = rangetest(..)(giveRaise)
    def giveRaise(self, percent):            # Arg 0 is the self instance here
        self.pay = int(self.pay * (1 + percent))

# Comment lines raise TypeError unless "python -O" used on shell command line

persinfo('Bob Smith', 45)                    # Really runs onCall(..) with state 
#persinfo('Bob Smith', 200)                  # Or person if -O cmd line argument

birthday(5, 31, 1963)
#birthday(5, 32, 1963)

sue = Person('Sue Jones', 'dev', 100000)
sue.giveRaise(.10)                           # Really runs onCall(self, .10)
print(sue.pay)                               # Or giveRaise(self, .10) if -O
#sue.giveRaise(1.10)
#print(sue.pay)




C:\misc> C:\python30\python devtools_test.py

C:\misc> C:\python30\python -O devtools_test.py




### file: devtools.py (new)

"""
File devtools.py: function decorator that performs range-test 
validation for passed arguments. Arguments are specified by 
keyword to the decorator. In the actual call, arguments may 
be passed by position or keyword, and defaults may be omitted.
See devtools_test.py for example use cases.
"""

trace = True

def rangetest(**argchecks):                 # Validate ranges for both+defaults
    def onDecorator(func):                  # onCall remembers func and argchecks
        if not __debug__:                   # True if "python -O main.py args..."
            return func                     # Wrap if debugging; else use original
        else:
            import sys
            code     = func.__code__
            allargs  = code.co_varnames[:code.co_argcount]
            funcname = func.__name__
            
            def onCall(*pargs, **kargs):
                # All pargs match first N expected args by position
                # The rest must be in kargs or be omitted defaults
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]

                for (argname, (low, high)) in argchecks.items():
                    # For all args to be checked
                    if argname in kargs:
                        # Was passed by name
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)

                    elif argname in positionals:
                        # Was passed by position
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0} argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    else:
                        # Assume not passed: default
                        if trace:
                            print('Argument "{0}" defaulted'.format(argname))

                return func(*pargs, **kargs)    # OK: run original call
            return onCall
    return onDecorator




# File devtools_test.py
# Comment lines raise TypeError unless "python -O" used on shell command line
from devtools import rangetest


# Test functions, positional and keyword

@rangetest(age=(0, 120))                  # persinfo = rangetest(..)(persinfo)
def persinfo(name, age):
    print('%s is %s years old' % (name, age))

@rangetest(M=(1, 12), D=(1, 31), Y=(0, 2009))
def birthday(M, D, Y):
    print('birthday = {0}/{1}/{2}'.format(M, D, Y))

persinfo('Bob', 40)
persinfo(age=40, name='Bob')
birthday(5, D=1, Y=1963)
#persinfo('Bob', 150)
#persinfo(age=150, name='Bob')
#birthday(5, D=40, Y=1963)


# Test methods, positional and keyword

class Person:
    def __init__(self, name, job, pay):
        self.job  = job
        self.pay  = pay
                                          # giveRaise = rangetest(..)(giveRaise)
    @rangetest(percent=(0.0, 1.0))        # percent passed by name or position
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

bob = Person('Bob Smith', 'dev', 100000)
sue = Person('Sue Jones', 'dev', 100000)
bob.giveRaise(.10)
sue.giveRaise(percent=.20)
print(bob.pay, sue.pay)
#bob.giveRaise(1.10)
#bob.giveRaise(percent=1.20)


# Test omitted defaults: skipped

@rangetest(a=(1, 10), b=(1, 10), c=(1, 10), d=(1, 10))
def omitargs(a, b=7, c=8, d=9):
    print(a, b, c, d)
                                          
omitargs(1, 2, 3, 4) 
omitargs(1, 2, 3)
omitargs(1, 2, 3, d=4)
omitargs(1, d=4)
omitargs(d=4, a=1)
omitargs(1, b=2, d=4)
omitargs(d=8, c=7, a=1)

#omitargs(1, 2, 3, 11)        # Bad d
#omitargs(1, 2, 11)           # Bad c
#omitargs(1, 2, 3, d=11)      # Bad d
#omitargs(11, d=4)            # Bad a
#omitargs(d=4, a=11)          # Bad a
#omitargs(1, b=11, d=4)       # Bad b
#omitargs(d=8, c=7, a=11)     # Bad a




C:\misc> C:\python30\python devtools_test.py




# In Python 3.0 (and 2.6 for compatibility):
>>> def func(a, b, c, d):
...     x = 1
...     y = 2
...
>>> code = func.__code__                     # Code object of function object
>>> code.co_nlocals
6
>>> code.co_varnames                         # All local var names
('a', 'b', 'c', 'd', 'x', 'y')
>>> code.co_varnames[:code.co_argcount]      # First N locals are expected args
('a', 'b', 'c', 'd')

>>> import sys                               # For backward compatibility
>>> sys.version_info                         # [0] is major release number
(3, 0, 0, 'final', 0)
>>> code = func.__code__ if sys.version_info[0] == 3 else func.func_code



omitargs()
omitargs(d=8, c=7, b=6)




@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a, b, c):                         # func = rangetest(..)(func)
    print(a + b + c)



@rangetest
def func(a:(1, 5), b, c:(0.0, 1.0)):
    print(a + b + c)




# Using decorator arguments

def rangetest(**argchecks):
    def onDecorator(func):
        def onCall(*pargs, **kargs):
            print(argchecks)
            for check in argchecks: pass     # Add validation code here
            return func(*pargs, **kargs)
        return onCall
    return onDecorator

@rangetest(a=(1, 5), c=(0.0, 1.0))
def func(a, b, c):                           # func = rangetest(..)(func)
    print(a + b + c)

func(1, 2, c=3)                              # Runs onCall, argchecks in scope


# Using function annotations

def rangetest(func):
    def onCall(*pargs, **kargs):
        argchecks = func.__annotations__
        print(argchecks)
        for check in argchecks: pass         # Add validation code here
        return func(*pargs, **kargs)
    return onCall

@rangetest
def func(a:(1, 5), b, c:(0.0, 1.0)):         # func = rangetest(func)
    print(a + b + c)

func(1, 2, c=3)                              # Runs onCall, annotations on func




def typetest(**argchecks):
    def onDecorator(func):
           ....
           def onCall(*pargs, **kargs):
                positionals = list(allargs)[:len(pargs)]
                for (argname, type) in argchecks.items():
                    if argname in kargs:
                        if not isinstance(kargs[argname], type):
                            ...
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        position = positionals.index(argname)
                        if not isinstance(pargs[position], type):
                            ...
                            raise TypeError(errmsg)
                    else:
                        # assume not passed: default
                return func(*pargs, **kargs)
            return onCall
    return onDecorator

@typetest(a=int, c=float)
def func(a, b, c, d):                    # func = typetest(...)(func)
    ...

func(1, 2, 3.0, 4)                       # Okay
func('spam', 2, 99, 4)                   # Triggers exception correctly




@typetest
def func(a: int, b, c: float, d):        # func = typetest(func)
    ...                                  # Gasp!...




### quiz answers code



### question 1



import time

def timer(label='', trace=True):             # On decorator args: retain args
    def onDecorator(func):                   # On @: retain decorated func
        def onCall(*args, **kargs):          # On calls: call original
            start   = time.clock()           # State is scopes + func attr
            result  = func(*args, **kargs)
            elapsed = time.clock() - start
            onCall.alltime += elapsed
            if trace:
                format = '%s%s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, onCall.alltime)
                print(format % values)
            return result
        onCall.alltime = 0
        return onCall
    return onDecorator

# Test on functions

@timer(trace=True, label='[CCC]==>')
def listcomp(N):                             # Like listcomp = timer(...)(listcomp)
    return [x * 2 for x in range(N)]         # listcomp(...) triggers onCall     

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))   # list for 3.0 views

for func in (listcomp, mapcall):
    result = func(5)                  # Time for this call, all calls, return value
    func(5000000)
    print(result)  
    print('allTime = %s\n' % func.alltime)   # Total time for all calls

# Test on methods

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @timer()
    def giveRaise(self, percent):            # giveRaise = timer()(giverRaise)
        self.pay *= (1.0 + percent)          # tracer remembers giveRaise

    @timer(label='**')
    def lastName(self):                      # lastName = timer(...)(lastName)
        return self.name.split()[-1]         # alltime per class, not instance

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)                           # runs onCall(sue, .10)
print(bob.pay, sue.pay)
print(bob.lastName(), sue.lastName())        # runs onCall(bob), remembers lastName
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))

# Expected output

[CCC]==>listcomp: 0.00002, 0.00002
[CCC]==>listcomp: 1.19636, 1.19638
[0, 2, 4, 6, 8]
allTime = 1.19637775192

[MMM]==>mapcall: 0.00002, 0.00002
[MMM]==>mapcall: 2.29260, 2.29262
[0, 2, 4, 6, 8]
allTime = 2.2926232943

giveRaise: 0.00001, 0.00001
giveRaise: 0.00001, 0.00002
55000.0 120000.0
**lastName: 0.00001, 0.00001
**lastName: 0.00001, 0.00002
Smith Jones
0.00002 0.00002




### question 2


traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
    def onDecorator(aClass):
        if not __debug__:
            return aClass
        else:
            class onInstance:
                def __init__(self, *args, **kargs):
                    self.__wrapped = aClass(*args, **kargs)
                def __getattr__(self, attr):
                    trace('get:', attr)
                    if failIf(attr):
                        raise TypeError('private attribute fetch: ' + attr)
                    else:
                        return getattr(self.__wrapped, attr)
                def __setattr__(self, attr, value):
                    trace('set:', attr, value)
                    if attr == '_onInstance__wrapped':
                        self.__dict__[attr] = value
                    elif failIf(attr):
                        raise TypeError('private attribute change: ' + attr)
                    else:
                        setattr(self.__wrapped, attr, value)
            return onInstance
    return onDecorator

def Private(*attributes):
    return accessControl(failIf=(lambda attr: attr in attributes))

def Public(*attributes):
    return accessControl(failIf=(lambda attr: attr not in attributes))


# Test code: split me off to another file to reuse decorator

@Private('age')                             # Person = Private('age')(Person)
class Person:                               # Person = onInstance with state
    def __init__(self, name, age):
        self.name = name
        self.age  = age                     # Inside accesses run normally

X = Person('Bob', 40)
print(X.name)                               # Outside accesses validated
X.name = 'Sue'
print(X.name)
#print(X.age)    # FAILS unles "python -O"
#X.age = 999     # ditto
#print(X.age)    # ditto

@Public('name')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

X = Person('bob', 40)                       # X is an onInstance
print(X.name)                               # onInstance embeds Person
X.name = 'Sue'
print(X.name)
#print(X.age)    # FAILS unless "python –O main.py"
#X.age = 999     # ditto
#print(X.age)    # ditto



