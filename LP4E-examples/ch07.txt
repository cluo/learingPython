>>> 'shrubbery', "shrubbery"
('shrubbery', 'shrubbery')

>>> 'knight"s', "knight's"
('knight"s', "knight's")

>>> title = "Meaning " 'of' " Life"     # Implicit concatenation
>>> title
'Meaning of Life'

>>> 'knight\'s', "knight\"s"
("knight's", 'knight"s')



>>> s = 'a\nb\tc'

>>> s
'a\nb\tc'
>>> print(s)
a
b c

>>> len(s)
5



>>> s = 'a\0b\0c'
>>> s
'a\x00b\x00c'
>>> len(s)
5

>>> s = '\001\002\x03'
>>> s
'\x01\x02\x03'
>>> len(s)
3

>>> S = "s\tp\na\x00m"
>>> S
's\tp\na\x00m'
>>> len(S)
7
>>> print(S)
s p
a m

>>> x = "C:\py\code"          # Keeps \ literally
>>> x
'C:\\py\\code'
>>> len(x)
10



myfile = open('C:\new\text.dat', 'w')

myfile = open(r'C:\new\text.dat', 'w')

>>> path = r'C:\new\text.dat'
>>> path                        # Show as Python code
'C:\\new\\text.dat'
>>> print(path)                 # User-friendly format
C:\new\text.dat
>>> len(path)                   # String length
15



>>> mantra = """Always look
... on the bright
... side of life."""
>>>
>>> mantra
'Always look\n on the bright\nside of life.'

>>> print(mantra)
Always look
 on the bright
side of life.


X = 1
"""
import os                   # Disable this code temporarily
print(os.getcwd())
"""
Y = 2



>>> len('abc')           # Length: number of items
3
>>> 'abc' + 'def'        # Concatenation: a new string
'abcdef'
>>> 'Ni!' * 4            # Repetition: like "Ni!" + "Ni!" + ...
'Ni!Ni!Ni!Ni!'

>>> print('------- ...more... ---')       # 80 dashes, the hard way
>>> print('-' * 80)

>>> myjob = "hacker"
>>> for c in myjob: print(c, end=' ')     # Step through items
...
h a c k e r

>>> "k" in myjob              # Found
True
>>> "z" in myjob              # Not found
False
>>> 'spam' in 'abcspamdef'    # Substring search, no position returned
True


>>> S = 'spam'
>>> S[0], S[-2]               # Indexing from front or end
('s', 'a')
>>> S[1:3], S[1:], S[:-1]     # Slicing: extract a section
('pa', 'pam', 'spa')


>>> S = 'abcdefghijklmnop'
>>> S[1:10:2]
'bdfhj'
>>> S[::2]
'acegikmo'

>>> S = 'hello'
>>> S[::-1]
'olleh'

>>> S = 'abcedfg'
>>> S[5:1:-1]
'fdec'

>>> 'spam'[1:3]              # Slicing syntax
'pa'
>>> 'spam'[slice(1, 3)]      # Slice objects
'pa'
>>> 'spam'[::-1]
'maps'
>>> 'spam'[slice(None, None, -1)]
'maps'



# File echo.py
import sys
print(sys.argv)

% python echo.py -a -b -c
['echo.py', '-a', '-b', '-c']



>>> "42" + 1
TypeError: cannot concatenate 'str' and 'int' objects

>>> int("42"), str(42)      # Convert from/to string
(42, '42')
>>> repr(42)                # Convert to as-code string
'42'

>>> print(str('spam'), repr('spam'))
('spam', "'spam'")

>>> S = "42"
>>> I = 1
>>> S + I
TypeError: cannot concatenate 'str' and 'int' objects

>>> int(S) + I         # Force addition
43

>>> S + str(I)         # Force concatenation
'421'

>>> str(3.1415), float("1.5")
('3.1415', 1.5)
>>> text = "1.234E-10"
>>> float(text)
1.2340000000000001e-010



>>> ord('s')
115
>>> chr(115)
's'

>>> S = '5'
>>> S = chr(ord(S) + 1)
>>> S
'6'
>>> S = chr(ord(S) + 1)
>>> S
'7'

>>> int('5')
5
>>> ord('5') - ord('0')
5

>>> B = '1101'              # Convert binary digits to integer with ord
>>> I = 0
>>> while B != '':
...     I = I * 2 + (ord(B[0]) - ord('0'))
...     B = B[1:]
...
>>> I
13

>>> int('1101', 2)      # Convert binary to integer: built-in
13
>>> bin(13)             # Convert integer to binary
'0b1101'



>>> S = 'spam'
>>> S[0] = "x"
Raises an error!


>>> S = S + 'SPAM!'    # To change a string, make a new one
>>> S
'spamSPAM!'
>>> S = S[:4] + 'Burger' + S[-1]
>>> S
'spamBurger!'


>>> S = 'splot'
>>> S = S.replace('pl', 'pamal')
>>> S
'spamalot'


>>> 'That is %d %s bird!' % (1, 'dead')           # Format expression
That is 1 dead bird!
>>> 'That is {0} {1} bird!'.format(1, 'dead')     # Format method in 2.6 and 3.0
'That is 1 dead bird!'



>>> S = 'spammy'
>>> S = S[:3] + 'xx' + S[5:]
>>> S
'spaxxy'


>>> S = 'spammy'
>>> S = S.replace('mm', 'xx')
>>> S
'spaxxy'


>>> 'aa$bb$cc$dd'.replace('$', 'SPAM')
'aaSPAMbbSPAMccSPAMdd


>>> S = 'xxxxSPAMxxxxSPAMxxxx'
>>> where = S.find('SPAM')                # Search for position
>>> where                                 # Occurs at offset 4
4
>>> S = S[:where] + 'EGGS' + S[(where+4):]
>>> S
'xxxxEGGSxxxxSPAMxxxx'


>>> S = 'xxxxSPAMxxxxSPAMxxxx'
>>> S.replace('SPAM', 'EGGS')         # Replace all
'xxxxEGGSxxxxEGGSxxxx'
>>> S.replace('SPAM', 'EGGS', 1)      # Replace one
'xxxxEGGSxxxxSPAMxxxx'


>>> S = 'spammy'
>>> L = list(S)
>>> L
['s', 'p', 'a', 'm', 'm', 'y']

>>> L[3] = 'x'                         # Works for lists, not strings
>>> L[4] = 'x'
>>> L
['s', 'p', 'a', 'x', 'x', 'y']

>>> S = ''.join(L)
>>> S
'spaxxy'


>>> 'SPAM'.join(['eggs', 'sausage', 'ham', 'toast'])
'eggsSPAMsausageSPAMhamSPAMtoast'




>>> line = 'aaa bbb ccc'
>>> col1 = line[0:3]
>>> col3 = line[8:]
>>> col1
'aaa'
>>> col3
'ccc'

>>> line = 'aaa bbb ccc'
>>> cols = line.split()
>>> cols
['aaa', 'bbb', 'ccc']

>>> line = 'bob,hacker,40'
>>> line.split(',')
['bob', 'hacker', '40']

>>> line = "i'mSPAMaSPAMlumberjack"
>>> line.split("SPAM")
["i'm", 'a', 'lumberjack']



>>> line = "The knights who say Ni!\n"
>>> line.rstrip()
'The knights who say Ni!'
>>> line.upper()
'THE KNIGHTS WHO SAY NI!\n'
>>> line.isalpha()
False
>>> line.endswith('Ni!\n')
True
>>> line.startswith('The')
True



>>> line
'The knights who say Ni!\n'
>>> line.find('Ni') != -1            # Search via method call or expression
True
>>> 'Ni' in line
True

>>> sub = 'Ni!\n'
>>> line.endswith(sub)               # End test via method call or slice
True
>>> line[-len(sub):] == sub
True



>>> S = 'a+b+c+'

>>> x = S.replace('+', 'spam')
>>> x
'aspambspamcspam

>>> import string
>>> y = string.replace(S, '+', 'spam')
>>> y
'aspambspamcspam'



# NOTE: ths spacing in the output of some of the following
# tests may differ from what is shown in the book, and what
# appears when run; cut-and-paste lost some whitespace here...



>>> 'That is %d %s bird!' % (1, 'dead')      # Format expression
That is 1 dead bird!

# ADDED: the new method equivalent
>>> 'That is {0:d} {1:s} bird!'.format(1, 'dead')
That is 1 dead bird!

>>> exclamation = "Ni"
>>> "The knights who say %s!" % exclamation
'The knights who say Ni!'

>>> "%d %s %d you" % (1, 'spam', 4)
'1 spam 4 you'

>>> "%s -- %s -- %s" % (42, 3.14159, [1, 2, 3])
'42 -- 3.14159 -- [1, 2, 3]'



>>> x = 1234
>>> res = "integers: ...%d...%-6d...%06d" % (x, x, x)
>>> res
'integers: ...1234...1234 ...001234'

>>> x = 1.23456789
>>> x
1.2345678899999999

>>> '%e | %f | %g' % (x, x, x)
'1.234568e+00 | 1.234568 | 1.23457'

>>> '%E' % x
'1.234568E+00'

>>> '%-6.2f | %05.2f | %+06.1f' % (x, x, x)
'1.23 | 01.23 | +001.2'

>>> "%s" % x, str(x)
('1.23456789', '1.23456789')

>>> '%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0)
'0.333333, 0.33, 0.3333'



>>> "%(n)d %(x)s" % {"n":1, "x":"spam"}
'1 spam'

>>> reply = """                               # Template with substitution targets
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
>>> values = {'name': 'Bob', 'age': 40}       # Build up values to substitute
>>> print(reply % values)                     # Perform substitutions

Greetings...
Hello Bob!
Your age squared is 40


>>> food = 'spam'
>>> age = 40
>>> vars()
{'food': 'spam', 'age': 40, ...many more... }

>>> "%(age)d %(food)s" % vars()
'40 spam'


>>> template = '{0}, {1} and {2}'                    # By position
>>> template.format('spam', 'ham', 'eggs')
'spam, ham and eggs'

>>> template = '{motto}, {pork} and {food}'          # By keyword
>>> template.format(motto='spam', pork='ham', food='eggs')
'spam, ham and eggs'

>>> template = '{motto}, {0} and {food}'             # By both
>>> template.format('ham', motto='spam', food='eggs')
'spam, ham and eggs'

>>> '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
'3.14, 42 and [1, 2]'

>>> X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
>>> X
'3.14, 42 and [1, 2]'

>>> X.split(' and ')
['3.14, 42', '[1, 2]']

>>> Y = X.replace('and', 'but under no circumstances')
>>> Y
'3.14, 42 but under no circumstances [1, 2]'



>>> import sys
>>> 'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'})
'My laptop runs win32'

>>> 'My {config[spam]} runs {sys.platform}'.format(sys=sys, 
                                                   config={'spam': 'laptop'})
'My laptop runs win32'



>>> somelist = list('SPAM')
>>> somelist
['S', 'P', 'A', 'M']

>>> 'first={0[0]}, third={0[2]}'.format(somelist)
'first=S, third=A'

>>> 'first={0}, last={1}'.format(somelist[0], somelist[-1])    # [-1] fails in fmt
'first=S, last=M'

>>> parts = somelist[0], somelist[-1], somelist[1:3]           # [1:3] fails in fmt
>>> 'first={0}, last={1}, middle={2}'.format(*parts)
"first=S, last=M, middle=['P', 'A']"



>>> '{0:10} = {1:10}'.format('spam', 123.4567)
'spam = 123.457'

>>> '{0:>10} = {1:<10}'.format('spam', 123.4567)
' spam = 123.457 '

>>> '{0.platform:>10} = {1[item]:<10}'.format(sys, dict(item='laptop'))
' win32 = laptop



>>> '{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159)
'3.141590e+00, 3.142e+00, 3.14159'

>>> '{0:f}, {1:.2f}, {2:06.2f}'.format(3.14159, 3.14159, 3.14159)
'3.141590, 3.14, 003.14'



>>> '{0:X}, {1:o}, {2:b}'.format(255, 255, 255)    # Hex, octal, binary
'FF, 377, 11111111'

>>> bin(255), int('11111111', 2), 0b11111111       # Other to/from binary
('0b11111111', 255, 255)

>>> hex(255), int('FF', 16), 0xFF                  # Other to/from hex
('0xff', 255, 255)

>>> oct(255), int('377', 8), 0o377, 0377           # Other to/from octal
('0377', 255, 255, 255)                            # 0377 works in 2.6, not 3.0!



>>> '{0:.2f}'.format(1 / 3.0)                 # Parameters hardcoded
'0.33'
>>> '%.2f' % (1 / 3.0)
'0.33'

>>> '{0:.{1}f}'.format(1 / 3.0, 4)            # Take value from arguments
'0.3333'
>>> '%.*f' % (4, 1 / 3.0)                     # Ditto for expression
'0.3333'



>>> '{0:.2f}'.format(1.2345)     # String method
'1.23'
>>> format(1.2345, '.2f')        # Built-in function
'1.23'
>>> '%.2f' % 1.2345              # Expression
'1.23'



print('%s=%s' % ('spam', 42))                # 2.X+ format expression

print('{0}={1}'.format('spam', 42))          # 3.0 (and 2.6) format method



# The basics: with % instead of format()

>>> template = '%s, %s, %s'
>>> template % ('spam', 'ham', 'eggs')                        # By position
'spam, ham, eggs'

>>> template = '%(motto)s, %(pork)s and %(food)s'
>>> template % dict(motto='spam', pork='ham', food='eggs')    # By key
'spam, ham and eggs'

>>> '%s, %s and %s' % (3.14, 42, [1, 2])                      # Arbitrary types
'3.14, 42 and [1, 2]'


# Adding keys, attributes, and offsets

>>> 'My %(spam)s runs %(platform)s' % {'spam': 'laptop', 'platform': sys.platform}
'My laptop runs win32'

>>> 'My %(spam)s runs %(platform)s' % dict(spam='laptop', platform=sys.platform)
'My laptop runs win32'

>>> somelist = list('SPAM')
>>> parts = somelist[0], somelist[-1], somelist[1:3]
>>> 'first=%s, last=%s, middle=%s' % parts
"first=S, last=M, middle=['P', 'A']"


# Adding specific formatting

>>> '%-10s = %10s' % ('spam', 123.4567)
'spam = 123.4567'

>>> '%10s = %-10s' % ('spam', 123.4567)
' spam = 123.4567 '

>>> '%(plat)10s = %(item)-10s' % dict(plat=sys.platform, item='laptop')
' win32 = laptop '

# Floating-point numbers

>>> '%e, %.3e, %g' % (3.14159, 3.14159, 3.14159)
'3.141590e+00, 3.142e+00, 3.14159'

>>> '%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159)
'3.141590, 3.14, 003.14'

# Hex and octal, but not binary
>>> '%x, %o' % (255, 255)
'ff, 377'



# Hardcoded references in both

>>> import sys
>>> 'My {1[spam]:<8} runs {0.platform:>8}'.format(sys, {'spam': 'laptop'})
'My laptop   runs    win32'

>>> 'My %(spam)-8s runs %(plat)8s' % dict(spam='laptop', plat=sys.platform)
'My laptop   runs    win32'



# Building data ahead of time in both

>>> data = dict(platform=sys.platform, spam='laptop')

>>> 'My {spam:<8} runs {platform:>8}'.format(**data)
'My laptop   runs    win32'

>>> 'My %(spam)-8s runs %(platform)8s' % data
'My laptop   runs    win32'



# python 3.1 and later

>>> '{0:d}'.format(999999999999)
'999999999999'
>>> '{0:,d}'.format(999999999999)
'999,999,999,999'

>>> '{:,d}'.format(999999999999)
'999,999,999,999'
>>> '{:,d} {:,d}'.format(9999999, 8888888)
'9,999,999 8,888,888'
>>> '{:,.2f}'.format(296999.2567)
'296,999.26'



>>> '{0:b}'.format((2 ** 16) -1)
'1111111111111111'

>>> '%b' % ((2 ** 16) -1)
ValueError: unsupported format character 'b' (0x62) at index 1

>>> bin((2 ** 16) -1)
'0b1111111111111111'

>>> '%s' % bin((2 ** 16) -1)[2:]
'1111111111111111'



'\n%s<Class %s, address %s:\n%s%s%s>\n' % (...)              # Expression 

'\n{0}<Class {1}, address {2}:\n{3}{4}{5}>\n'.format(...)    # Method



C:\misc> C:\Python31\python
>>> 'The {0} side {1} {2}'.format('bright', 'of', 'life')
'The bright side of life'
>>>
>>> 'The {} side {} {}'.format('bright', 'of', 'life') # Python 3.1+
'The bright side of life'
>>>
>>> 'The %s side %s %s' % ('bright', 'of', 'life')
'The bright side of life'


C:\misc> C:\Python31\python
>>> '{0:f}, {1:.2f}, {2:05.2f}'.format(3.14159, 3.14159, 3.14159)
'3.141590, 3.14, 03.14'
>>>
>>> '{:f}, {:.2f}, {:06.2f}'.format(3.14159, 3.14159, 3.14159)
'3.141590, 3.14, 003.14'
>>>
>>> '%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159)
'3.141590, 3.14, 003.14'



>>> '%.2f' % 1.2345
'1.23'
>>> '%.2f %s' % (1.2345, 99)
'1.23 99'

>>> '%s' % 1.23
'1.23'
>>> '%s' % (1.23,)
'1.23'
>>> '%s' % ((1.23,),)
'(1.23,)'

>>> '{0:.2f}'.format(1.2345)
'1.23'
>>> '{0:.2f} {1}'.format(1.2345, 99)
'1.23 99'
>>> '{0}'.format(1.23)
'1.23'
>>> '{0}'.format((1.23,))
'(1.23,)'

