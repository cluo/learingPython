# NOTE: the first few snippets from this chapter are not runnable code,
# but are included in case you wish to expand them into working examples.


try:
    <statements>            # Run this main action first
except <name1>:
    <statements>            # Run if name1 is raised during try block
except (name2, name3):
    <statements>            # Run if any of these exceptions occur
except <name4> as <data>:
    <statements>            # Run if name4 is raised, and get instance raised
except:
    <statements>            # Run for all (other) exceptions raised
else:
    <statements>            # Run if no exception was raised during try block


try:
    action()
except NameError:
    ...
except IndexError:
    ...
except KeyError:
    ...
except (AttributeError, TypeError, SyntaxError):
    ...
else:
    ...


try:
    action()
except NameError:
    ...                   # Handle NameError
except IndexError:
    ...                   # Handle IndexError
except:
    ...                   # Handle all other exceptions
else:
    ...                   # Handle the no-exception case


try:
    action()
except:
    ...                   # Catch all possible exceptions


try:
    action()
except Exception:
    ...                   # Catch all possible exceptions, except exits


try:
    ...run code...
except IndexError:
    ...handle exception...
# Did we get here because the try failed or not?


try:
    ...run code...
except IndexError:
    ...handle exception...
else:
    ...no exception occurred...


try:
    ...run code...
    ...no exception occurred...
except IndexError:
    ...handle exception...




### file: bad.py

def gobad(x, y):
    return x / y

def gosouth(x):
    print(gobad(x, 0))

gosouth(1)



% python bad.py



### file: kaboom.py

def kaboom(x, y):
    print(x + y)               # Trigger TypeError

try:
    kaboom([0,1,2], "spam")
except TypeError:              # Catch and recover here
    print('Hello world!')
print('resuming here')         # Continue here if exception or not



% python kaboom.py
Hello world!
resuming here



try:
    <statements>               # Run this action first
finally:
    <statements>               # Always run this code on the way out



class MyError(Exception): pass

def stuff(file):
    raise MyError()

file = open('data', 'w')     # Open an output file
try:
    stuff(file)              # Raises exception
finally:
    file.close()             # Always close file to flush output buffers
print('not reached')         # Continue here only if no exception



try:                               # Merged form
    main-action
except Exception1:
    handler1
except Exception2:
    handler2
...
else:
    else-block
finally:
    finally-block



try:                               # Format 1
    statements
except [type [as value]]:          # [type [, value]] in Python 2
    statements
[except [type [as value]]:
    statements]*
[else:
    statements]
[finally:
    statements]

try:                               # Format 2
    statements
finally:
    statements



try:                               # Nested equivalent to merged form
    try:
        main-action
    except Exception1:
        handler1
    except Exception2:
        handler2
    ...
    else:
        no-error
finally:
    cleanup



### file: mergedexc.py

sep = '-' * 32 + '\n'
print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')


print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')



c:\misc> C:\Python30\python mergedexc.py



raise <instance>             # Raise instance of class
raise <class>                # Make and raise instance of class
raise                        # Re-raise the most recent exception



raise IndexError             # Class (instance created)
raise IndexError()           # Instance (created in statement)



exc = IndexError()           # Create instance ahead of time
raise exc

excs = [IndexError, TypeError]
raise excs[0]



try:
    ...
except IndexError as X:      # X assigned the raised instance object
   ...



class MyExc(Exception): pass 
...
raise MyExc('spam')          # Exception class with constructor args
...
try:
    ...
except MyExc as X:           # Instance attributes available in handler
    print(X.args)



>>> try:
...     raise IndexError('spam')         # Exceptions remember arguments
... except IndexError:
...     print('propagating')
...     raise                            # Reraise most recent exception
...
propagating
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: spam



raise exception from otherexception


>>> try:
...    1 / 0
... except Exception as E:
...    raise TypeError('Bad!') from E
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: int division or modulo by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
TypeError: Bad!



assert <test>, <data>          # The <data> part is optional


if __debug__:
    if not <test>:
        raise AssertionError(<data>)



### file: asserter.py

def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

% python
>>> import asserter
>>> asserter.f(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "asserter.py", line 2, in f
    assert x < 0, 'x must be negative'
AssertionError: x must be negative



def reciprocal(x):
    assert x != 0              # A useless assert!
    return 1 / x               # Python checks for zero automatically



from __future__ import with_statement


with expression [as variable]:
    with-block



with open(r'C:\misc\data') as myfile:
    for line in myfile:
        print(line)
        ...more code here...



myfile = open(r'C:\misc\data')
try:
    for line in myfile:
        print(line)
        ...more code here...
finally:
    myfile.close()



lock = threading.Lock()
with lock:
    # critical section of code
    ...access shared resources...



with decimal.localcontext() as ctx:
    ctx.prec = 2
    x = decimal.Decimal('1.00') / decimal.Decimal('3.00')



### file: withas.py

class TraceBlock:
    def message(self, arg):
        print('running', arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception!', exc_type)
            return False                                  # Propagate

with TraceBlock() as action:
    action.message('test 1')
    print('reached')

with TraceBlock() as action:
    action.message('test 2')
    raise TypeError
    print('not reached')



% python withas.py



with open('data') as fin, open('res', 'w') as fout:
    for line in fin:
        if 'some key' in line:
            fout.write(line)



with A() as a, B() as b:
    …statements…

with A() as a:
    with B() as b:
        …statements…



