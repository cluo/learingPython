class C:
    def meth(self, x):
        ...
    def meth(self, x, y, z):
        ...



class C:
    def meth(self, *args):
        if len(args) == 1:
            ...
        elif type(arg[0]) == int:
            ...



class C:
    def meth(self, x):
        x.operation()                   # Assume x does the right thing



### file: employees.py

class Employee:
    def __init__(self, name, salary=0):
        self.name   = name
        self.salary = salary
    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)
    def work(self):
        print(self.name, "does stuff")
    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")

if __name__ == "__main__":
    bob = PizzaRobot('bob')       # Make a robot named bob
    print(bob)                    # Run inherited __repr__
    bob.work()                    # Run type-specific action
    bob.giveRaise(0.20)           # Give bob a 20% raise
    print(bob); print()

    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()



C:\python\examples> python employees.py



### file: pizzashop.py

from employees import PizzaRobot, Server

class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)

class Oven:
    def bake(self):
        print("oven bakes")

class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')         # Embed other objects
        self.chef   = PizzaRobot('Bob')     # A robot named bob
        self.oven   = Oven()

    def order(self, name):
        customer = Customer(name)           # Activate other objects
        customer.order(self.server)         # Customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

if __name__ == "__main__":
    scene = PizzaShop()                     # Make the composite
    scene.order('Homer')                    # Simulate Homer's order
    print('...')
    scene.order('Shaggy')                   # Simulate Shaggy's order



C:\python\examples> python pizzashop.py



def processor(reader, converter, writer):
    while 1:
        data = reader.read()
        if not data: break
        data = converter(data)
        writer.write(data)



### file: streams.py

class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
    def process(self):
        while 1:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)
    def converter(self, data):
        assert False, 'converter must be defined'       # Or raise exception



### file: converters.py

from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('spam.txt'), sys.stdout)
    obj.process()



C:\lp4e> type spam.txt
spam
Spam
SPAM!

C:\lp4e> python converters.py
SPAM
SPAM
SPAM!



C:\lp4e> python
>>> import converters
>>> prog = converters.Uppercase(open('spam.txt'), open('spamup.txt', 'w'))
>>> prog.process()

C:\lp4e> type spamup.txt
SPAM
SPAM
SPAM!



C:\lp4e> python
>>> from converters import Uppercase
>>>
>>> class HTMLize:
...      def write(self, line):
...         print('<PRE>%s</PRE>' % line.rstrip())
...
>>> Uppercase(open('spam.txt'), HTMLize()).process()
<PRE>SPAM</PRE>
<PRE>SPAM</PRE>
<PRE>SPAM!</PRE>



import pickle
object = someClass()
file   = open(filename, 'wb')     # Create external file
pickle.dump(object, file)         # Save object in file

import pickle
file   = open(filename, 'rb')
object = pickle.load(file)        # Fetch it back later


import shelve
object = someClass()
dbase  = shelve.open('filename')
dbase['key'] = object             # Save under key

import shelve
dbase  = shelve.open('filename')
object = dbase['key']             # Fetch it back later


>>> from pizzashop import PizzaShop
>>> shop = PizzaShop()
>>> shop.server, shop.chef
(<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>)
>>> import pickle
>>> pickle.dump(shop, open('shopfile.dat', 'wb'))


>>> import pickle
>>> obj = pickle.load(open('shopfile.dat', 'rb'))
>>> obj.server, obj.chef
(<Employee: name=Pat, salary=40000>, <Employee: name=Bob, salary=50000>)
>>> obj.order('Sue')
Sue orders from <Employee: name=Pat, salary=40000>
Bob makes pizza
oven bakes
Sue pays for item to <Employee: name=Pat, salary=40000>



### file: trace.py

class wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object
    def __getattr__(self, attrname):
        print('Trace:', attrname)                # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch



# NOTE: in the following, use list(x.keys()) for Python 3.X 
# (list() was not used in the first printing of the book


>>> from trace import wrapper
>>> x = wrapper([1,2,3])                         # Wrap a list
>>> x.append(4)                                  # Delegate to list method
Trace: append
>>> x.wrapped                                    # Print my member
[1, 2, 3, 4]

>>> x = wrapper({"a": 1, "b": 2})                # Wrap a dictionary
>>> list(x.keys())                               # Delegate to dictionary method
Trace: keys
['a', 'b']



class C1:
    def meth1(self): self.X = 88         # I assume X is mine
    def meth2(self): print(self.X)

class C2:
    def metha(self): self.X = 99         # Me too
    def methb(self): print(self.X)

class C3(C1, C2): ...
I = C3()                                 # Only 1 X in I!



### file: private.py

class C1:
    def meth1(self): self.__X = 88       # Now X is mine
    def meth2(self): print(self.__X)     # Becomes _C1__X in I
class C2:
    def metha(self): self.__X = 99       # Me too
    def methb(self): print(self.__X)     # Becomes _C2__X in I

class C3(C1, C2): pass
I = C3()                                 # Two X names in I

I.meth1(); I.metha()
print(I.__dict__)
I.meth2(); I.methb()



% python private.py
{'_C2__X': 99, '_C1__X': 88}
88
99



class Super:
    def method(self): ...                  # A real application method

class Tool:
    def __method(self): ...                # Becomes _Tool__method
    def other(self): self.__method()       # Use my internal method 

class Sub1(Tool, Super): ...
    def actions(self): self.method()       # Runs Super.method as expected

class Sub2(Tool):
    def __init__(self): self.method = 99   # Doesn't break Tool.__method



class Spam:
    def doit(self, message):
        print(message)

object1 = Spam()
object1.doit('hello world')

object1 = Spam()
x = object1.doit        # Bound method object: instance+function
x('hello world')        # Same effect as object1.doit('...')

object1 = Spam()
t = Spam.doit           # Unbound method object (a function in 3.0: see ahead)
t(object1, 'howdy')     # Pass in instance (if the method expects one in 3.0)



class Eggs:
    def m1(self, n):
        print(n)
    def m2(self):
        x = self.m1     # Another bound method object
        x(42)           # Looks like a simple function

Eggs().m2()             # Prints 42



C:\misc> c:\python30\python
>>> class Selfless:
...     def __init__(self, data):
...         self.data = data
...     def selfless(arg1, arg2):               # A simple function in 3.0
...         return arg1 + arg2
...     def normal(self, arg1, arg2):           # Instance expected when called
...         return self.data + arg1 + arg2
...
>>> X = Selfless(2)
>>> X.normal(3, 4)                  # Instance passed to self automatically
9
>>> Selfless.normal(X, 3, 4)        # self expected by method: pass manually
9
>>> Selfless.selfless(3, 4)         # No instance: works in 3.0, fails in 2.6!
7

>>> X.selfless(3, 4)
TypeError: selfless() takes exactly 2 positional arguments (3 given)

>>> Selfless.normal(3, 4)
TypeError: normal() takes exactly 3 positional arguments (2 given)



>>> class Number:
...     def __init__(self, base):
...         self.base = base
...     def double(self):
...         return self.base * 2
...     def triple(self):
...         return self.base * 3
...
>>> x = Number(2)                                       # Class instance objects
>>> y = Number(3)                                       # State + methods
>>> z = Number(4)
>>> x.double()                                          # Normal immediate calls
4

>>> acts = [x.double, y.double, y.triple, z.double]     # List of bound methods
>>> for act in acts:                                    # Calls are deferred
...     print(act())                                    # Call as though functions
...
4
6
9
8



>>> bound = x.double
>>> bound.__self__, bound.__func__
(<__main__.Number object at 0x0278F610>, <function double at 0x027A4ED0>)
>>> bound.__self__.base
2
>>> bound()                             # Calls bound.__func__(bound.__self__, ...)
4



>>> def square(arg):
...     return arg ** 2                          # Simple functions (def or lambda)
...
>>> class Sum:
...     def __init__(self, val):                 # Callable instances
...         self.val = val
...     def __call__(self, arg):
...         return self.val + arg
...
>>> class Product:
...     def __init__(self, val):                 # Bound methods
...         self.val = val
...     def method(self, arg):
...         return self.val * arg
...
>>> sobject = Sum(2)
>>> pobject = Product(3)
>>> actions = [square, sobject, pobject.method]  # Function, instance, method

>>> for act in actions:                          # All 3 called same way
...     print(act(5))                            # Call any 1-arg callable
...
25
7
15
>>> actions[-1](5)                               # Index, comprehensions, maps
15
>>> [act(5) for act in actions]
[25, 7, 15]
>>> list(map(lambda act: act(5), actions))
[25, 7, 15]



>>> class Negate:
...     def __init__(self, val):                 # Classes are callables too
...         self.val = -val                      # But called for object, not work
...     def __repr__(self):                      # Instance print format
...         return str(self.val)
...
>>> actions = [square, sobject, pobject.method, Negate]     # Call a class too
>>> for act in actions:
...     print(act(5))
...
25
7
15
-5
>>> [act(5) for act in actions]                     # Runs __repr__ not __str__!
[25, 7, 15, -5]

>>> table = {act(5): act for act in actions}        # 2.6/3.0 dict comprehension
>>> for (key, value) in table.items():
...     print('{0:2} => {1}'.format(key, value))    # 2.6/3.0 str.format
...
-5 => <class '__main__.Negate'>
25 => <function square at 0x025D4978>
15 => <bound method Product.method of <__main__.Product object at 0x025D0F90>>
 7 => <__main__.Sum object at 0x025D0F70>



# NOTE: see also the elaboration of this sidebar on the book's web page,
# http://www.rmi.net/~lutz/lp4e-updates.html; in particular, lambdas are
# not necessary if the handler is a zero-argument method call


def handler():
    ...use globals for state...
...
widget = Button(text='spam', command=handler)


class MyWidget:
    def handler(self):
        ...use self.attr for state...
    def makewidgets(self):
        b = Button(text='spam', command=self.handler)



>>> class Spam:
...     def __init__(self):                   # No __repr__ or __str__
...         self.data1 = "food"
...
>>> X = Spam()
>>> print(X)                                  # Default: class, address
<__main__.Spam object at 0x00864818>          # Displays "instance" in Python 2.6



# NOTE: the following code had a typo in the book, fixes here 
# ("retubrn" instead of "return")



### File: lister.py

class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of
    instances via inheritance of __str__, coded here; displays
    instance attrs only; self is the instance of lowest class;
    uses __X names to avoid clashing with client's attrs
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attrnames())              # name=value list
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):                  # Instance attr dict
            result += '\tname %s=%s\n' % (attr, self.__dict__ [attr])
        return result



>>> from lister import ListInstance
>>> class Spam(ListInstance):                    # Inherit a __str__ method
...     def __init__(self):
...         self.data1 = 'food'
...
>>> x = Spam()
>>> print(x)                                     # print() and str() run __str__
<Instance of Spam, address 40240880:
        name data1=food
>

>>> str(x)
'<Instance of Spam, address 40240880:\n\tname data1=food\n>'
>>> x                                            # The __repr__ still is a default
<__main__.Spam object at 0x026606F0>



### File: testmixin.py

from lister import *                  # Get lister tool classes

class Super:
    def __init__(self):               # Superclass __init__
        self.data1 = 'spam'           # Create instance attrs
    def ham(self):
        pass

class Sub(Super, ListInstance):       # Mix in ham and a __str__
    def __init__(self):               # listers have access to self
        Super.__init__(self)
        self.data2 = 'eggs'           # More instance attrs
        self.data3 = 42
    def spam(self):                   # Define another method here
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                          # Run mixed-in __str__



C:\misc> C:\python30\python testmixin.py
<Instance of Sub, address 40962576:
        name data1=spam
        name data2=eggs
        name data3=42
>



>>> import lister
>>> class C(lister.ListInstance): pass
...
>>> x = C()
>>> x.a = 1; x.b = 2; x.c = 3
>>> print(x)
<Instance of C, address 40961776:
        name a=1
        name b=2
        name c=3
>



### File lister.py, continued

class ListInherited:
    """
    Use dir() to collect both instance attrs and names
    inherited from its classes; Python 3.0 shows more
    names than 2.6 because of the implied object superclass
    in the new-style class model; getattr() fetches inherited
    names not in self.__dict__; use __str__, not __repr__,
    or else this loops when printing bound methods!
    """
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
                           self.__class__.__name__,         # My class's name
                           id(self),                        # My address
                           self.__attrnames())              # name=value list
    def __attrnames(self):
        result = ''
        for attr in dir(self):                              # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__':      # Skip internals
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result


### File: testmixin.py (change)
class Sub(Super, ListInherited):                            # Mix in a __str__

C:\misc> c:\python26\python testmixin.py

C:\misc> c:\python30\python testmixin.py



### File lister.py, continued

class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class
    tree and all its objects’ attrs at and above self;
    run by print(), str() returns constructed string;
    uses __X attr names to avoid impacting clients;
    uses generator expr to recurse to superclasses;
    uses str.format() to make substitutions clearer
    """
    def __str__(self):
        self.__visited = {}
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
                           self.__class__.__name__,
                           id(self),                        
                           self.__attrnames(self, 0),
                           self.__listclass(self.__class__, 4))

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                           dots,
                           aClass.__name__,
                           id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(
                           dots,
                           aClass.__name__,
                           id(aClass),
                           self.__attrnames(aClass, indent),
                           ''.join(genabove),
                           dots)

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}=<>\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result




### File: testmixin.py (change
class Sub(Super, ListTree):         # Mix in a __str__

C:\misc> c:\python26\python testmixin.py

C:\misc> c:\python30\python testmixin.py



>>> from lister import ListTree
>>> from tkinter import Button                  # Both classes have a __str__
>>> class MyButton(ListTree, Button): pass      # ListTree first: use its __str__
...
>>> B = MyButton(text='spam')
>>> open('savetree.txt', 'w').write(str(B))     # Save to a file for later viewing
18247
>>> print(B)                                    # Print the display here 
<Instance of MyButton, address 44355632:
    _ListTree__visited={}
    _name=44355632
    _tclCommands=[]
    ...much more omitted...
>



def factory(aClass, *args):               # Varargs tuple
    return aClass(*args)                  # Call aClass (or apply() in 2.6 only)

class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job  = job

object1 = factory(Spam)                      # Make a Spam object
object2 = factory(Person, "Guido", "guru")   # Make a Person object



def factory(aClass, *args, **kwargs):        # +kwargs dict
    return aClass(*args, **kwargs)           # Call aClass



classname = ...parse from config file...
classarg  = ...parse from config file...

import streamtypes                           # Customizable code
aclass = getattr(streamtypes, classname)     # Fetch from module
reader = factory(aclass, classarg)           # Or aclass(classarg)
processor(reader, ...)



