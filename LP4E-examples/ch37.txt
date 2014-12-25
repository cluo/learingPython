# NOTE: many examples in this chapter are script files, but are 
# not named; to run, cut and paste into a .py text file of your
# choosing, and run with a shell command, IDLE, or other technique.
# At this point in the book, this is assumed knowledge.


person.name                 # Fetch attribute value
person.name = value         # Change attribute value




class Person:
    def getName(self):
        if not valid():
            raise TypeError('cannot fetch name')
	    else:
            return self.name.transform()
    def setName(self, value):
        if not valid(value):
            raise TypeError('cannot change name')
        else:
            self.name = transform(value)

person = Person()
person.getName()
person.setName('value')




attribute = property(fget, fset, fdel, doc) 




class Person:                       # Use (object) in 2.6
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs getName
bob.name = 'Robert Smith'           # Runs setName
print(bob.name)
del bob.name                        # Runs delName

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
print(Person.name.__doc__)          # Or help(Person.name)




class Super:
    ...the original Person class code...
    name = property(getName, setName, delName, 'name property docs')

class Person(Super):
    pass                            # Properties are inherited

bob = Person('Bob Smith')
...rest unchanged...




class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):                         # On attr fetch
        return self.value ** 2 
    def setX(self, value):                  # On attr assign              
        self.value = value
    X = property(getX, setX)                # No delete or docs

P = PropSquare(3)       # 2 instances of class with property
Q = PropSquare(32)      # Each has different state information

print(P.X)              # 3 ** 2
P.X = 4
print(P.X)              # 4 ** 2
print(Q.X)              # 32 ** 2




class Person:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):                 # name = property(name)
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):          # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self):                 # name = name.deleter(name)
        print('remove...')
        del self._name

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs name getter (name 1)
bob.name = 'Robert Smith'           # Runs name setter (name 2)
print(bob.name)
del bob.name                        # Runs name deleter (name 3)

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
print(Person.name.__doc__)          # Or help(Person.name)




class Descriptor:
    "docstring goes here"
    def __get__(self, instance, owner): ...        # Return attr value
    def __set__(self, instance, value): ...        # Return nothing (None)
    def __delete__(self, instance): ...            # Return nothing (None)




>>> class Descriptor(object):
...     def __get__(self, instance, owner):
...         print(self, instance, owner, sep='\n')
...
>>> class Subject:
...     attr = Descriptor()             # Decriptor instance is class attr
...
>>> X = Subject()

>>> X.attr
<__main__.Descriptor object at 0x0281E690>
<__main__.Subject object at 0x028289B0>
<class '__main__.Subject'>

>>> Subject.attr
<__main__.Descriptor object at 0x0281E690>
None
<class '__main__.Subject'>




>>> class D:
...     def __get__(*args): print('get')
...
>>> class C:
...     a = D()
...
>>> X = C()
>>> X.a                                 # Runs inherited descriptor __get__
get
>>> C.a
get
>>> X.a = 99                            # Stored on X, hiding C.a
>>> X.a
99
>>> list(X.__dict__.keys())
['a']
>>> Y = C()
>>> Y.a                                 # Y still inherits descriptor
get
>>> C.a
get




>>> class D:
...     def __get__(*args): print('get')
...     def __set__(*args): raise AttributeError('cannot set')
...
>>> class C:
...     a = D()
...
>>> X = C()
>>> X.a                                 # Routed to C.a.__get__
get
>>> X.a = 99                            # Routed to C.a.__set__
AttributeError: cannot set




class Name:                             # Use (object) in 2.6
    "name descriptor docs"
    def __get__(self, instance, owner):
        print('fetch...')
        return instance._name
    def __set__(self, instance, value):
        print('change...')
        instance._name = value
    def __delete__(self, instance):
        print('remove...')
        del instance._name

class Person:                           # Use (object) in 2.6
    def __init__(self, name):
        self._name = name
    name = Name()                       # Assign descriptor to attr

bob = Person('Bob Smith')               # bob has a managed attribute
print(bob.name)                         # Runs Name.__get__
bob.name = 'Robert Smith'               # Runs Name.__set__
print(bob.name)
del bob.name                            # Runs Name.__delete__

print('-'*20)
sue = Person('Sue Jones')               # sue inherits descriptor too
print(sue.name)
print(Name.__doc__)                     # Or help(Name)




...
class Super:
    def __init__(self, name):
        self._name = name
    name = Name()

class Person(Super):                            # Descriptors are inherited
   pass
...




class Person:
    def __init__(self, name):
        self._name = name

    class Name:                                 # Using a nested class
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name
    name = Name()




...
print(Person.Name.__doc__)     # Differs: not Name.__doc__ outside class




class DescSquare:
    def __init__(self, start):                  # Each desc has own state
        self.value = start
    def __get__(self, instance, owner):         # On attr fetch
        return self.value ** 2
    def __set__(self, instance, value):         # On attr assign
        self.value = value                      # No delete or docs

class Client1:
    X = DescSquare(3)          # Assign descriptor instance to class attr

class Client2:
    X = DescSquare(32)         # Another instance in another client class
                               # Could also code 2 instances in same class
c1 = Client1()
c2 = Client2()

print(c1.X)                    # 3 ** 2
c1.X = 4
print(c1.X)                    # 4 ** 2
print(c2.X)                    # 32 ** 2




class DescState:                           # Use descriptor state
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):    # On attr fetch
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):    # On attr assign
        print('DescState set')
        self.value = value

# Client class

class CalcAttrs:
    X = DescState(2)                       # Descriptor class attr
    Y = 3                                  # Class attr 
    def __init__(self):
        self.Z = 4                         # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                 # X is computed, others are not
obj.X = 5                                  # X assignment is intercepted
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)




class InstState:                           # Using instance state
    def __get__(self, instance, owner):
        print('InstState get')             # Assume set by client class
        return instance._Y * 100
    def __set__(self, instance, value):    
        print('InstState set')
        instance._Y = value

# Client class

class CalcAttrs:
    X = DescState(2)                       # Descriptor class attr
    Y = InstState()                        # Descriptor class attr
    def __init__(self):
        self._Y = 3                        # Instance attr
        self.Z  = 4                        # Instance attr

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                 # X and Y are computed, Z is not 
obj.X = 5                                  # X and Y arssignments intercepted
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)




class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset 
        self.fdel = fdel                                  # Save unbound methods
        self.__doc__ = doc                                # or other callables

    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self         
        if self.fget is None:
            raise AttributeError("can't get attribute")
        return self.fget(instance)                        # Pass instance to self
                                                          # in property accessors
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(instance, value)

    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(instance)

class Person:
    def getName(self): ...
    def setName(self, value): ...
    name = Property(getName, setName)                     # Use like property()




def __getattr__(self, name):        # On undefined attribute fetch [obj.name]
def __getattribute__(self, name):   # On all attribute fetch [obj.name]
def __setattr__(self, name, value): # On all attribute assignment [obj.name=value]
def __delattr__(self, name):        # On all attribute deletion [del obj.name]




class Catcher:
    def __getattr__(self, name):
        print('Get:', name)
    def __setattr__(self, name, value):
        print('Set:', name, value)

X = Catcher()
X.job                               # Prints "Get: job"
X.pay                               # Prints "Get: pay"
X.pay = 99                          # Prints "Set: pay 99"




class Wrapper:
    def __init__(self, object):
        self.wrapped = object                    # Save object
    def __getattr__(self, attrname):
        print('Trace:', attrname)                # Trace fetch
        return getattr(self.wrapped, attrname)   # Delegate fetch




    def __getattribute__(self, name):
        x = self.other                                # LOOPS!

    def __getattribute__(self, name):
        x = object.__getattribute__(self, 'other')    # Force higher to avoid me

    def __setattr__(self, name, value):
        self.other = value                            # LOOPS!

    def __setattr__(self, name, value):
        self.__dict__['other'] = value                # Use atttr dict to avoid me

    def __setattr__(self, name, value):
        object.__setattr__(self, 'other', value)      # Force higher to avoid me

    def __getattribute__(self, name):
        x = self.__dict__['other']                    # LOOPS!




class Person:
    def __init__(self, name):               # On [Person()]
        self._name = name                   # Triggers __setattr__!

    def __getattr__(self, attr):            # On [obj.undefined]
        if attr == 'name':                  # Intercept name: not stored
            print('fetch...')
            return self._name               # Does not loop: real attr
        else:                               # Others are errors
            raise AttributeError(attr)

    def __setattr__(self, attr, value):     # On [obj.any = value]
        if attr == 'name':
            print('change...')
            attr = '_name'                  # Set internal name
        self.__dict__[attr] = value         # Avoid looping here

    def __delattr__(self, attr):            # On [del obj.any]
        if attr == 'name':
            print('remove...')
            attr = '_name'                  # Avoid looping here too
        del self.__dict__[attr]             # but much less common

bob = Person('Bob Smith')           # bob has a managed attribute
print(bob.name)                     # Runs __getattr__
bob.name = 'Robert Smith'           # Runs __setattr__
print(bob.name)
del bob.name                        # Runs __delattr__

print('-'*20)
sue = Person('Sue Jones')           # sue inherits property too
print(sue.name)
#print(Person.name.__doc__)         # No equivalent here




    # Replace __getattr__ with this

    def __getattribute__(self, attr):                 # On [obj.any]
        if attr == 'name':                            # Intercept all names
            print('fetch...')
            attr = '_name'                            # Map to internal name
        return object.__getattribute__(self, attr)    # Avoid looping here




class AttrSquare:
    def __init__(self, start):
        self.value = start                            # Triggers __setattr__!
        
    def __getattr__(self, attr):                      # On undefined attr fetch
        if attr == 'X':
            return self.value ** 2                    # value is not undefined
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):               # On all attr assignments
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value

A = AttrSquare(3)       # 2 instances of class with overloading
B = AttrSquare(32)      # Each has different state information

print(A.X)              # 3 ** 2
A.X = 4
print(A.X)              # 4 ** 2
print(B.X)              # 32 ** 2




class AttrSquare:
    def __init__(self, start):
        self.value = start                  # Triggers __setattr__!
        
    def __getattribute__(self, attr):       # On all attr fetches
        if attr == 'X':
            return self.value ** 2          # Triggers __getattribute__ again!
        else:
            return object.__getattribute__(self, attr)

    def __setattr__(self, attr, value):     # On all attr assignments
        if attr == 'X':
            attr = 'value'
        object.__setattr__(self, attr, value)




    def __getattribute__(self, attr):
        if attr == 'X':
            return object.__getattribute__(self, 'value') ** 2




class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):            # On undefined attrs only
        print('get: ' + attr)               # Not attr1: inherited from class
        return 3                            # Not attr2: stored on instance

X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)

print('-'*40)

class GetAttribute(object):                 # (object) needed in 2.6 only
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr):       # On all attr fetches
        print('get: ' + attr)               # Use superclass to avoid looping here
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)




# 2 dynamically computed attributes with properties

class Powers:
    def __init__(self, square, cube):
        self._square = square                      # _square is the base value
        self._cube   = cube                        # square is the property name

    def getSquare(self):
        return self._square ** 2
    def setSquare(self, value):
        self._square = value
    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3
    cube = property(getCube)

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25




# Same, but with descriptors

class DescSquare:
    def __get__(self, instance, owner):
        return instance._square ** 2
    def __set__(self, instance, value):
        instance._square = value

class DescCube:
    def __get__(self, instance, owner):
        return instance._cube ** 3

class Powers:                                  # Use (object) in 2.6
    square = DescSquare()
    cube   = DescCube()
    def __init__(self, square, cube):
        self._square = square                  # "self.square = square" works too,
        self._cube   = cube                    # because it triggers desc __set__!

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25




# Same, but with generic __getattr__ undefined attribute interception

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube   = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25




# Same, but with generic __getattribute__ all attribute interception

class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube   = cube
    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)
    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square)      # 3 ** 2 = 9
print(X.cube)        # 4 ** 3 = 64
X.square = 5
print(X.square)      # 5 ** 2 = 25




### file: getattr.py

class GetAttr:
    eggs = 88             # eggs stored on class, spam on instance
    def __init__(self):
       self.spam = 77
    def __len__(self):    # len here, else __getattr__ called with __len__
        print('__len__: 42')
        return 42
    def __getattr__(self, attr):     # Provide __str__ if asked, else dummy func
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None

class GetAttribute(object):          # object required in 2.6, implied in 3.0
    eggs = 88                        # In 2.6 all are isinstance(object) auto
    def __init__(self):              # But must derive to get new-style tools,
        self.spam = 77               # incl __getattribute__, some __X__ defaults
    def __len__(self):
        print('__len__: 42')
        return 42
    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None

for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))

    X = Class()
    X.eggs               # Class attr
    X.spam               # Instance attr
    X.other              # Missing attr
    len(X)               # __len__ defined explicitly
    
    try:                 # New-styles must support [], +, call directly: redefine
        X[0]             # __getitem__?
    except:
        print('fail []')

    try:
        X + 99           # __add__?
    except:
        print('fail +')

    try:
        X()              # __call__?  (implicit via built-in)
    except:
        print('fail ()')
    X.__call__()         # __call__?  (explicit, not inherited)

    print(X.__str__())   # __str__?   (explicit, inherited from type)
    print(X)             # __str__?   (implicit via built-in)




C:\misc> c:\python26\python getattr.py

C:\misc> c:\python30\python getattr.py




# NOTE: this is person.py, despite the getattr.py filename in 
# its first command line (a minor typo in the first printing)



### file: person.py

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)      # Embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)      # Intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr)           # Delegate all other attrs
    def __str__(self):
        return str(self.person)                     # Must overload again (in 3.0)
     
if __name__ == '__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)    # Manager.__init__
    print(tom.lastName())                # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                   # Manager.giveRaise -> Person.giveRaise
    print(tom)                           # Manager.__str__ -> Person.__str__




C:\misc> c:\python30\python person.py          # not gettar.py




# Delete the Manager __str__ method

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)      # Embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)      # Intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr)           # Delegate all other attrs




C:\misc> c:\python30\python person.py

C:\misc> c:\python26\python person.py




# Replace __getattr_ with __getattribute__

class Manager:                                           # Use (object) in 2.6
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)           # Embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)           # Intercept and delegate
    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)   # Fetch my attrs
        else:
            return getattr(self.person, attr)            # Delegate all others




C:\misc> c:\python30\python person.py




# Code __getattribute__ differently to minimize extra calls

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def __getattribute__(self, attr):
        print('**', attr)
        person = object.__getattribute__(self, 'person')
        if attr == 'giveRaise':
            return lambda percent: person.giveRaise(percent+.10)
        else:
            return getattr(person, attr)
    def __str__(self):
        person = object.__getattribute__(self, 'person') 
        return str(person)




class CardHolder:
    acctlen = 8                                # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct                       # Instance data
        self.name = name                       # These trigger prop setters too
        self.age  = age                        # __X mangled to have class name
        self.addr = addr                       # addr is not managed
                                               # remain has no data
    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)
        
    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')
        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)

    def remainGet(self):                       # Could be a method, not attr
        return self.retireage - self.age       # Unless already using as attr
    remain = property(remainGet)




bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
bob.name = 'Bob Q. Smith'
bob.age  = 50
bob.acct = '23-45-67-89'
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')

sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
try:
    sue.age = 200
except:
    print('Bad age for Sue')

try:
    sue.remain = 5
except:
    print("Can't set sue.remain")

try:
    sue.acct = '1234567'
except:
    print('Bad acct for Sue')




class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __set__ calls too
        self.age  = age                          # __X not needed: in descriptor
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    class Name:
        def __get__(self, instance, owner):      # Class names: CardHolder locals
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()
        
    class Age:
        def __get__(self, instance, owner):
            return self.age                             # Use descriptor data
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value
    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:          # Use instance class data
                raise TypeError('invald acct number')
            else:
                self.acct = value
    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age    # Triggers Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')        # Else set allowed here
    remain = Remain()




class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __setattr__ too
        self.age  = age                          # _acct not mangled: name tested
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    def __getattr__(self, name):
        if name == 'acct':                           # On undefined attr fetches
            return self._acct[:-3] + '***'           # name, age, addr are defined
        elif name == 'remain':
            return self.retireage - self.age         # Doesn't trigger __getattr__
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':                           # On all attr assignments
            value = value.lower().replace(' ', '_')  # addr stored directly
        elif name == 'age':                          # acct mangled to _acct
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            name  = '_acct'
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                  # Avoid looping




class CardHolder:
    acctlen = 8                                  # Class data
    retireage = 59.5
    
    def __init__(self, acct, name, age, addr):
        self.acct = acct                         # Instance data
        self.name = name                         # These trigger __setattr__ too
        self.age  = age                          # acct not mangled: name tested
        self.addr = addr                         # addr is not managed
                                                 # remain has no data
    def __getattribute__(self, name):
        superget = object.__getattribute__             # Don't loop: one level up
        if name == 'acct':                             # On all attr fetches
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, name)                # name, age, addr: stored 

    def __setattr__(self, name, value):
        if name == 'name':                             # On all attr assignments
            value = value.lower().replace(' ', '_')    # addr stored directly
        elif name == 'age':
            if value < 0 or value > 150:
                raise ValueError('invalid age')
        elif name == 'acct':
            value = value.replace('-', '')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                     # Avoid loops, orig names



