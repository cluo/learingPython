### three files, as labeled

# dir1\__init__.py
print('dir1 init')
x = 1

# dir1\dir2\__init__.py
print('dir2 init')
y = 2

# dir1\dir2\mod.py
print('in mod.py')
z = 3



>>> import dir1.dir2.mod      # First imports run init files
dir1 init
dir2 init
in mod.py
>>>
>>> import dir1.dir2.mod      # Later imports do not
>>>
>>> from imp import reload    # Needed in 3.0
>>> reload(dir1)
dir1 init
<module 'dir1' from 'dir1\__init__.pyc'>
>>>
>>> reload(dir1.dir2)
dir2 init
<module 'dir1.dir2' from 'dir1\dir2\__init__.pyc'>



>>> dir1
<module 'dir1' from 'dir1\__init__.pyc'>
>>> dir1.dir2
<module 'dir1.dir2' from 'dir1\dir2\__init__.pyc'>
>>> dir1.dir2.mod
<module 'dir1.dir2.mod' from 'dir1\dir2\mod.pyc'>



>>> dir1.x
1
>>> dir1.dir2.y
2
>>> dir1.dir2.mod.z
3



>>> dir2.mod
NameError: name 'dir2' is not defined
>>> mod.z
NameError: name 'mod' is not defined



% python
>>> from dir1.dir2 import mod      # Code path here only
dir1 init
dir2 init
in mod.py
>>> mod.z                          # Don't repeat path
3
>>> from dir1.dir2.mod import z
>>> z
3
>>> import dir1.dir2.mod as mod    # Use shorter name (see Chapter 24)
>>> mod.z
3



import system1.utilities
import system2.utilities
system1.utilities.function('spam')
system2.utilities.function('eggs')



from . import spam                        # Relative to this package
from .spam import name
from __future__ import  absolute_import   # Required until 2.7?
import string                             # Skip this package's version
from . import string                      # Searches this package only

from .string import name1, name2            # Imports names from mypkg.string
from . import string                        # Imports mypkg.string
from .. import string                       # Imports string sibling of mypkg



import string                          # Imports string outside package
from string import name                # Imports name from string outside package
from . import string                   # Imports mypkg.string (relative)
from .string import name1, name2       # Imports names from mypkg.string
from .. import spam                    # Imports a sibling of mypkg
from . import D                        # Imports A.B.D     (. means A.B)
from .. import E                       # Imports A.E       (.. means A)

from .D import X                       # Imports A.B.D.X   (. means A.B)
from ..E import X                      # Imports A.E.X     (.. means A)



from mypkg import string                    # Imports mypkg.string (absolute)
from system.section.mypkg import string     # system container on sys.path only
from . import string                        # Relative import syntax




### In the following, filenames are provided in comments



C:\test> c:\Python30\python
>>> import string
>>> string
<module 'string' from 'c:\Python30\lib\string.py'>



# test\string.py
print('string' * 8)

C:\test> c:\Python30\python
>>> import string
stringstringstringstringstringstringstringstring
>>> string
<module 'string' from 'string.py'>



>>> from . import string
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: Attempted relative import in non-package



# test\main.py
import string
print(string)

C:\test> C:\python30\python main.py                   # Same results in 2.6
stringstringstringstringstringstringstringstring
<module 'string' from 'C:\test\string.py'>



C:\test> del string*
C:\test> mkdir pkg

# test\pkg\spam.py
import eggs                    # Works in 2.6 but not 3.0!
print(eggs.X)

# test\pkg\eggs.py
X = 99999
import string
print(string)



C:\test> c:\Python26\python
>>> import pkg.spam
<module 'string' from 'c:\Python26\lib\string.pyc'>
99999

C:\test> c:\Python30\python
>>> import pkg.spam
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "pkg\spam.py", line 1, in <module>
    import eggs
ImportError: No module named eggs



# test\pkg\spam.py
from . import eggs             # Use package relative import in 2.6 or 3.0
print(eggs.X)

# test\pkg\eggs.py
X = 99999
import string
print(string)

C:\test> c:\Python26\python
>>> import pkg.spam
<module 'string' from 'c:\Python26\lib\string.pyc'>
99999

C:\test> c:\Python30\python
>>> import pkg.spam
<module 'string' from 'c:\Python30\lib\string.py'>
99999



# test\string.py
print('string' * 8)

# test\pkg\spam.py
from . import eggs
print(eggs.X)

# test\pkg\eggs.py
X = 99999
import string                  # Gets string in CWD, not Python lib!
print(string)

C:\test> c:\Python30\python    # Same result in 2.6
>>> import pkg.spam
stringstringstringstringstringstringstringstring
<module 'string' from 'string.py'>
99999



C:\test> del string*

# test\pkg\spam.py
import string                  # Relative in 2.6, absolute in 3.0
print(string)

# test\pkg\string.py
print('Ni' * 8)



C:\test> c:\Python30\python
>>> import pkg.spam
<module 'string' from 'c:\Python30\lib\string.py'>

C:\test> c:\Python26\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>



# test\pkg\spam.py
from . import string           # Relative in both 2.6 and 3.0
print(string)

# test\pkg\string.py
print('Ni' * 8)

C:\test> c:\Python30\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>

C:\test> c:\Python26\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>



# test\pkg\spam.py
from . import string           # Fails if no string.py here!

C:\test> C:\python30\python
>>> import pkg.spam
...text omitted...
ImportError: cannot import name string



# test\string.py
print('string' * 8)

# test\pkg\spam.py
from . import string           # Relative in both 2.6 and 3.0
print(string)

# test\pkg\string.py
print('Ni' * 8)



C:\test> c:\Python30\python    # Same result in 2.6
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>



# test\string.py
print('string' * 8)

# test\pkg\spam.py
import string            # Relative in 2.6, "absolute" in 3.0: CWD!
print(string)

# test\pkg\string.py
print('Ni' * 8)

C:\test> c:\Python30\python
>>> import pkg.spam
stringstringstringstringstringstringstringstring
<module 'string' from 'string.py'>

C:\test> c:\Python26\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.pyc'>



from email.message import Message
from tkinter.filedialog import askopenfilename
from http.server import CGIHTTPRequestHandler



