### file: b.py

def spam(text):
    print(text, 'spam')



### file: a.py

import b
b.spam('gumby')


# NOTE: described but not shown explicitly in the book:
C:\misc> a.py
gumby spam



### fileL: C:\Python30\pydirs.pth
c:\pycode\utilities
d:\pycode\package1



>>> import sys
>>> sys.path
['', 'C:\\users', 'C:\\Windows\\system32\\python30.zip', 'c:\\Python30\\DLLs', 
'c:\\Python30\\lib', 'c:\\Python30\\lib\\plat-win', 'c:\\Python30', 
'C:\\Users\\Mark', 'c:\\Python30\\lib\\site-packages']





