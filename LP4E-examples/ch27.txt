# NOTE: this chapter repeatedly modifies the same file, person.py; 
# changed lines are highlighted in the text; here, all of this file's
# extensions are colected



# File person.py (start)

class Person:



# Add record field initialization

class Person:
    def __init__(self, name, job, pay):      # Constructor takes 3 arguments 
        self.name = name                     # Fill out fields when created 
        self.job  = job                      # self is the new instance object
        self.pay  = pay



# Add defaults for constructor arguments

class Person:
    def __init__(self, name, job=None, pay=0):         # Normal function args
        self.name = name
        self.job  = job
        self.pay  = pay



# Add incremental self-test code

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

bob = Person('Bob Smith')                         # Test the class
sue = Person('Sue Jones', job='dev', pay=100000)  # Runs __init__ automatically
print(bob.name, bob.pay)                          # Fetch attached attributes
print(sue.name, sue.pay)                          # sue’s and bob’s attrs differ



C:\misc> person.py
Bob Smith 0
Sue Jones 100000



# Allow this file to be imported as well as run/tested

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

if __name__ == '__main__':                  # When run for testing only
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)



C:\misc> person.py
Bob Smith 0
Sue Jones 100000

c:\misc> python
Python 3.0.1 (r301:69561, Feb 13 2009, 20:04:18) ...
>>> import person
>>>



c:\misc> c:\python26\python person.py
('Bob Smith', 0)
('Sue Jones', 100000)


print('{0} {1}'.format(bob.name, bob.pay))    # New format method
print('%s %s' % (bob.name, bob.pay))          # Format expression



>>> name = 'Bob Smith'      # Simple string, outside class
>>> name.split()            # Extract last name
['Bob', 'Smith']
>>> name.split()[-1]        # Or [1], if always just two parts
'Smith'



>>> pay = 100000            # Simple variable, outside class
>>> pay *= 1.10             # Give a 10% raise
>>> print(pay)              # Or: pay = pay * 1.10, if you like to type
110000.0                    # Or: pay = pay + (pay * .10), if you _really_ do!



# Process embedded built-in types: strings, mutability

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.name.split()[-1])            # Extract object's last name
    sue.pay *= 1.10                        # Give this object a raise
    print(sue.pay)



# Add methods to encapsulate operations for maintainability

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):                               # Behavior methods
        return self.name.split()[-1]                  # self is implied subject
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))      # Must change here only

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())             # Use the new methods
    sue.giveRaise(.10)                                # instead of hardcoding
    print(sue.pay)



# Add __str__ overload method for printing objects

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):                                         # Added method
        return '[Person: %s, %s]' % (self.name, self.pay)      # String to print

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)



class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus))   # Bad: cut-and-paste

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)            # Good: augment original



# Add customization of one behavior in a subclass

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

class Manager(Person):
    def giveRaise(self, percent, bonus=.10):           # Redefine at this level
        Person.giveRaise(self, percent + bonus)        # Call Person's version
     
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'mgr', 50000)           # Make a Manager: __init__
    tom.giveRaise(.10)                                 # Runs custom version
    print(tom.lastName())                              # Runs inherited method
    print(tom)                                         # Runs inherited __str__



if __name__ == '__main__':
    ...
    print('--All three--')
    for object in (bob, sue, tom):            # Process objects generically
        object.giveRaise(.10)                 # Run this object’s giveRaise
        print(object)                         # Run the common __str__



class Person: 
    def lastName(self): ...
    def giveRaise(self): ...
    def __str__(self): ...

class Manager(Person):                        # Inherit
    def giveRaise(self, ...): ...             # Customize
    def someThingElse(self, ...): ...         # Extend

tom = Manager()
tom.lastName()                                # Inherited verbatim
tom.giveRaise()                               # Customized version
tom.someThingElse()                           # Extension here
print(tom)                                    # Inherited overload method



# Add customization of constructor in a subclass

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

class Manager(Person):
    def __init__(self, name, pay):                     # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)        # Run original with 'mgr'
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
     
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)                   # Job name not needed:
    tom.giveRaise(.10)                                  # Implied/set by class
    print(tom.lastName())
    print(tom)



# Embedding-based Manager alternative

class Person: 
    ...same...

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
    ...same...



# Aggregate embedded objects into a composite

...
bob = Person(...)
sue = Person(...)
tom = Manager(...)

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members: 
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members: 
            print(person)

development = Department(bob, sue)          # Embed objects in a composite
development.addMember(tom)
development.giveRaises(.10)                 # Runs embedded objects' giveRaise 
development.showAll()                       # Runs embedded objects' __str__s



>>> from person import Person
>>> bob = Person('Bob Smith')
>>> print(bob)                                 # Show bob's __str__
[Person: Bob Smith, 0]

>>> bob.__class__                              # Show bob's class and its name
<class 'person.Person'>
>>> bob.__class__.__name__
'Person'

>>> list(bob.__dict__.keys())                  # Attributes are really dict keys
['pay', 'job', 'name']                         # Use list() to force list in 3.0

>>> for key in bob.__dict__:
        print(key, '=>', bob.__dict__[key])    # Index manually
	
pay => 0
job => None
name => Bob Smith

>>> for key in bob.__dict__:
        print(key, '=>', getattr(bob, key))    # obj.attr, but attr is a var
	
pay => 0
job => None
name => Bob Smith



### File: classtools.py (new)

"Assorted class utilities and tools"

class AttrDisplay:
    """
    Provides an inheritable print overload method that displays 
    instances with their class names and a name=value pair for 
    each attribute stored on the instance itself (but not attrs 
    inherited from its classes). Can be mixed into any class, 
    and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':
    class TopTest(AttrDisplay):
        count = 0
        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass
            
    X, Y = TopTest(), SubTest()
    print(X)                         # Show all instance attrs
    print(Y)                         # Show lowest class name



C:\misc> classtools.py
[TopTest: attr1=0, attr2=1]
[SubTest: attr1=2, attr2=3]



>>> from person import Person
>>> bob = Person('Bob Smith')

# In Python 2.6:

>>> bob.__dict__.keys()                 # Instance attrs only
['pay', 'job', 'name']

>>> dir(bob)                            # + inherited attrs in classes
['__doc__', '__init__', '__module__', '__str__', 'giveRaise', 'job', 
'lastName', 'name', 'pay']

# In Python 3.0:

>>> list(bob.__dict__.keys())           # 3.0 keys() is a view, not a list
['pay', 'job', 'name']

>>> dir(bob)                            # 3.0 includes class type methods
['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
...more lines omitted...
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
'giveRaise', 'job', 'lastName', 'name', 'pay']



    class TopTest(AttrDisplay):
        ....
        def gatherAttrs(self):         # Replaces method in AttrDisplay!
            return 'Spam'



# File person.py (final)

from classtools import AttrDisplay                  # Use generic display tool

class Person(AttrDisplay):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):                             # Assumes last is last
        return self.name.split()[-1]
    def giveRaise(self, percent):                   # Percent must be 0..1
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)
     
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)



C:\misc> person.py
[Person: job=None, name=Bob Smith, pay=0]
[Person: job=dev, name=Sue Jones, pay=100000]
Smith Jones
[Person: job=dev, name=Sue Jones, pay=110000]
Jones
[Manager: job=mgr, name=Tom Jones, pay=60000]



# File makedb.py: store Person objects on a shelve database

from person import Person, Manager              # Load our classes
bob = Person('Bob Smith')                       # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')                    # Filename where objects are stored
for object in (bob, sue, tom):                  # Use object's name attr as key
    db[object.name] = object                    # Store object on shelve by key
db.close()                                      # Close after making changes



C:\misc> makedb.py



# Directory listing module: verify files are present

>>> import glob
>>> glob.glob('person*')
['person.py', 'person.pyc', 'persondb.bak', 'persondb.dat', 'persondb.dir']

# Type the file: text mode for string, binary mode for bytes

>>> print(open('persondb.dir').read())
'Tom Jones', (1024, 91)
...more omitted...

>>> print(open('persondb.dat', 'rb').read())
b'\x80\x03cperson\nPerson\nq\x00)\x81q\x01}q\x02(X\x03\x00\x00\x00payq\x03K...
...more omitted...



>>> import shelve
>>> db = shelve.open('persondb')                # Reopen the shelve
  
>>> len(db)                                     # Three 'records' stored
3
>>> list(db.keys())                             # keys() is the index
['Tom Jones', 'Sue Jones', 'Bob Smith']         # list() to make a list in 3.0
 
>>> bob = db['Bob Smith']                       # Fetch bob by key
>>> print(bob)                                  # Runs __str__ from AttrDisplay
[Person: job=None, name=Bob Smith, pay=0]
 
>>> bob.lastName()                              # Runs lastName from Person
'Smith'
 
>>> for key in db:                              # Iterate, fetch, print
        print(key, '=>', db[key])

Tom Jones => [Manager: job=mgr, name=Tom Jones, pay=50000]
Sue Jones => [Person: job=dev, name=Sue Jones, pay=100000]
Bob Smith => [Person: job=None, name=Bob Smith, pay=0]

>>> for key in sorted(db):                           
        print(key, '=>', db[key])               # Iterate by sorted keys

Bob Smith => [Person: job=None, name=Bob Smith, pay=0]
Sue Jones => [Person: job=dev, name=Sue Jones, pay=100000]
Tom Jones => [Manager: job=mgr, name=Tom Jones, pay=50000]



# File updatedb.py: update Person object on database

import shelve
db = shelve.open('persondb')               # Reopen shelve with same filename

for key in sorted(db):                     # Iterate to display database objects
    print(key, '\t=>', db[key])            # Prints with custom format

sue = db['Sue Jones']                      # Index by key to fetch
sue.giveRaise(.10)                         # Update in memory using class method
db['Sue Jones'] = sue                      # Assign to key to update in shelve
db.close()                                 # Close after making changes



c:\misc> updatedb.py
Bob Smith       => [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       => [Person: job=dev, name=Sue Jones, pay=100000]
Tom Jones       => [Manager: job=mgr, name=Tom Jones, pay=50000]

c:\misc> updatedb.py
Bob Smith       => [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       => [Person: job=dev, name=Sue Jones, pay=110000]
Tom Jones       => [Manager: job=mgr, name=Tom Jones, pay=50000]

c:\misc> updatedb.py
Bob Smith       => [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       => [Person: job=dev, name=Sue Jones, pay=121000]
Tom Jones       => [Manager: job=mgr, name=Tom Jones, pay=50000]

c:\misc> updatedb.py
Bob Smith       => [Person: job=None, name=Bob Smith, pay=0]
Sue Jones       => [Person: job=dev, name=Sue Jones, pay=133100]
Tom Jones       => [Manager: job=mgr, name=Tom Jones, pay=50000]



c:\misc> python
>>> import shelve
>>> db = shelve.open('persondb')             # Reopen database 
>>> rec = db['Sue Jones']                    # Fetch object by key
>>> print(rec)
[Person: job=dev, name=Sue Jones, pay=146410]
>>> rec.lastName()
'Jones'
>>> rec.pay
146410



