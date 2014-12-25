>>> class FirstClass:               # Define a class object
...     def setdata(self, value):   # Define class methods
...         self.data = value       # self is the instance
...     def display(self):
...         print(self.data)        # self.data: per instance
...



>>> x = FirstClass()                # Make two instances
>>> y = FirstClass()                # Each is a new namespace



>>> x.setdata("King Arthur")        # Call methods: self is x
>>> y.setdata(3.14159)              # Runs: FirstClass.setdata(y, 3.14159)



>>> x.display()                     # self.data differs in each instance
King Arthur
>>> y.display()
3.14159



>>> x.data = "New value"            # Can get/set attributes
>>> x.display()                     # Outside the class too
New value


>>> x.anothername = "spam"          # Can set new attributes here too!



>>> class SecondClass(FirstClass):                   # Inherits setdata
...     def display(self):                           # Changes display
...         print('Current value = "%s"' % self.data)
...



>>> z = SecondClass()
>>> z.setdata(42)           # Finds setdata in FirstClass
>>> z.display()             # Finds overridden method in SecondClass
Current value = "42"



>>> x.display()             # x is still a FirstClass instance (old message)
New value



from modulename import FirstClass           # Copy name into my scope
class SecondClass(FirstClass):              # Use class name directly
    def display(self): ...



import modulename                           # Access the whole module
class SecondClass(modulename.FirstClass):   # Qualify to reference
    def display(self): ...



# food.py
var = 1                                       # food.var
def func():                                   # food.func
    ...
class spam:                                   # food.spam
    ...
class ham:                                    # food.ham
    ...
class eggs:                                   # food.eggs
    ...



class person:
   ...

import person                                 # Import module
x = person.person()                           # Class within module


from person import person                     # Get class from module
x = person()                                  # Use class name


import person                                 # Lowercase for modules
x = person.Person()                           # Uppercase for classes



>>> class ThirdClass(SecondClass):                     # Inherit from SecondClass
...     def __init__(self, value):                     # On "ThirdClass(value)"
...         self.data = value
...     def __add__(self, other):                      # On "self + other"
...         return ThirdClass(self.data + other)
...     def __str__(self):                             # On "print(self)", "str()"
...         return '[ThirdClass: %s]' % self.data
...     def mul(self, other):                          # In-place change: named 
...         self.data *= other
...
>>> a = ThirdClass('abc')           # __init__ called
>>> a.display()                     # Inherited method called
Current value = "abc"
>>> print(a)                        # __str__: returns display string
[ThirdClass: abc]

>>> b = a + 'xyz'                   # __add__: makes a new instance
>>> b.display()                     # b has all ThirdClass methods 
Current value = "abcxyz"
>>> print(b)                        # __str__: returns display string
[ThirdClass: abcxyz]

>>> a.mul(3)                        # mul: changes instance in-place
>>> print(a)
[ThirdClass: abcabcabc]



>>> class rec: pass              # Empty namespace object

>>> rec.name = 'Bob'             # Just objects with attributes
>>> rec.age  = 40

>>> print(rec.name)              # Like a C struct or a record
Bob

>>> x = rec()                    # Instances inherit class names
>>> y = rec()

>>> x.name, y.name               # name is stored on the class only 
('Bob', 'Bob')

>>> x.name = 'Sue'               # But assignment changes x only
>>> rec.name, x.name, y.name
('Bob', 'Sue', 'Bob')

>>> rec.__dict__.keys()
['__module__', 'name', 'age', '__dict__', '__weakref__', '__doc__']

>>> list(x.__dict__.keys())
['name']

>>> list(y.__dict__.keys())                # list() not required in Python 2.6
[]

>>> x.__class__
<class '__main__.rec'>

>>> rec.__bases__                          # () empty tuple in Python 2.6
(<class 'object'>,)

>>> def upperName(self):
...     return self.name.upper()    # Still needs a self

>>> upperName(x)                    # Call as a simple function
'SUE'

>>> rec.method = upperName

>>> x.method()                              # Run  method to process x
'SUE'

>>> y.method()                              # Same, but pass y to self
'BOB'

>>> rec.method(x)                           # Can call through instance or class
'SUE'



>>> rec = {}
>>> rec['name'] = 'mel'                     # Dictionary-based record
>>> rec['age']  = 45
>>> rec['job']  = 'trainer/writer'
>>>
>>> print(rec['name'])
mel



>>> class rec: pass
...
>>> rec.name = 'mel'                        # Class-based record
>>> rec.age  = 45
>>> rec.job  = 'trainer/writer'
>>>
>>> print(rec.age)
40



>>> class rec: pass
...
>>> pers1 = rec()                           # Instance-based records
>>> pers1.name = 'mel'
>>> pers1.job  = 'trainer'
>>> pers1.age   = 40
>>>
>>> pers2 = rec()
>>> pers2.name = 'vls'
>>> pers2.job  = 'developer'
>>>
>>> pers1.name, pers2.name
('mel', 'vls')



>>> class Person:
...     def __init__(self, name, job):      # Class = Data + Logic
...         self.name = name
...         self.job  = job
...     def info(self):
...         return (self.name, self.job)
...
>>> rec1 = Person('mel', 'trainer')
>>> rec2 = Person('vls', 'developer')
>>>
>>> rec1.job, rec2.info()
('trainer', ('vls', 'developer'))






