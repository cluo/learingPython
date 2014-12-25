>>> def fetcher(obj, index):
...     return obj[index]
...



>>> x = 'spam'
>>> fetcher(x, 3)                         # Like x[3]
'm'



>>> fetcher(x, 4)                         # Default handler - shell interface
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in fetcher
IndexError: string index out of range



>>> fetcher(x, 4)                         # Default handler - IDLE GUI interface
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    fetcher(x, 4)
  File "<pyshell#3>", line 2, in fetcher
    return obj[index]
IndexError: string index out of range



>>> try:
...     fetcher(x, 4)
... except IndexError:                    # Catch and recover
...     print('got exception')
...
got exception
>>>



>>> def catcher():
...     try:
...         fetcher(x, 4)
...     except IndexError:
...         print('got exception')
...     print('continuing')
...
>>> catcher()
got exception
continuing
>>>



>>> try:
...     raise IndexError                  # Trigger exception manually
... except IndexError:
...     print('got exception')
...
got exception



>>> raise IndexError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError



>>> assert False, 'Nobody expects the Spanish Inquisition!'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Nobody expects the Spanish Inquisition!



>>> class Bad(Exception):                 # User-defined exception
...     pass
...
>>> def doomed(): 
...     raise Bad()                       # Raise an instance 
...
>>> try:
...     doomed()
... except Bad:                           # Catch class name
...     print('got Bad')
...
got Bad
>>>



>>> try:
...     fetcher(x, 3)
... finally:                              # Termination actions
...     print('after fetch')
...
'm'
after fetch
>>>



fetcher(x, 3)
print('after fetch')



>>> def after():
...     try:
...         fetcher(x, 4)
...     finally:
...         print('after fetch')
...     print('after try?')
...
>>> after()
after fetch
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in after
  File "<stdin>", line 2, in fetcher
IndexError: string index out of range
>>>



>>> def after():
...     try:
...         fetcher(x, 3)
...     finally:
...         print('after fetch')
...     print('after try?')
...
>>> after()
after fetch
after try?
>>>



>>> with open('lumberjack.txt', 'w') as file:        # Always close file on exit
...     file.write('The larch!\n')



doStuff()
{                                 # C program
    if (doFirstThing() == ERROR)  # Detect errors everywhere
        return ERROR;             # even if not handled here
    if (doNextThing() == ERROR)
        return ERROR;
    ...
    return doLastThing();
}

main()
{
    if (doStuff() == ERROR)
        badEnding();
    else
        goodEnding();
}



def doStuff():        # Python code
    doFirstThing()    # We don't care about exceptions here,
    doNextThing()     # so we don’t need to detect them
    ...
    doLastThing()

if __name__ == '__main__':
    try:
        doStuff()     # This is where we care about results,
    except:           # so it's the only place we must check
        badEnding()
    else:
        goodEnding()



