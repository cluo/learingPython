>>> print('Hello world!')
Hello world!
>>> print(2 ** 8)
256



>>> lumberjack = 'okay'
>>> lumberjack
'okay'
>>> 2 ** 8
256



>>> 'Spam!' * 8        # <== Learning by trying
'Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!'



>>> X                  # <== Making mistakes
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'X' is not defined



>>> import os
>>> os.getcwd()        # <== Testing on the fly
'c:\\Python30'



>>> for x in 'spam':
...     print(x)       # <== Press Enter twice here to make this loop run
...



>>> for x in 'spam':
...     print(x)       # <== Need to press Enter twice before a new statement
... print('done')
File "<stdin>", line 3
 print('done')
     ^
SyntaxError: invalid syntax



### file: script1.py

# A first Python script
import sys                # Load a library module
print(sys.platform)
print(2 ** 100)           # Raise 2 to a power
x = 'Spam!'
print(x * 8)              # String repetition



### file: brian

#!/usr/local/bin/python                      # or: #!/usr/bin/env python
print('The Bright Side ' + 'of Life...')     # + means concatenate for strings



### file: script1.py (modified)

# A first Python script
import sys                # Load a library module
print(sys.platform)
print(2 ** 100)           # Raise 2 to a power  (later changed to 2 ** 16)
x = 'Spam!'
print(x * 8)              # String repetition
input()                   # <== ADDED           (use raw_input() in Python 2.X)



#### file: myfile.py

title = "The Meaning of Life"



>>> import myfile               # Run file; load module as a whole
>>> print(myfile.title)         # Use its attribute names: '.' to qualify
The Meaning of Life

>>> from myfile import title    # Run file; copy its names
>>> print(title)                # Use name directly: no need to qualify
The Meaning of Life



### file: threenames.py

a = 'dead'         # Define three attributes
b = 'parrot'       # Exported to other files
c = 'sketch'
print(a, b, c)     # Also used in this file



>>> import threenames                     # Grab the whole module
dead parrot sketch
>>>
>>> threenames.b, threenames.c
('parrot', 'sketch')
>>>
>>> from threenames import a, b, c        # Copy multiple names
>>> b, c
('parrot', 'sketch')

>>> dir(threenames)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'a', 'b', 'c']



>>> exec(open('script1.py').read())
win32
65536
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!

...change script1.py in a text edit window...

>>> exec(open('script1.py').read())
win32
4294967296
Spam!Spam!Spam!Spam!Spam!Spam!Spam!Spam!

>>> x = 999
>>> exec(open('script1.py').read())   # Code run in this namespace by default
...same outout...
>>> x                                 # Its assignments can overwrite names here
'Spam!'



### C language code (embedding)

#include <Python.h>
...
Py_Initialize();                                    // This is C, not Python
PyRun_SimpleString("x = 'brave ' + 'sir robin'");   // But it runs Python code



L = [1, 2]        # Make a 2-item list
L.append(L)       # Append L as a single item to itself
L                 # Print L

