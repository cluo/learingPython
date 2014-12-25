### file: setwrapper.py

class Set:
   def __init__(self, value = []):    # Constructor
       self.data = []                 # Manages a list
       self.concat(value)

   def intersect(self, other):        # other is any sequence
       res = []                       # self is the subject
       for x in self.data:
           if x in other:             # Pick common items
               res.append(x)
       return Set(res)                # Return a new Set

   def union(self, other):            # other is any sequence
       res = self.data[:]             # Copy of my list
       for x in other:                # Add items in other
           if not x in res:
               res.append(x)
       return Set(res)

   def concat(self, value):           # value: list, Set...
       for x in value:                # Removes duplicates
          if not x in self.data:
               self.data.append(x)

   def __len__(self):          return len(self.data)            # len(self)
   def __getitem__(self, key): return self.data[key]            # self[i]
   def __and__(self, other):   return self.intersect(other)     # self & other
   def __or__(self, other):    return self.union(other)         # self | other
   def __repr__(self):         return 'Set:' + repr(self.data)  # print()



x = Set([1, 3, 5, 7])
print(x.union(Set([1, 4, 7])))       # prints Set:[1, 3, 5, 7, 4] 
print(x | Set([1, 4, 6]))            # prints Set:[1, 3, 5, 7, 4, 6]



### file: typesubclass.py

# Subclass built-in list type/class
# Map 1..N to 0..N-1; call back to built-in version.

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)

if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')               # __init__ inherited from list
    print(x)                        # __repr__ inherited from list

    print(x[1])                     # MyList.__getitem__
    print(x[3])                     # Customizes list superclass method

    x.append('spam'); print(x)      # Attributes from list superclass
    x.reverse();      print(x)



% python typesubclass.py



### file: setsubclass.py

class Set(list):
    def __init__(self, value = []):      # Constructor
        list.__init__([])                # Customizes list
        self.concat(value)               # Copies mutable defaults

    def intersect(self, other):          # other is any sequence
        res = []                         # self is the subject
        for x in self:
            if x in other:               # Pick common items
                res.append(x)
        return Set(res)                  # Return a new Set

    def union(self, other):              # other is any sequence
        res = Set(self)                  # Copy me and my list
        res.concat(other)
        return res

    def concat(self, value):             # value: list, Set . . .
        for x in value:                  # Removes duplicates
            if not x in self:
                self.append(x)

    def __and__(self, other): return self.intersect(other)
    def __or__(self, other):  return self.union(other)
    def __repr__(self):       return 'Set:' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersect(y), y.union(x))
    print(x & y, x | y)
    x.reverse(); print(x)



% python setsubclass.py



C:\misc> c:\python26\python
>>> class C: pass                       # Classic classes in 2.6
...
>>> I = C()
>>> type(I)                             # Instances are made from classes
<type 'instance'>
>>> I.__class__
<class __main__.C at 0x025085A0>

>>> type(C)                             # But classes are not the same as types
<type 'classobj'>
>>> C.__class__
AttributeError: class C has no attribute '__class__'

>>> type([1, 2, 3])
<type 'list'>
>>> type(list)
<type 'type'>
>>> list.__class__
<type 'type'>



C:\misc> c:\python26\python
>>> class C(object): pass               # New-style classes in 2.6
...
>>> I = C()
>>> type(I)                             # Type of instance is class it's made from
<class '__main__.C'>
>>> I.__class__
<class '__main__.C'>

>>> type(C)                             # Classes are user-defined types
<type 'type'>
>>> C.__class__
<type 'type'>

>>> type([1, 2, 3])                     # Built-in types work the same way
<type 'list'>
>>> type(list)
<type 'type'>
>>> list.__class__
<type 'type'>



C:\misc> c:\python30\python
>>> class C: pass                       # All classes are new-style in 3.0
...
>>> I = C()
>>> type(I)                             # Type of instance is class it's made from
<class '__main__.C'>
>>> I.__class__
<class '__main__.C'>

>>> type(C)                             # Class is a type, and type is a class
<class 'type'>
>>> C.__class__
<class 'type'>

>>> type([1, 2, 3])                     # Classes and built-in types work the same
<class 'list'>
>>> type(list)
<class 'type'>
>>> list.__class__
<class 'type'>



C:\misc> c:\python30\python
>>> class C: pass
...
>>> class D: pass
...
>>> c = C()
>>> d = D()
>>> type(c) == type(d)                 # 3.0: compares the instances' classes
False

>>> type(c), type(d)
(<class '__main__.C'>, <class '__main__.D'>)
>>> c.__class__, d.__class__
(<class '__main__.C'>, <class '__main__.D'>)

>>> c1, c2 = C(), C()
>>> type(c1) == type(c2)
True



C:\misc> c:\python26\python
>>> class C: pass
...
>>> class D: pass
...
>>> c = C()
>>> d = D()
>>> type(c) == type(d)                 # 2.6: all instances are same type
True
>>> c.__class__ == d.__class__         # Must compare classes explicitly
False

>>> type(c), type(d)
(<type 'instance'>, <type 'instance'>)
>>> c.__class__, d.__class__
(<class __main__.C at 0x024585A0>, <class __main__.D at 0x024588D0>)



C:\misc> c:\python26\python
>>> class C(object): pass
...
>>> class D(object): pass
...
>>> c = C()
>>> d = D()
>>> type(c) == type(d)                 # 2.6 new-style: same as all in 3.0
False

>>> type(c), type(d)
(<class '__main__.C'>, <class '__main__.D'>)
>>> c.__class__, d.__class__
(<class '__main__.C'>, <class '__main__.D'>)



>>> class C: pass
...
>>> X = C()

>>> type(X)                           # Type is now class instance was created from
<class '__main__.C'>
>>> type(C)
<class 'type'>



>>> isinstance(X, object)
True
>>> isinstance(C, object)             # Classes always inherit from object
True



>>> type('spam')
<class 'str'>
>>> type(str)
<class 'type'>

>>> isinstance('spam', object)        # Same for  built-in types (classes)
True
>>> isinstance(str, object)
True



>>> type(type)                        # All classes are types, and vice versa
<class 'type'>
>>> type(object)
<class 'type'>

>>> isinstance(type, object)          # All classes derive from object, even type
True
>>> isinstance(object, type)          # Types make classes, and type is a class
True
>>> type is object
False



>>> class A:      
        attr = 1         # Classic (Python 2.6)

>>> class B(A):          # B and C both lead to A   
        pass

>>> class C(A):   
        attr = 2

>>> class D(B, C): 
        pass             # Tries A before C

>>> x = D()
>>> x.attr               # Searches x, D, B, A
1



>>> class A(object): 
        attr = 1         # New-style ("object" not required in 3.0)

>>> class B(A):      
        pass

>>> class C(A):      
        attr = 2

>>> class D(B, C):    
        pass             # Tries C before A

>>> x = D()
>>> x.attr               # Searches x, D, B, C
2



>>> class A:      
        attr = 1         # Classic

>>> class B(A):   
        pass

>>> class C(A):   
        attr = 2

>>> class D(B, C): 
        attr = C.attr    # Choose C, to the right

>>> x = D()
>>> x.attr               # Works like new-style (all 3.0)
2



>>> class A(object): 
        attr = 1         # New-style

>>> class B(A):
        pass

>>> class C(A):
        attr = 2

>>> class D(B, C):    
        attr = B.attr    # Choose A.attr, above

>>> x = D()
>>> x.attr               # Works like classic (default 2.6)
1



>>> class A:
        def meth(s): print('A.meth')

>>> class C(A):
        def meth(s): print('C.meth')

>>> class B(A):
        pass

>>> class D(B, C): pass            # Use default search order
>>> x = D()                        # Will vary per class type
>>> x.meth()                       # Defaults to classic order in 2.6
A.meth

>>> class D(B, C): meth = C.meth   # Pick C's method: new-style (and 3.0)
>>> x = D()
>>> x.meth()
C.meth

>>> class D(B, C): meth = B.meth   # Pick B's method: classic
>>> x = D()
>>> x.meth()
A.meth



class D(B, C):
    def meth(self):                # Redefine lower
        ...
        C.meth(self)               # Pick C's method by calling



>>> class limiter(object):
...     __slots__ = ['age', 'name', 'job']
...
>>> x = limiter()
>>> x.age                                           # Must assign before use
AttributeError: age

>>> x.age = 40
>>> x.age
40
>>> x.ape = 1000                                    # Illegal: not in __slots__
AttributeError: 'limiter' object has no attribute 'ape'



>>> class C:
...     __slots__ = ['a', 'b']           # __slots__ means no __dict__ by default
...
>>> X = C()
>>> X.a = 1
>>> X.a
1
>>> X.__dict__
AttributeError: 'C' object has no attribute '__dict__'
>>> getattr(X, 'a')
1
>>> setattr(X, 'b', 2)                   # But getattr() and setattr() still work
>>> X.b
2
>>> 'a' in dir(X)                        # And dir() finds slot attributes too
True
>>> 'b' in dir(X)
True



>>> class D:
...     __slots__ = ['a', 'b']
...     def __init__(self): self.d = 4   # Cannot add new names if no __dict__
...	
>>> X = D()
AttributeError: 'D' object has no attribute 'd'



>>> class D:
...     __slots__ = ['a', 'b', '__dict__']    # List __dict__ to include one too
...     c = 3                                 # Class attrs work normally
...     def __init__(self): self.d = 4        # d put in __dict__, a in __slots__
...	                                           
>>> X = D()                   
>>> X.d
4
>>> X.__dict__                   # Some objects have both __dict__ and __slots__
{'d': 4}                         # getattr() can fetch either type of attr
>>> X.__slots__
['a', 'b', '__dict__']
>>> X.c
3
>>> X.a                          # All instance attrs undefined until assigned
AttributeError: a
>>> X.a = 1
>>> getattr(X, 'a',), getattr(X, 'c'), getattr(X, 'd')
(1, 3, 4)



>>> for attr in list(X.__dict__) + X.__slots__:
...     print(attr, '=>', getattr(X, attr))
	
d => 4
a => 1
b => 2
__dict__ => {'d': 4}



>>> for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
...     print(attr, '=>', getattr(X, attr))

	
d => 4
a => 1
b => 2
__dict__ => {'d': 4}



>>> class E:
...     __slots__ = ['c', 'd']            # Superclass has slots
...
>>> class D(E):                                 
...     __slots__ = ['a', '__dict__']     # So does its subclass
...
>>> X = D()
>>> X.a = 1; X.b = 2; X.c = 3             # The instance is the union
>>> X.a, X.c
(1, 3)

>>> E.__slots__                           # But slots are not concatenated
['c', 'd']
>>> D.__slots__
['a', '__dict__']
>>> X.__slots__                           # Instance inherits *lowest* __slots__
['a', '__dict__']
>>> X.__dict__                            # And has its own an attr dict
{'b': 2}

>>> for attr in list(getattr(X, '__dict__', [])) + getattr(X, '__slots__', []):
...     print(attr, '=>', getattr(X, attr))
...
b => 2                                    # Superclass slots missed!
a => 1
__dict__ => {'b': 2}

>>> dir(X)                                # dir() includes all slot names
[...many names omitted... 'a', 'b', 'c', 'd']



>>> class classic:
...     def __getattr__(self, name):
...         if name == 'age':
...             return 40
...         else:
...             raise AttributeError
...
>>> x = classic()
>>> x.age                                 # Runs __getattr__
40
>>> x.name                                # Runs __getattr__
AttributeError



>>> class newprops(object):
...     def getage(self):
...         return 40
...     age = property(getage, None, None, None)  # get, set, del, docs
...
>>> x = newprops()
>>> x.age                                         # Runs getage
40
>>> x.name                                        # Normal fetch
AttributeError: newprops instance has no attribute 'name'



>>> class newprops(object):
...     def getage(self):
...         return 40
...     def setage(self, value):
...         print('set age:', value)
...         self._age = value
...     age = property(getage, setage, None, None)
...
>>> x = newprops()
>>> x.age                                         # Runs getage
40
>>> x.age = 42                                    # Runs setage
set age: 42
>>> x._age                                        # Normal fetch; no getage call
42
>>> x.job = 'trainer'                             # Normal assign; no setage call
>>> x.job                                         # Normal fetch; no getage call
'trainer'



>>> class classic:
...     def __getattr__(self, name):              # On undefined reference
...         if name == 'age':
...             return 40
...         else:
...             raise AttributeError
...     def __setattr__(self, name, value):       # On all assignments
...         print('set:', name, value)
...         if name == 'age':
...             self.__dict__['_age'] = value
...         else:
...             self.__dict__[name] = value
...
>>> x = classic()
>>> x.age                                         # Runs __getattr__
40
>>> x.age = 41                                    # Runs __setattr__
set: age 41
>>> x._age                                        # Defined: no __getattr__ call
41
>>> x.job = 'trainer'                             # Runs __setattr__ again
>>> x.job                                         # Defined: no __getattr__ call



### file: spam.py

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print("Number of instances created: ", Spam.numInstances)



C:\misc> c:\python26\python
>>> from spam import Spam
>>> a = Spam()                   # Cannot call unbound class methods in 2.6
>>> b = Spam()                   # Methods expect a self object by default
>>> c = Spam()

>>> Spam.printNumInstances()
TypeError: unbound method printNumInstances() must be called with Spam instance
as first argument (got nothing instead)
>>> a.printNumInstances()
TypeError: printNumInstances() takes no arguments (1 given)



C:\misc> c:\python30\python
>>> from spam import Spam
>>> a = Spam()                       # Can call functions in class in 3.0
>>> b = Spam()                       # Calls through instances still pass a self 
>>> c = Spam()

>>> Spam.printNumInstances()         # Differs in 3.0
Number of instances created:  3
>>> a.printNumInstances()
TypeError: printNumInstances() takes no arguments (1 given)



Spam.printNumInstances()             # Fails in 2.6, works in 3.0
instance.printNumInstances()         # Fails in both 2.6 and 3.0



### file spam.py (changed)

def printNumInstances():
    print("Number of instances created: ", Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

>>> import spam
>>> a = spam.Spam()
>>> b = spam.Spam()
>>> c = spam.Spam() 
>>> spam.printNumInstances()           # But function may be too far removed
Number of instances created:  3        # And cannot be changed via inheritance
>>> spam.Spam.numInstances
3



class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances(self):
        print("Number of instances created: ", Spam.numInstances)

>>> from spam import Spam
>>> a, b, c = Spam(), Spam(), Spam()
>>> a.printNumInstances()
Number of instances created:  3
>>> Spam.printNumInstances(a)
Number of instances created:  3
>>> Spam().printNumInstances()         # But fetching counter changes counter!
Number of instances created:  4



class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print(self, x)

    def smeth(x):                  # Static: no instance passed
        print(x)

    def cmeth(cls, x):             # Class: gets class, not instance
        print(cls, x)

    smeth = staticmethod(smeth)    # Make smeth a static method
    cmeth = classmethod(cmeth)     # Make cmeth a class method



>>> obj = Methods()                # Make an instance

>>> obj.imeth(1)                   # Normal method, call through instance
<__main__.Methods object...> 1     # Becomes imeth(obj, 1)

>>> Methods.imeth(obj, 2)          # Normal method, call through class
<__main__.Methods object...> 2     # Instance passed explicitly

>>> Methods.smeth(3)               # Static method, call through class
3                                  # No instance passed or expected

>>> obj.smeth(4)                   # Static method, call through instance
4                                  # Instance not passed

>>> Methods.cmeth(5)               # Class method, call through class
<class '__main__.Methods'> 5       # Becomes cmeth(Methods, 5)

>>> obj.cmeth(6)                   # Class method, call through instance
<class '__main__.Methods'> 6       # Becomes cmeth(Methods, 6)



class Spam:
    numInstances = 0                         # Use static method for class data
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances():
        print("Number of instances:", Spam.numInstances)
    printNumInstances = staticmethod(printNumInstances)



>>> a = Spam()
>>> b = Spam()
>>> c = Spam()
>>> Spam.printNumInstances()                 # Call as simple function
Number of instances: 3
>>> a.printNumInstances()                    # Instance argument not passed
Number of instances: 3




class Sub(Spam):
    def printNumInstances():                 # Override a static method
        print("Extra stuff...")              # But call back to original
        Spam.printNumInstances()
    printNumInstances = staticmethod(printNumInstances)

>>> a = Sub()
>>> b = Sub()
>>> a.printNumInstances()                    # Call from subclass instance
Extra stuff...
Number of instances: 2
>>> Sub.printNumInstances()                  # Call from subclass itself
Extra stuff...
Number of instances: 2
>>> Spam.printNumInstances()
Number of instances: 2



>>> class Other(Spam): pass                  # Inherit static method verbatim

>>> c = Other()
>>> c.printNumInstances()
Number of instances: 3



class Spam:
    numInstances = 0                         # Use class method instead of static
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances:", cls.numInstances)
    printNumInstances = classmethod(printNumInstances)



>>> a, b = Spam(), Spam()
>>> a.printNumInstances()                    # Passes class to first argument
Number of instances: 2
>>> Spam.printNumInstances()                 # Also passes class to first argument
Number of instances: 2



class Spam:
    numInstances = 0                         # Trace class passed in
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(cls):
        print("Number of instances:", cls.numInstances, cls)
    printNumInstances = classmethod(printNumInstances)

class Sub(Spam):
    def printNumInstances(cls):              # Override a class method
        print("Extra stuff...", cls)         # But call back to original
        Spam.printNumInstances()
    printNumInstances = classmethod(printNumInstances)

class Other(Spam): pass                      # Inherit class method verbatim



>>> x, y = Sub(), Spam()
>>> x.printNumInstances()                    # Call from subclass instance
Extra stuff... <class 'test.Sub'>
Number of instances: 2 <class 'test.Spam'>
>>> Sub.printNumInstances()                  # Call from subclass itself
Extra stuff... <class 'test.Sub'>
Number of instances: 2 <class 'test.Spam'>
>>> y.printNumInstances()
Number of instances: 2 <class 'test.Spam'>



>>> z = Other()
>>> z.printNumInstances()
Number of instances: 3 <class 'test.Other'>



class Spam:
    numInstances = 0
    def count(cls):                    # Per-class instance counters
        cls.numInstances += 1          # cls is lowest class above instance
    def __init__(self):
        self.count()                   # Passes self.__class__ to count
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0
    def __init__(self):                # Redefines __init__
        Spam.__init__(self)

class Other(Spam):                     # Inherits __init__
    numInstances = 0

>>> x = Spam()
>>> y1, y2 = Sub(), Sub()
>>> z1, z2, z3 = Other(), Other(), Other()
>>> x.numInstances, y1.numInstances, z1.numInstances
(1, 2, 3)
>>> Spam.numInstances, Sub.numInstances, Other.numInstances
(1, 2, 3)



class C:
   @staticmethod                                 # Decoration syntax
   def meth():
       ...



class C:
   def meth():
       ...
   meth = staticmethod(meth)                     # Rebind name



class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

    @staticmethod
    def printNumInstances():
        print("Number of instances created: ", Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()      # Calls from both classes and instances work now!
a.printNumInstances()         # Both print "Number of instances created:  3"



class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func  = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer                       # Same as spam = tracer(spam)
def spam(a, b, c):            # Wrap spam in a decorator object
    print(a, b, c)

spam(1, 2, 3)                 # Really calls the tracer wrapper object
spam('a', 'b', 'c')           # Invokes __call__ in class
spam(4, 5, 6)                 # __call__ adds logic and runs original object



def decorator(aClass): ...

@decorator
class C: ...



def decorator(aClass): ...

class C: ...
C = decorator(C)



def count(aClass):
    aClass.numInstances = 0
    return aClass                  # Return class itself, instead of a wrapper

@count
class Spam: ...                    # Same as Spam = count(Spam)

@count
class Sub(Spam): ...               # numInstances = 0 not needed here

@count
class Other(Spam): ...



class Meta(type):
    def __new__(meta, classname, supers, classdict): ...

class C(metaclass=Meta): ...



class C: 
    __metaclass__ = Meta
    ...



>>> class X:
...     a = 1       # Class attribute
...
>>> I = X()
>>> I.a             # Inherited by instance
1
>>> X.a
1



>>> X.a = 2         # May change more than X
>>> I.a             # I changes too
2
>>> J = X()         # J inherits from X's runtime values
>>> J.a             # (but assigning to J.a changes a in J, not X or I)
2



class X: pass                       # Make a few attribute namespaces
class Y: pass

X.a = 1                             # Use class attributes as variables
X.b = 2                             # No instances anywhere to be found
X.c = 3
Y.a = X.a + X.b + X.c

for X.i in range(Y.a): print(X.i)   # Prints 0..5



class Record: pass
X = Record()
X.name = 'bob'
X.job  = 'Pizza maker'



>>> class C:
...     shared = []                 # Class attribute
...     def __init__(self):
...         self.perobj = []        # Instance attribute
...
>>> x = C()                         # Two instances
>>> y = C()                         # Implicitly share class attrs
>>> y.shared, y.perobj
([], [])

>>> x.shared.append('spam')         # Impacts y's view too!
>>> x.perobj.append('spam')         # Impacts x's data only
>>> x.shared, x.perobj
(['spam'], ['spam'])

>>> y.shared, y.perobj              # y sees change made through x
(['spam'], [])
>>> C.shared                        # Stored on class and shared
['spam']



x.shared.append('spam')    # Changes shared object attached to class in-place
x.shared = 'spam'          # Changed or creates instance attribute attached to x



class ListTree:
    def __str__(self): ...

class Super:
    def __str__(self): ...

class Sub(ListTree, Super):    # Get ListTree's __str__ by listing it first

x = Sub()                      # Inheritance searches ListTree before Super



class ListTree:
    def __str__(self): ...
    def other(self): ...

class Super:
    def __str__(self): ...
    def other(self): ...

class Sub(ListTree, Super):    # Get ListTree's __str__ by listing it first
    other = Super.other        # But explicitly pick Super's version of other
    def __init__(self):
        ...

x = Sub()                      # Inheritance searches Sub before ListTree/Super



class Sub(Super, ListTree):               # Get Super's other by order
    __str__ = Lister.__str__              # Explicitly pick Lister.__str__



def generate():                  # Fails prior to Python 2.2, works later
    class Spam:
        count = 1
        def method(self):        # Name Spam not visible:
            print(Spam.count)    # not local (def), global (module), built-in
    return Spam()

generate().method()

C:\python\examples> python nester.py
...error text omitted...
    Print(Spam.count)            # Not local (def), global (module), built-in
NameError: Spam



def generate():
    global Spam                 # Force Spam to module scope
    class Spam:
        count = 1
        def method(self):
            print(Spam.count)   # Works: in global (enclosing module)
    return Spam()

generate().method()             # Prints 1



def generate():
    return Spam()

class Spam:                    # Define at top level of module
    count = 1
    def method(self):
        print(Spam.count)      # Works: in global (enclosing module)

generate().method()



def generate():
    class Spam:
        count = 1
        def method(self):
            print(self.__class__.count)      # Works: qualify to get class
    return Spam()

generate().method()



### lab code



class Lunch:
    def __init__(self)               # Make/embed Customer and Employee
    def order(self, foodName)        # Start a Customer order simulation
    def result(self)                 # Ask the Customer what Food it has

class Customer:
    def __init__(self)                        # Initialize my food to None
    def placeOrder(self, foodName, employee)  # Place order with an Employee
    def printFood(self)                       # Print the name of my food

class Employee:
    def takeOrder(self, foodName)    # Return a Food, with requested name

class Food:
    def __init__(self, name)         # Store food name



% python
>>> from zoo import Cat, Hacker
>>> spot = Cat()
>>> spot.reply()                   # Animal.reply; calls Cat.speak
meow
>>> data = Hacker()                # Animal.reply; calls Primate.speak
>>> data.reply()
Hello world!



% python
>>> import parrot
>>> parrot.Scene().action()        # Activate nested objects
customer: "that's one ex-bird!"
clerk: "no it isn't..."
parrot: None

