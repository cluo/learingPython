class Extras:
    def extra(self, args):              # Normal inheritance: too static
        ...

class Client1(Extras): ...              # Clients inherit extra methods
class Client2(Extras): ...
class Client3(Extras): ...

X = Client1()                           # Make an instance
X.extra()                               # Run the extra methods




def extra(self, arg): ...

class Client1: ...                      # Client augments: too distributed
if required():
    Client1.extra = extra

class Client2: ...
if required():
    Client2.extra = extra

class Client3: ...
if required():
    Client3.extra = extra

X = Client1()
X.extra()




def extra(self, arg): ...

def extras(Class):                      # Manager function: too manual
    if required():
        Class.extra = extra

class Client1: ...
extras(Client1)

class Client2: ...
extras(Client2)

class Client3: ...
extras(Client3)

X = Client1()
X.extra()




def extra(self, arg): ...

class Extras(type):
    def __init__(Class, classname, superclasses, attributedict):
        if required():
            Class.extra = extra

class Client1(metaclass=Extras): ...    # Metaclass declaration only
class Client2(metaclass=Extras): ...    # Client class is instance of meta
class Client3(metaclass=Extras): ...

X = Client1()                           # X is instance of Client1
X.extra()




def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra
    return Class

class Client1: ...
Client1 = extras(Client1)

class Client2: ...
Client2 = extras(Client2)

class Client3: ...
Client3 = extras(Client3)

X = Client1()
X.extra()




def extra(self, arg): ...

def extras(Class):
    if required():
        Class.extra = extra
    return Class

@extras
class Client1: ...             # Client1 = extras(Client1)

@extras
class Client2: ...             # Rebinds class independent of instances

@extras
class Client3: ...

X = Client1()                  # Makes instance of augmented class
X.extra()                      # X is instance of original Client1




C:\misc> c:\python30\python
>>> type([])                     # In 3.0 list is instance of list type
<class 'list'>
>>> type(type([]))               # Type of list is type class
<class 'type'>

>>> type(list)                   # Same, but with type names
<class 'type'>
>>> type(type)                   # Type of type is type: top of hierarchy
<class 'type'>




C:\misc> c:\python26\python
>>> type([])                     # In 2.6, type is a bit different
<type 'list'>
>>> type(type([]))
<type 'type'>

>>> type(list)
<type 'type'>
>>> type(type)
<type 'type'>




C:\misc> c:\python30\python
>>> class C: pass                 # 3.0 class object (new-style)
...
>>> X = C()                       # Class instance object

>>> type(X)                       # Instance is instance of class
<class '__main__.C'>
>>> X.__class__                   # Instance's class
<class '__main__.C'>

>>> type(C)                       # Class is instance of type
<class 'type'>
>>> C.__class__                   # Class's class is type
<class 'type'>




C:\misc> c:\python26\python
>>> class C(object): pass         # In 2.6 new-style classes,
...                               # classes have a class too
>>> X = C()

>>> type(X)
<class '__main__.C'>
>>> type(C)
<type 'type'>

>>> X.__class__
<class '__main__.C'>
>>> C.__class__
<type 'type'>




C:\misc> c:\python26\python
>>> class C: pass                 # In 2.6 classic classes,
...                               # classes have no class themselves
>>> X = C()

>>> type(X)
<type 'instance'>
>>> type(C)
<type 'classobj'>

>>> X.__class__
<class __main__.C at 0x005F85A0>
>>> C.__class__
AttributeError: class C has no attribute '__class__'




class = type(classname, superclasses, attributedict)

type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)


class Spam(Eggs):                # Inherits from Eggs
    data = 1                     # Class data attribute
    def meth(self, arg):         # Class method attribute
        pass


Spam = type('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module__': '__main__'})




class Spam(metaclass=Meta):                   # 3.0 and later

class Spam(Eggs, metaclass=Meta):             # Other supers okay

class spam(object):                           # 2.6 version (only)
    __metaclass__ = Meta



class = Meta(classname, superclasses, attributedict)

Meta.__new__(Meta, classname, superclasses, attributedict)
Meta.__init__(class, classname, superclasses, attributedict)



class Spam(Eggs, metaclass=Meta):      # Inherits from Eggs, instance of Meta
    data = 1                           # Class data attribute
    def meth(self, arg):               # Class method attribute
        pass

Spam = Meta('Spam', (Eggs,), {'data': 1, 'meth': meth, '__module__': '__main__'})




class Meta(type):
    def __new__(meta, classname, supers, classdict):
        # Run by inherited type.__call__
        return type.__new__(meta, classname, supers, classdict)




class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
  
class Eggs: 
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):      # Inherits from Eggs, instance of Meta
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        pass

print('making instance')
X = Spam()
print('data:', X.data)




class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    
    def __init__(Class, classname, supers, classdict):
        print('In MetaOne init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
  
class Eggs: 
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne):      # Inherits from Eggs, instance of Meta
    data = 1                              # Class data attribute
    def meth(self, arg):                  # Class method attribute
        pass

print('making instance')
X = Spam()
print('data:', X.data)




# A simple function can serve as a metaclass too

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)
  
class Eggs: 
    pass

print('making class')
class Spam(Eggs, metaclass=MetaFunc):            # Run simple function at end
    data = 1                                     # Function returns class
    def meth(self, args):
        pass

print('making instance')
X = Spam()
print('data:', X.data)




# __call__ can be redefined, metas can have metas

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs: 
    pass

print('making class')
class Spam(Eggs, metaclass=SubMeta):      
    data = 1                            
    def meth(self, arg):               
        pass

print('making instance')
X = Spam()
print('data:', X.data)




class SuperMeta:
    def __call__(self, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class

class SubMeta(SuperMeta):
    def __New__(self, classname, supers, classdict):
        print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs: 
    pass

print('making class')
class Spam(Eggs, metaclass=SubMeta()):          # Meta is normal class instance
    data = 1                                    # Called at end of statement
    def meth(self, arg):               
        pass

print('making instance')
X = Spam()
print('data:', X.data)




class MetaOne(type):                                  
    def __new__(meta, classname, supers, classdict):        # Redefine type method
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        print('toast')

class Super(metaclass=MetaOne):        # Metaclass inherited by subs too
    def spam(self):                    # MetaOne run twice for two classes
        print('spam')
        
class C(Super):                        # Superclass: inheritance versus instance
    def eggs(self):                    # Classes inherit from superclasses
        print('eggs')                  # But not from metclasses

X = C()
X.eggs()       # Inherited from C
X.spam()       # Inherited from Super
X.toast()      # Not inherited from metaclass




# Extend manually - adding new methods to classes

class Client1:
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2

class Client2:
    value = 'ni?'

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

Client1.eggs = eggsfunc
Client1.ham  = hamfunc

Client2.eggs = eggsfunc
Client2.ham  = hamfunc

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))




# Extend with a metaclass - supports future changes better

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

class Extender(type):
    def __new__(meta, classname, supers, classdict):
        classdict['eggs'] = eggsfunc
        classdict['ham']  = hamfunc
        return type.__new__(meta, classname, supers, classdict)

class Client1(metaclass=Extender):
    def __init__(self, value):
        self.value = value
    def spam(self):
        return self.value * 2

class Client2(metaclass=Extender):
    value = 'ni?'

X = Client1('Ni!')
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))




# Can also configure class based on runtime tests

class MetaExtend(type):
    def __new__(meta, classname, supers, classdict):
        if sometest():
            classdict['eggs'] = eggsfunc1
        else:
            classdict['eggs'] = eggsfunc2
        if someothertest():
            classdict['ham']  = hamfunc
        else:
            classdict['ham']  = lambda *args: 'Not supported'
        return type.__new__(meta, classname, supers, classdict)




# Extend with a decorator: same as providing __init__ in a metaclass

def eggsfunc(obj):
    return obj.value * 4

def hamfunc(obj, value):
    return value + 'ham'

def Extender(aClass):
    aClass.eggs = eggsfunc                   # Manages class, not instance
    aClass.ham  = hamfunc                    # Equiv to metaclass __init__
    return aClass

@Extender
class Client1:                               # Client1 = Extender(Client1)
    def __init__(self, value):               # Rebound at end of class stmt
        self.value = value
    def spam(self):
        return self.value * 2

@Extender
class Client2:
    value = 'ni?'

X = Client1('Ni!')                           # X is a Client1 instance
print(X.spam())
print(X.eggs())
print(X.ham('bacon'))

Y = Client2()
print(Y.eggs())
print(Y.ham('bacon'))




# Class decorator to trace external instance attribute fetches

def Tracer(aClass):                                   # On @decorator
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.wrapped = aClass(*args, **kargs)     # Use enclosing scope name 
        def __getattr__(self, attrname):
            print('Trace:', attrname)                 # Catches all but .wrapped 
            return getattr(self.wrapped, attrname)    # Delegate to wrapped object
    return Wrapper

@Tracer
class Person:                                         # Person = Tracer(Person)
    def __init__(self, name, hours, rate):            # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                              # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate

bob = Person('Bob', 40, 50)                           # bob is really a Wrapper
print(bob.name)                                       # Wrapper embeds a Person
print(bob.pay())                                      # Triggers __getattr__




# Manage instances like the prior example, but with a metaclass

def Tracer(classname, supers, classdict):             # On class creation call
    aClass = type(classname, supers, classdict)       # Make client class
    class Wrapper:
        def __init__(self, *args, **kargs):           # On instance creation
            self.wrapped = aClass(*args, **kargs)
        def __getattr__(self, attrname):
            print('Trace:', attrname)                 # Catches all but .wrapped 
            return getattr(self.wrapped, attrname)    # Delegate to wrapped object
    return Wrapper

class Person(metaclass=Tracer):                       # Make Person with Tracer
    def __init__(self, name, hours, rate):            # Wrapper remembers Person
        self.name = name
        self.hours = hours
        self.rate = rate                              # In-method fetch not traced
    def pay(self):
        return self.hours * self.rate

bob = Person('Bob', 40, 50)                           # bob is really a Wrapper
print(bob.name)                                       # Wrapper embeds a Person
print(bob.pay())                                      # Triggers __getattr__




### File: mytools.py
# File mytools.py: assorted decorator tools

def tracer(func):                         # Use function, not class with __call__
    calls = 0                             # Else self is decorator instance only
    def onCall(*args, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

import time
def timer(label='', trace=True):                # On decorator args: retain args
    def onDecorator(func):                      # On @: retain decorated func
        def onCall(*args, **kargs):             # On calls: call original
            start   = time.clock()              # State is scopes + func attr
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




from mytools import tracer

class Person:
    @tracer
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay

    @tracer
    def giveRaise(self, percent):         # giveRaise = tracer(giverRaise)
        self.pay *= (1.0 + percent)       # onCall remembers giveRaise

    @tracer
    def lastName(self):                   # lastName = tracer(lastName)
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                        # Runs onCall(sue, .10)
print(sue.pay)
print(bob.lastName(), sue.lastName())     # Runs onCall(bob), remembers lastName




# Metaclass that adds tracing decorator to every method of a client class

from types import FunctionType
from mytools import tracer

class MetaTrace(type):                                  
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:                      # Method?
                classdict[attr] = tracer(attrval)                  # Decorate it
        return type.__new__(meta, classname, supers, classdict)    # Make class

class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())




# Metaclass factory: apply any decorator to all methods of a class

from types import FunctionType
from mytools import tracer, timer

def decorateAll(decorator):
    class MetaDecorate(type):                                  
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:         
                    classdict[attr] = decorator(attrval)  
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate

class Person(metaclass=decorateAll(tracer)):       # Apply a decorator to all
    def __init__(self, name, pay):
        self.name = name
        self.pay  = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())




class Person(metaclass=decorateAll(tracer)):               # Apply tracer

class Person(metaclass=decorateAll(timer())):              # Apply timer, defaults

class Person(metaclass=decorateAll(timer(label='**'))):    # Decorator arguments



# If using timer: total time per method

print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)




# Class decorator factory: apply any decorator to all methods of a class

from types import FunctionType
from mytools import tracer, timer

def decorateAll(decorator):
    def DecoDecorate(aClass):
        for attr, attrval in aClass.__dict__.items():
            if type(attrval) is FunctionType: 
                setattr(aClass, attr, decorator(attrval))        # Not __dict__  
        return aClass
    return DecoDecorate

@decorateAll(tracer)                          # Use a class decorator
class Person:                                 # Applies func decorator to methods
    def __init__(self, name, pay):            # Person = decorateAll(..)(Person)
        self.name = name                      # Person = DecoDecorate(Person)
        self.pay  = pay
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())




@decorateAll(tracer)                 # Decorate all with tracer

@decorateAll(timer())                # Decorate all with timer, defaults

@decorateAll(timer(label='@@'))      # Same but pass a decorator argument



# If using timer: total time per method

print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)






