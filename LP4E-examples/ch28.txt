>>> class SharedData:
...     spam = 42          # Generates a class data attribute
...
>>> x = SharedData()       # Make two instances
>>> y = SharedData()
>>> x.spam, y.spam         # They inherit and share 'spam'
(42, 42)



>>> SharedData.spam = 99
>>> x.spam, y.spam, SharedData.spam
(99, 99, 99)



>>> x.spam = 88
>>> x.spam, y.spam, SharedData.spam
(88, 99, 99)



class MixedNames:                            # Define class
    data = 'spam'                            # Assign class attr
    def __init__(self, value):               # Assign method name
        self.data = value                    # Assign instance attr
    def display(self):
        print(self.data, MixedNames.data)    # Instance attr, class attr



>>> x = MixedNames(1)          # Make two instance objects
>>> y = MixedNames(2)          # Each has its own data
>>> x.display(); y.display()   # self.data differs, MixedNames.data is the same
1 spam
2 spam



class NextClass:                            # Define class
    def printer(self, text):                # Define method
        self.message = text                 # Change instance
        print(self.message)                 # Access instance



>>> x = NextClass()                         # Make instance

>>> x.printer('instance call')              # Call its method
instance call

>>> x.message                               # Instance changed
'instance call'



>>> NextClass.printer(x, 'class call')      # Direct class call
class call

>>> x.message                               # Instance changed again
'class call'



>>> NextClass.printer('bad call')
TypeError: unbound method printer() must be called with NextClass instance...



class Super:
    def __init__(self, x):
        ...default code...

class Sub(Super):
    def __init__(self, x, y):
        Super.__init__(self, x)             # Run superclass __init__
        ...custom code...                   # Do my init actions

I = Sub(1, 2)



>>> class Super:
...     def method(self):
...         print('in Super.method')
...
>>> class Sub(Super):
...     def method(self):                    # Override method
...         print('starting Sub.method')     # Add actions here
...         Super.method(self)               # Run default action
...         print('ending Sub.method')
...



>>> x = Super()                              # Make a Super instance
>>> x.method()                               # Runs Super.method
in Super.method

>>> x = Sub()                                # Make a Sub instance
>>> x.method()                               # Runs Sub.method, calls Super.method
starting Sub.method
in Super.method
ending Sub.method



### file: specialize.py

class Super:
    def method(self):
        print('in Super.method')           # Default behavior
    def delegate(self):
        self.action()                      # Expected to be defined

class Inheritor(Super):                    # Inherit method verbatim
    pass

class Replacer(Super):                     # Replace method completely
    def method(self):
        print('in Replacer.method')

class Extender(Super):                     # Extend method behavior
    def method(self):
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')

class Provider(Super):                     # Fill in a required method
    def action(self):
        print('in Provider.action')

if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()



class Super:
    def delegate(self):
        self.action()
    def action(self):
        assert False, 'action must be defined!'         # If this version called

>>> X = Super()
>>> X.delegate()
AssertionError: action must be defined!



class Super:
    def delegate(self):
        self.action()
    def action(self):
        raise NotImplementedError('action must be defined!')

>>> X = Super()
>>> X.delegate()
NotImplementedError: action must be defined!



>>> class Sub(Super): pass
...
>>> X = Sub()
>>> X.delegate()
NotImplementedError: action must be defined!

>>> class Sub(Super):
...     def action(self): print('spam')
...
>>> X = Sub()
>>> X.delegate()
spam



from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    @abstractmethod
    def method(self, ...):
        pass



class Super:
    __metaclass__ = ABCMeta
    @abstractmethod
    def method(self, ...): 
        pass



>>> from abc import ABCMeta, abstractmethod
>>>
>>> class Super(metaclass=ABCMeta):
...     def delegate(self):
...         self.action()
...     @abstractmethod
...     def action(self):
...         pass
...
>>> X = Super()
TypeError: Can't instantiate abstract class Super with abstract methods action

>>> class Sub(Super): pass
...
>>> X = Sub()
TypeError: Can't instantiate abstract class Sub with abstract methods action

>>> class Sub(Super):
...     def action(self): print('spam')
...
>>> X = Sub()
>>> X.delegate()
spam



### File: manynames.py

X = 11                       # Global (module) name/attribute (X, or manynames.X)

def f():
    print(X)                 # Access global X (11)

def g():
    X = 22                   # Local (function) variable (X, hides module X)
    print(X)

class C:
    X = 33                   # Class attribute (C.X)
    def m(self):
        X = 44               # Local variable in method (X)
        self.X = 55          # Instance attribute (instance.X)


# manynames.py, continued

if __name__ == '__main__':
    print(X)                 # 11: module (a.k.a. manynames.X outside file)
    f()                      # 11: global
    g()                      # 22: local
    print(X)                 # 11: module name unchanged

    obj = C()                # Make instance
    print(obj.X)             # 33: class name inherited by instance

    obj.m()                  # Attach attribute name X to instance now
    print(obj.X)             # 55: instance
    print(C.X)               # 33: class (a.k.a. obj.X if no X in instance)

    #print(C.m.X)            # FAILS: only visible in method
    #print(g.X)              # FAILS: only visible in function



### File: otherfile.py

import manynames

X = 66
print(X)                     # 66: the global here
print(manynames.X)           # 11: globals become attributes after imports

manynames.f()                # 11: manynames's X, not the one here!
manynames.g()                # 22: local in other file’s function

print(manynames.C.X)         # 33: attribute of class in other module
I = manynames.C()
print(I.X)                   # 33: still from class here
I.m()  
print(I.X)                   # 55: now from instance!



X = 11                       # Global in module

def g1():
    print(X)                 # Reference global in module

def g2():
    global X
    X = 22                   # Change global in module

def h1():
    X = 33                   # Local in function
    def nested():
        print(X)             # Reference local in enclosing scope

def h2():
    X = 33                   # Local in function
    def nested():
        nonlocal X           # Python 3.0 statement
        X = 44               # Change local in enclosing scope



>>> class super:
...     def hello(self):
...         self.data1 = 'spam'
...
>>> class sub(super):
...     def hola(self):
...         self.data2 = 'eggs'
...



>>> X = sub()
>>> X.__dict__                            # Instance namespace dict
{}

>>> X.__class__                           # Class of instance
<class '__main__.sub'>

>>> sub.__bases__                         # Superclasses of class
(<class '__main__.super'>,)

>>> super.__bases__                       # () empty tuple in Python 2.6
(<class 'object'>,)



>>> Y = sub()

>>> X.hello()
>>> X.__dict__
{'data1': 'spam'}

>>> X.hola()
>>> X.__dict__
{'data1': 'spam', 'data2': 'eggs'}

>>> sub.__dict__.keys()
['__module__', '__doc__', 'hola']

>>> super.__dict__.keys()
['__dict__', '__module__', '__weakref__', 'hello', '__doc__']

>>> Y.__dict__
{}



>>> X.data1, X.__dict__['data1']
('spam', 'spam')

>>> X.data3 = 'toast'
>>> X.__dict__
{'data1': 'spam', 'data3': 'toast', 'data2': 'eggs'}

>>> X.__dict__['data3'] = 'ham'
>>> X.data3
'ham'



>>> X.__dict__, Y.__dict__
({'data1': 'spam', 'data3': 'ham', 'data2': 'eggs'}, {})
>>> list(X.__dict__.keys())                                  # Need list() in 3.0
['data1', 'data3', 'data2']

# In Python 2.6:

>>>> dir(X)
['__doc__', '__module__', 'data1', 'data2', 'data3', 'hello', 'hola']
>>> dir(sub)
['__doc__', '__module__', 'hello', 'hola']
>>> dir(super)
['__doc__', '__module__', 'hello']

# In Python 3.0:

>>> dir(X)
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__',
...more omitted...
'data1', 'data2', 'data3', 'hello', 'hola']

>>> dir(sub)
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__',
...more omitted...
'hello', 'hola']

>>> dir(super)
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__',
...more omitted...
'hello'
]



### File: classtree.py

"""
Climb inheritance trees using namespace links,
displaying higher superclasses with indentation
"""

def classtree(cls, indent):
    print('.' * indent + cls.__name__)    # Print class name here
    for supercls in cls.__bases__:        # Recur to all superclasses
        classtree(supercls, indent+3)     # May visit super > once

def instancetree(inst):
    print('Tree of %s' % inst)            # Show instance
    classtree(inst.__class__, 3)          # Climb to its class

def selftest():
    class A:      pass
    class B(A):   pass
    class C(A):   pass
    class D(B,C): pass
    class E:      pass
    class F(D,E): pass
    instancetree(B())
    instancetree(F())

if __name__ == '__main__': selftest()



C:\misc> c:\python30\python
>>> class Emp: pass
...
>>> class Person(Emp): pass
>>> bob = Person()

>>> import classtree
>>> classtree.instancetree(bob)
Tree of <__main__.Person object at 0x028203B0>
...Person
......Emp
.........object



### file: docstr.py

"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__"
    def method(self, arg):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass



>>> import docstr
>>> docstr.__doc__
'I am: docstr.__doc__'

>>> docstr.func.__doc__
'I am: docstr.func.__doc__'

>>> docstr.spam.__doc__
'I am: spam.__doc__ or docstr.spam.__doc__'

>>> docstr.spam.method.__doc__
'I am: spam.method.__doc__ or self.method.__doc__'



>>> help(docstr)
Help on module docstr:

NAME
    docstr - I am: docstr.__doc__

FILE
    c:\misc\docstr.py

CLASSES
    spam

    class spam
     |  I am: spam.__doc__ or docstr.spam.__doc__
     |
     |  Methods defined here:
     |
     |  method(self, arg)
     |      I am: spam.method.__doc__ or self.method.__doc__

FUNCTIONS
    func(args)
        I am: docstr.func.__doc__



