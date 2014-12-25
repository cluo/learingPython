C:\misc> C:\Python25\python
>>> myexc = "My exception string"                 # Were we ever this young?
>>> try:
...     raise myexc
... except myexc:
...     print('caught')
...
caught



### file: classexc.py

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()          # Raise superclass instance
    raise X

def raiser1():
    X = Specific1()        # Raise subclass instance
    raise X

def raiser2():
    X = Specific2()        # Raise different subclass instance
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:        # Match General or any subclass of it
        import sys
        print('caught:', sys.exc_info()[0])



C:\python30> python classexc.py



class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0(): raise General()
def raiser1(): raise Specific1()
def raiser2(): raise Specific2()

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General as X:                     # X is the raised instance
        print('caught:', X.__class__)        # Same as sys.exc_info()[0]



try:
    func()
except (General, Specific1, Specific2):     # Catch any of these
    ...



# mathlib.py

class Divzero(Exception): pass
class Oflow(Exception): pass

def func():
    ...
    raise Divzero()



# client.py

import mathlib

try:
    mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow):
    ...handle and recover...



# mathlib.py

class Divzero(Exception): pass
class Oflow(Exception): pass
class Uflow(Exception): pass



# client.py

try:
    mathlib.func(...)
except (mathlib.Divzero, mathlib.Oflow, mathlib.Uflow):
    ...handle and recover...



# client.py

try:
    mathlib.func(...)
except:                           # Catch everything here
    ...handle and recover...



# mathlib.py

class NumErr(Exception): pass
class Divzero(NumErr): pass
class Oflow(NumErr): pass
...
def func():
    ...
    raise DivZero()



# client.py

import mathlib
...
try:
    mathlib.func(...)
except mathlib.NumErr:
    ...report and recover...



# mathlib.py

...
class Uflow(NumErr): pass



>>> import exceptions     # Python 2.X only
>>> help(exceptions)



try:
    action()
except Exception:
    ...handle all application exceptions...
else:
    ...handle no-exception case...



>>> raise IndexError                    # Same as IndexError(): no arguments
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError

>>> raise IndexError('spam')            # Constructor argument attached, printed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: spam

>>> I = IndexError('spam')              # Available in object attribute
>>> I.args
('spam',)



>>> class E(Exception): pass
...
>>> try:
...    raise E('spam')
... except E as X:
...    print(X, X.args)                 # Displays and saves construtor arguments
...
spam ('spam',)

>>> try:
...    raise E('spam', 'eggs', 'ham')
... except E as X:
...    print(X, X.args)
...
('spam', 'eggs', 'ham') ('spam', 'eggs', 'ham')



>>> class MyBad(Exception): pass
...
>>> try:
...     raise MyBad('Sorry--my mistake!')
... except MyBad as X:
...     print(X)
...
Sorry--my mistake!



>>> raise MyBad('Sorry--my mistake!')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyBad: Sorry--my mistake!



>>> class MyBad(Exception):
...     def __str__(self):
...         return 'Always look on the bright side of life...'
...
>>> try:
...     raise MyBad()
... except MyBad as X:
...     print(X)
...
Always look on the bright side of life...

>>> raise MyBad()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
__main__.MyBad: Always look on the bright side of life...



>>> class FormatError(Exception):
...     def __init__(self, line, file):
...         self.line = line
...         self.file = file
...
>>> def parser():
...     raise FormatError(42, file='spam.txt')     # When error  found
...
>>> try:
...     parser()
... except FormatError as X:
...     print('Error at', X.file, X.line)
...
Error at spam.txt 42



>>> class FormatError(Exception): pass             # Inherited constructor
...
>>> def parser():
...     raise FormatError(42, 'spam.txt')          # No keywords allowed!
...
>>> try:
...     parser()
... except FormatError as X:
...     print('Error at:', X.args[0], X.args[1])   # Not specific to this app
...
Error at: 42 spam.txt



### file: parse.py

class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at', self.file, self.line, file=log)

def parser():
    raise FormatError(40, 'spam.txt')

try:
    parser()
except FormatError as exc:
    exc.logerror()



C:\misc> C:\Python30\python parse.py
C:\misc> type formaterror.txt
Error at spam.txt 40




