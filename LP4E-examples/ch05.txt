>>> int(3.1415)      # Truncates float to integer
3
>>> float(3)         # Converts integer to float
3.0



>>> a = 3              # Name created
>>> b = 4



>>> a + 1, a – 1       # Addition (3 + 1), subtraction (3 - 1)
(4, 2)
>>> b * 3, b / 2       # Multiplication (4 * 3), division (4 / 2)
(12, 2.0)
>>> a % 2, b ** 2      # Modulus (remainder), power (4 ** 2)
(1, 16)
>>> 2 + 4.0, 2.0 ** b  # Mixed-type conversions
(6.0, 16.0)



>>> c * 2
Traceback (most recent call last):
File "<stdin>", line 1, in ?
NameError: name 'c' is not defined



>>> b / 2 + a               # Same as ((4 / 2) + 3)
5.0
>>> print(b / (2.0 + a))    # Same as (4 / (2.0 + 3))
0.8



>>> b / (2.0 + a)           # Auto echo output: more digits
0.80000000000000004
>>> print(b / (2.0 + a))    # print rounds off digits
0.8



>>> 1 / 2.0
0.5



>>> num = 1 / 3.0
>>> num                       # Echoes
0.33333333333333331
>>> print(num)                # print rounds
0.333333333333
>>> '%e' % num                # String formatting expression
'3.333333e-001'
>>> '%4.2f' % num             # Alternative floating-point format
'0.33'
>>> '{0:4.2f}'.format(num)    # String formatting method (Python 2.6 and 3.0)
'0.33'



>>> num = 1 / 3
>>> repr(num)                 # Used by echoes: as-code form
'0.33333333333333331'
>>> str(num)                  # Used by print: user-friendly form
'0.333333333333'



>>> 1 < 2                     # Less than
True
>>> 2.0 >= 1                  # Greater than or equal: mixed-type 1 converted to 1.0
True
>>> 2.0 == 2.0                # Equal value
True
>>> 2.0 != 2.0                # Not equal value
False



>>> X = 2
>>> Y = 4
>>> Z = 6

>>> X < Y < Z                 # Chained comparisons: range tests
True
>>> X < Y and Y < Z
True

>>> X < Y > Z
False
>>> X < Y and Y > Z
False
>>> 1 < 2 < 3.0 < 4
True
>>> 1 > 2 > 3.0 > 4
False

>>> 1 == 2 < 3         # Same as: 1 == 2 and 2 < 3
False                  # Not same as: False < 3 (which means 0 < 3, which is true)



C:\misc> C:\Python30\python
>>>
>>> 10 / 4            # Differs in 3.0: keeps remainder
2.5
>>> 10 // 4           # Same in 3.0: truncates remainder
2
>>> 10 / 4.0          # Same in 3.0: keeps remainder
2.5
>>> 10 // 4.0         # Same in 3.0: truncates to floor
2.0

C:\misc> C:\Python26\python
>>>
>>> 10 / 4
2
>>> 10 // 4
2
>>> 10 / 4.0
2.5
>>> 10 // 4.0
2.0



C:\misc> C:\Python26\python
>>> from __future__ import division         # Enable 3.0 "/" behavior
>>> 10 / 4
2.5
>>> 10 // 4
2



>>> import math
>>> math.floor(2.5)
2
>>> math.floor(-2.5)
-3
>>> math.trunc(2.5)
2
>>> math.trunc(-2.5)
-2



C:\misc> c:\python30\python
>>> 5 / 2, 5 / -2
(2.5, -2.5)

>>> 5 // 2, 5 // -2       # Truncates to floor: rounds to first lower integer
(2, -3)                   # 2.5 becomes 2, -2.5 becomes -3

>>> 5 / 2.0, 5 / -2.0
(2.5, -2.5)

>>> 5 // 2.0, 5 // -2.0   # Ditto for floats, though result is float too
(2.0, -3.0)



C:\misc> c:\python26\python
>>> 5 / 2, 5 / -2         # Differs in 3.0
(2, -3)

>>> 5 // 2, 5 // -2       # This and the rest are the same in 2.6 and 3.0
(2, -3)

>>> 5 / 2.0, 5 / -2.0
(2.5, -2.5)

>>> 5 // 2.0, 5 // -2.0
(2.0, -3.0)


C:\misc> c:\python30\python
>>> import math
>>> 5 / -2                       # Keep remainder
-2.5 
>>> 5 // -2                      # Floor below result
-3
>>> math.trunc(5 / -2)           # Truncate instead of floor
-2

C:\misc> c:\python26\python
>>> import math
>>> 5 / float(-2)                # Remainder in 2.6
-2.5
>>> 5 / -2, 5 // -2              # Floor in 2.6
(-3, -3)
>>> math.trunc(5 / float(-2))    # Truncate in 2.6
-2


# If you are using 3.0, here is the short story on division operators for reference:
>>> (5 / 2), (5 / 2.0), (5 / -2.0), (5 / -2)       # 3.0 true division
(2.5, 2.5, -2.5, -2.5)

>>> (5 // 2), (5 // 2.0), (5 // -2.0), (5 // -2)   # 3.0 floor division
(2, 2.0, -3.0, -3)

>>> (9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0)       # Both
(3.0, 3.0, 3, 3.0)

# For 2.6 readers, division works as follows:
>>> (5 / 2), (5 / 2.0), (5 / -2.0), (5 / -2)       # 2.6 classic division
(2, 2.5, -2.5, -3)

>>> (5 // 2), (5 // 2.0), (5 // -2.0), (5 // -2)   # 2.6 floor division (same)
(2, 2.0, -3.0, -3)

>>> (9 / 3), (9.0 / 3), (9 // 3), (9 // 3.0)       # Both
(3, 3.0, 3, 3.0)



>>> 999999999999999999999999999999 + 1
1000000000000000000000000000000

>>> 999999999999999999999999999999 + 1
1000000000000000000000000000000L             # 2.6

>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376

>>> 2 ** 200
1606938044258990275541962092341162602522202993782792835301376L    # 2.6



>>> 1j * 1J
(-1+0j)
>>> 2 + 1j * 3
(2+3j)
>>> (2 + 1j) * 3
(6+3j)



>>> 0o1, 0o20, 0o377           # Octal literals
(1, 16, 255)
>>> 0x01, 0x10, 0xFF           # Hex literals
(1, 16, 255)
>>> 0b1, 0b10000, 0b11111111   # Binary literals
(1, 16, 255)


>>> oct(64), hex(64), bin(64)
('0100', '0x40', '0b1000000')

>>> int('64'), int('100', 8), int('40', 16), int('1000000', 2)
(64, 64, 64, 64)

>>> int('0x40', 16), int('0b1000000', 2)      # Literals okay too
(64, 64)

>>> eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000')
(64, 64, 64, 64)



>>> '{0:o}, {1:x}, {2:b}'.format(64, 64, 64)
'100, 40, 1000000'

>>> '%o, %x, %X' % (64, 255, 255)
'100, ff, FF'


>>> 0o1, 0o20, 0o377       # New octal format in 2.6 (same as 3.0)
(1, 16, 255)
>>> 01, 020, 0377          # Old octal literals in 2.6 (and earlier)
(1, 16, 255)



# Note: in the following the trailing "L"s appear in Python 2.X,
# but not 3.X, as implied earlier in the chapter (this is 2.X output);
# it was run in 2.6 to reveal the long type created for extra precision;
# teh same happens in 3.X, but you can't tell the difference;
 
>>> X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
>>> X
5192296858534827628530496329220095L
>>> oct(X)
'017777777777777777777777777777777777777L'
>>> bin(X)
'0b1111111111111111111111111111111111111111111111111111111111 ...and so on...


# The 3.X output is as follows:
>>> X = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
>>> X
5192296858534827628530496329220095
>>> oct(X)
'0o17777777777777777777777777777777777777'
>>> bin(X)
'0b11111111111111111111111111111111111111111111 ...same...



>>> x = 1        # 0001
>>> x << 2       # Shift left 2 bits: 0100
4
>>> x | 2        # Bitwise OR: 0011
3
>>> x & 1        # Bitwise AND: 0001
1



>>> X = 0b0001           # Binary literals
>>> X << 2               # Shift left
4
>>> bin(X << 2)          # Binary digits string
'0b100'
>>> bin(X | 0b010)       # Bitwise OR
'0b11'
>>> bin(X & 0b1)         # Bitwise AND
'0b1'
>>> X = 0xFF             # Hex literals
>>> bin(X)
'0b11111111'
>>> X ^ 0b10101010       # Bitwise XOR
85
>>> bin(X ^ 0b10101010)
'0b1010101'
>>> int('1010101', 2)    # String to int per base
85
>>> hex(85)              # Hex digit string
'0x55'



>>> X = 99
>>> bin(X), X.bit_length()
('0b1100011', 7)
>>> bin(256), (256).bit_length()
('0b100000000', 9)
>>> len(bin(256)) - 2
9



>>> import math
>>> math.pi, math.e                         # Common constants
(3.1415926535897931, 2.7182818284590451)

>>> math.sin(2 * math.pi / 180)             # Sine, tangent, cosine
0.034899496702500969

>>> math.sqrt(144), math.sqrt(2)            # Square root
(12.0, 1.4142135623730951)

>>> pow(2, 4), 2 ** 4                       # Exponentiation (power)
(16, 16)

>>> abs(-42.0), sum((1, 2, 3, 4))           # Absolute value, summation
(42.0, 10)

>>> min(3, 1, 2, 4), max(3, 1, 2, 4)        # Minimum, maximum
(1, 4)



>>> math.floor(2.567), math.floor(-2.567)            # Floor (next-lower integer)
(2, -3)

>>> math.trunc(2.567), math.trunc(-2.567)            # Truncate (drop decimal digits)
(2, -2)

>>> int(2.567), int(-2.567)                          # Truncate (integer conversion)
(2, -2)

>>> round(2.567), round(2.467), round(2.567, 2)      # Round (Python 3.0 version)
(3, 2, 2.5699999999999998)

>>> '%.1f' % 2.567, '{0:.2f}'.format(2.567)          # Round for display (Chapter 7)
('2.6', '2.57')



>>> (1 / 3), round(1 / 3, 2), ('%.2f' % (1 / 3))
(0.33333333333333331, 0.33000000000000002, '0.33')



>>> import math
>>> math.sqrt(144)        # Module
12.0
>>> 144 ** .5             # Expression
12.0
>>> pow(144, .5)          # Built-in
12.0

>>> math.sqrt(1234567890) # Larger numbers
35136.418286444619
>>> 1234567890 ** .5
35136.418286444619
>>> pow(1234567890, .5)
35136.418286444619



>>> import random
>>> random.random()
0.44694718823781876
>>> random.random()
0.28970426439292829

>>> random.randint(1, 10)
5
>>> random.randint(1, 10)
4

>>> random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])
'Life of Brian'
>>> random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life'])
'Holy Grail'




>>> 0.1 + 0.1 + 0.1 - 0.3
5.5511151231257827e-17

>>> print(0.1 + 0.1 + 0.1 - 0.3)
5.55111512313e-17

>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')

>>> Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')
Decimal('0.00')



>>> import decimal
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.1428571428571428571428571429')

>>> decimal.getcontext().prec = 4
>>> decimal.Decimal(1) / decimal.Decimal(7)
Decimal('0.1429')



>>> 1999 + 1.33
2000.3299999999999
>>>
>>> decimal.getcontext().prec = 2
>>> pay = decimal.Decimal(str(1999 + 1.33))
>>> pay
Decimal('2000.33')



C:\misc> C:\Python30\python
>>> import decimal
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.3333333333333333333333333333')
>>>
>>> with decimal.localcontext() as ctx:
...     ctx.prec = 2
...     decimal.Decimal('1.00') / decimal.Decimal('3.00')
...
Decimal('0.33')
>>>
>>> decimal.Decimal('1.00') / decimal.Decimal('3.00')
Decimal('0.3333333333333333333333333333')



>>> from fractions import Fraction
>>> x = Fraction(1, 3)                # Numerator, denominator
>>> y = Fraction(4, 6)                # Simplified to 2, 3 by gcd
>>> x
Fraction(1, 3)
>>> y
Fraction(2, 3)
>>> print(y)
2/3

>>> x + y
Fraction(1, 1)
>>> x – y                             # Results are exact: numerator, denominator
Fraction(-1, 3)
>>> x * y
Fraction(2, 9)

>>> Fraction('.25')
Fraction(1, 4)
>>> Fraction('1.25')
Fraction(5, 4)
>>>
>>> Fraction('.25') + Fraction('1.25')
Fraction(3, 2)



>>> a = 1 / 3.0       # Only as accurate as floating-point hardware
>>> b = 4 / 6.0       # Can lose precision over calculations
>>> a
0.33333333333333331
>>> b
0.66666666666666663

>>> a + b
1.0
>>> a - b
-0.33333333333333331
>>> a * b
0.22222222222222221

>>> 0.1 + 0.1 + 0.1 - 0.3       # This should be zero (close, but not exact)
5.5511151231257827e-17

>>> from fractions import Fraction
>>> Fraction(1, 10) + Fraction(1, 10) + Fraction(1, 10) - Fraction(3, 10)
Fraction(0, 1)

>>> from decimal import Decimal
>>> Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
Decimal('0.0')



>>> 1 / 3                             # Use 3.0 in Python 2.6 for true "/"
0.33333333333333331

>>> Fraction(1, 3)                    # Numeric accuracy
Fraction(1, 3)

>>> import decimal
>>> decimal.getcontext().prec = 2
>>> decimal.Decimal(1) / decimal.Decimal(3)
Decimal('0.33')



>>> (1 / 3) + (6 / 12)                   # Use ".0" in Python 2.6 for true "/"
0.83333333333333326

>>> Fraction(6, 12)                      # Automatically simplified
Fraction(1, 2)

>>> Fraction(1, 3) + Fraction(6, 12)
Fraction(5, 6)

>>> decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
Decimal('0.83')

>>> 1000.0 / 1234567890
8.1000000737100011e-07

>>> Fraction(1000, 1234567890)
Fraction(100, 123456789)



>>> (2.5).as_integer_ratio()              # float object method
(5, 2)
>>> f = 2.5
>>> z = Fraction(*f.as_integer_ratio())   # Convert float -> fraction: two args
>>> z                                     # Same as Fraction(5, 2)
Fraction(5, 2)

>>> x                                     # x from prior interaction
Fraction(1, 3)
>>> x + z
Fraction(17, 6)                           # 5/2 + 1/3 = 15/6 + 2/6

>>> float(x)                              # Convert fraction -> float
0.33333333333333331
>>> float(z)
2.5

>>> float(x + z)
2.8333333333333335
>>> 17 / 6
2.8333333333333335

>>> Fraction.from_float(1.75)             # Convert float -> fraction: other way
Fraction(7, 4)
>>> Fraction(*(1.75).as_integer_ratio())
Fraction(7, 4)



>>> x
Fraction(1, 3)
>>> x + 2                # Fraction + int -> Fraction
Fraction(7, 3)
>>> x + 2.0              # Fraction + float -> float
2.3333333333333335
>>> x + (1./3)           # Fraction + float -> float
0.66666666666666663

>>> x + (4./3)
1.6666666666666665
>>> x + Fraction(4, 3)   # Fraction + Fraction -> Fraction
Fraction(5, 3)



>>> 4.0 / 3
1.3333333333333333
>>> (4.0 / 3).as_integer_ratio()       # Precision loss from float
(6004799503160661, 4503599627370496)

>>> x
Fraction(1, 3)
>>> a = x + Fraction(*(4.0 / 3).as_integer_ratio())
>>> a
Fraction(22517998136852479, 13510798882111488)

>>> 22517998136852479 / 13510798882111488.         # 5 / 3 (or close to it!)
1.6666666666666667

>>> a.limit_denominator(10)                        # Simplify to closest fraction
Fraction(5, 3)



>>> x = set('abcde')
>>> y = set('bdxyz')
>>> x
set(['a', 'c', 'b', 'e', 'd'])          # 2.6 display format

>>> 'e' in x                  # Membership
True 
>>> x – y                     # Difference
set(['a', 'c', 'e']) 
>>> x | y                     # Union
set(['a', 'c', 'b', 'e', 'd', 'y', 'x', 'z'])
>>> x & y                     # Intersection
set(['b', 'd'])
>>> x ^ y                     # Symmetric difference (XOR)
set(['a', 'c', 'e', 'y', 'x', 'z'])
>>> x > y, x < y              # Superset, subset
(False, False)

>>> z = x.intersection(y)     # Same as x & y
>>> z
set(['b', 'd'])
>>> z.add('SPAM')             # Insert one item
>>> z
set(['b', 'd', 'SPAM'])
>>> z.update(set(['X', 'Y'])) # Merge: in-place union
>>> z
set(['Y', 'X', 'b', 'd', 'SPAM'])
>>> z.remove('b')             # Delete one item
>>> z
set(['Y', 'X', 'd', 'SPAM'])

>>> for item in set('abc'): print(item * 3)
...
aaa
ccc
bbb

>>> S = set([1, 2, 3])
>>> S | set([3, 4])          # Expressions require both to be sets
set([1, 2, 3, 4])
>>> S | [3, 4]
TypeError: unsupported operand type(s) for |: 'set' and 'list'
>>> S.union([3, 4])          # But their methods allow any iterable
set([1, 2, 3, 4])
>>> S.intersection((1, 3, 5))
set([1, 3])
>>> S.issubset(range(-5, 5))
True



C:\Misc> c:\python30\python
>>> set([1, 2, 3, 4])          # Built-in: same as in 2.6
{1, 2, 3, 4}
>>> set('spam')                # Add all items in an iterable
{'a', 'p', 's', 'm'}
>>> {1, 2, 3, 4}               # Set literals: new in 3.0
{1, 2, 3, 4}
>>> S = {'s', 'p', 'a', 'm'}
>>> S.add('alot')
>>> S
{'a', 'p', 's', 'm', 'alot'}

>>> S1 = {1, 2, 3, 4}
>>> S1 & {1, 3}                # Intersection
{1, 3}
>>> {1, 5, 3, 6} | S1          # Union
{1, 2, 3, 4, 5, 6}
>>> S1 - {1, 3, 4}             # Difference
{2}
>>> S1 > {1, 3}                # Superset
True

>>> S1 - {1, 2, 3, 4}          # Empty sets print differently
set()
>>> type({})                   # Because {} is an empty dictionary
<class 'dict'>
>>> S = set()                  # Initialize an empty set
>>> S.add(1.23)
>>> S
{1.23}

{1, 2, 3, 4}
>>> {1, 2, 3} | [3, 4]
TypeError: unsupported operand type(s) for |: 'set' and 'list'

>>> {1, 2, 3}.union([3, 4])
{1, 2, 3, 4}
>>> {1, 2, 3}.union({3, 4})
{1, 2, 3, 4}
>>> {1, 2, 3}.union(set([3, 4]))
{1, 2, 3, 4}

>>> {1, 2, 3}.intersection((1, 3, 5))
{1, 3}
>>> {1, 2, 3}.issubset(range(-5, 5))
True

>>> S
{1.23}
>>> S.add([1, 2, 3])                  # Only immutable objects work in a set
TypeError: unhashable type: 'list'
>>> S.add({'a':1})
TypeError: unhashable type: 'dict'
>>> S.add((1, 2, 3))
>>> S                                 # No list or dict, but tuple okay
{1.23, (1, 2, 3)}

>>> S | {(4, 5, 6), (1, 2, 3)}        # Union: same as S.union(...)
{1.23, (4, 5, 6), (1, 2, 3)}
>>> (1, 2, 3) in S                    # Membership: by complete values
True
>>> (1, 4, 3) in S
False



>>> {x ** 2 for x in [1, 2, 3, 4]}     # 3.0 set comprehension
{16, 1, 4, 9}

>>> {x for x in 'spam'}                # Same as: set('spam')
{'a', 'p', 's', 'm'}
>>> {c * 4 for c in 'spam'}            # Set of collected expression results
{'ssss', 'aaaa', 'pppp', 'mmmm'}
>>> {c * 4 for c in 'spamham'}
{'ssss', 'aaaa', 'hhhh', 'pppp', 'mmmm'}

>>> S = {c * 4 for c in 'spam'}
>>> S | {'mmmm', 'xxxx'}
{'ssss', 'aaaa', 'pppp', 'mmmm', 'xxxx'}
>>> S & {'mmmm', 'xxxx'}
{'mmmm'}



>>> L = [1, 2, 1, 3, 2, 4, 5]
>>> set(L)
{1, 2, 3, 4, 5}
>>> L = list(set(L))                     # Remove duplicates
>>> L
[1, 2, 3, 4, 5]

>>> engineers = {'bob', 'sue', 'ann', 'vic'}
>>> managers = {'tom', 'sue'}
>>> 'bob' in engineers                    # Is bob an engineer?
True
>>> engineers & managers                  # Who is both engineer and manager?
{'sue'}
>>> engineers | managers                  # All people in either category
{'vic', 'sue', 'tom', 'bob', 'ann'}
>>> engineers – managers                  # Engineers who are not managers
{'vic', 'bob', 'ann'}
>>> managers – engineers                  # Managers who are not engineers
{'tom'}
>>> engineers > managers                  # Are all managers engineers? (superset)
False
>>> {'bob', 'sue'} < engineers            # Are both engineers? (subset)
True
>>> (managers | engineers) > managers     # All people is a superset of managers
True
>>> managers ^ engineers                  # Who is in one but not both?
{'vic', 'bob', 'ann', 'tom'}
>>> (managers | engineers) - (managers ^ engineers)        # Intersection!
{'sue'}



>>> type(True)
<class 'bool'>
>>> isinstance(True, int)
True
>>> True == 1           # Same value
True
>>> True is 1           # But different object: see the next chapter
False
>>> True or False       # Same as: 1 or 0
True
>>> True + 4            # (Hmmm)
5




