### file: nestedexc.py

def action2():
    print(1 + [])            # Generate TypeError

def action1():
    try:
        action2()
    except TypeError:        # Most recent matching try
        print('inner try')

try:
    action1()
except TypeError:            # Here, only if action1 re-raises
    print('outer try')

% python nestexc.py
inner try



try:
    try:
        action2()
    except TypeError:        # Most recent matching try
        print('inner try')
except TypeError:            # Here, only if nested handler re-raises
    print('outer try')



>>> try:
...     try:
...         raise IndexError
...     finally:
...         print('spam')
... finally:
...     print('SPAM')
...
spam
SPAM
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError



### file: except-finally.py

def raise1():  raise IndexError
def noraise(): return
def raise2():  raise SyntaxError

for func in (raise1, noraise, raise2):
    print('\n', func, sep='')
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
    finally:
        print('finally run')



% python except-finally.py



while True:
    try:
        line = input()           # Read line from stdin
    except EOFError:
        break                    # Exit loop at end-of-file
    else:
        ...process next line here...



class Found(Exception): pass

def searcher():
    if ...success...:
        raise Found()
    else:
        return

try:
    searcher()
except Found:                    # Exception if item was found
    ...success...
else:                            # else returned: not found
    ...failure...



class Failure(Exception): pass

def searcher():
    if ...success...:
        return ...founditem...
    else:
        raise Failure()

try:
    item = searcher()
except Failure:
    ...report...
else:
    ...use item here...



myfile = open(r'C:\misc\script', 'w')
try:
    ...process myfile...
finally:
    myfile.close()



with open(r'C:\misc\script', 'w') as myfile:
    ...process myfile...



try:
    ...run program...
except:                         # All uncaught exceptions come here
    import sys
    print('uncaught!', sys.exc_info()[0], sys.exc_info()[1])



import sys
log = open('testlog', 'a')
from testapi import moreTests, runNextTest, testName
def testdriver():
    while moreTests():
        try:
            runNextTest()
        except:
            print('FAILED', testName(), sys.exc_info()[:2], file=log)
        else:
            print('PASSED', testName(), file=log)
testdriver()



try:
    ...
except:
    # sys.exc_info()[0:2] are the exception class and instance



try:
    ...
except General as instance:
    # instance.__class__ is the exception class



try:
    ...
except General as instance:
    # instance.method() does the right thing for this instance



def func():
    try:
        ...                      # IndexError is raised in here
    except:
        ...                      # But everything comes here and dies!
try:
    func()
except IndexError:               # Exception should be processed here
    ...



### file: exiter.py

import sys
def bye():
    sys.exit(40)                 # Crucial error: abort now!
try:
    bye()
except:
    print('got it')              # Oops--we ignored the exit
print('continuing...')


% python exiter.py
got it
continuing...



try:
    bye()
except Exception:                # Won't catch exits, but _will_ catch many others
    ...



mydictionary = {...}
...
try:
    x = myditctionary['spam']    # Oops: misspelled
except:
    x = None                     # Assume we got KeyError
...continue here with x...



try:
    ...
except (MyExcept1, MyExcept2):   # Breaks if you add a MyExcept3
    ...                          # Non-errors
else:
    ...                          # Assumed to be an error



try:
    ...
except SuccessCategoryName:      # OK if I add a myerror3 subclass
    ...                          # Non-errors
else:
    ...                          # Assumed to be an error



