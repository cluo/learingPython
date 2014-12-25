>>> ord('a')         # 'a' is a byte with binary value 97 in ASCII
97
>>> hex(97)
'0x61'
>>> chr(97)          # Binary value 97 stands for character 'a'
'a'



>>> 0xC4
196
>>> chr(196)
'Ä'



C:\misc> c:\python30\python

>>> B = b'spam'           # Make a bytes object (8-bit bytes)
>>> S = 'eggs'            # Make a str object (Unicode characters, 8-bit or wider)

>>> type(B), type(S)
(<class 'bytes'>, <class 'str'>)

>>> B                     # Prints as a character string, really sequence of ints
b'spam'
>>> S
'eggs'



>>> B[0], S[0]            # Indexing returns an int for bytes, str for str
(115, 'e')

>>> B[1:], S[1:]          # Slicing makes another bytes or str object
(b'pam', 'ggs')

>>> list(B), list(S)
([115, 112, 97, 109], ['e', 'g', 'g', 's'])     # bytes is really ints



>>> B[0] = 'x'                                  # Both are immutable
TypeError: 'bytes' object does not support item assignment

>>> S[0] = 'x'
TypeError: 'str' object does not support item assignment

>>> B = B"""              # bytes prefix works on single, double, triple quotes
... xxxx
... yyyy
... """
>>> B
b'\nxxxx\nyyyy\n'



>>> S = 'eggs'
>>> S.encode()                          # str to bytes: encode text into raw bytes
b'eggs'

>>> bytes(S, encoding='ascii')          # str to bytes, alternative
b'eggs'

>>> B = b'spam'
>>> B.decode()                          # bytes to str: decode raw bytes into text
'spam'

>>> str(B, encoding='ascii')            # bytes to str, alternative
'spam'



>>> import sys
>>> sys.platform                        # Underlying platform
'win32'
>>> sys.getdefaultencoding()            # Default encoding for str here
'utf-8'

>>> bytes(S)
TypeError: string argument without an encoding

>>> str(B)                              # str without encoding
"b'spam'"                               # A print string, not conversion!
>>> len(str(B))
7
>>> len(str(B, encoding='ascii'))       # Use encoding to convert to str
4



C:\misc> c:\python30\python

>>> ord('X')             # 'X' has binary value 88 in the default encoding 
88
>>> chr(88)              # 88 stands for character 'X'
'X'

>>> S = 'XYZ'            # A Unicode string of ASCII text
>>> S
'XYZ'
>>> len(S)               # 3 characters long
3
>>> [ord(c) for c in S]  # 3 bytes with integer ordinal values
[88, 89, 90]



>>> S.encode('ascii')    # Values 0..127 in 1 byte (7 bits) each
b'XYZ'
>>> S.encode('latin-1')  # Values 0..255 in 1 byte (8 bits) each
b'XYZ'
>>> S.encode('utf-8')    # Values 0..127 in 1 byte, 128..2047 in 2, others 3 or 4
b'XYZ'



>>> S.encode('latin-1')[0]
88
>>> list(S.encode('latin-1'))
[88, 89, 90]



>>> chr(0xc4)            # 0xC4, 0xE8: characters outside ASCII's range
'Ä'
>>> chr(0xe8)
'è'

>>> S = '\xc4\xe8'       # Single byte 8-bit hex escapes
>>> S
'Äè'

>>> S = '\u00c4\u00e8'   # 16-bit Unicode escapes
>>> S
'Äè'
>>> len(S)               # 2 characters long (not number of bytes!)
2



>>> S = '\u00c4\u00e8'
>>> S
'Äè'
>>> len(S)
2

>>> S.encode('ascii')
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: 
ordinal not in range(128)

>>> S.encode('latin-1')              # One byte per character
b'\xc4\xe8'

>>> S.encode('utf-8')                # Two bytes per character
b'\xc3\x84\xc3\xa8'

>>> len(S.encode('latin-1'))         # 2 bytes in latin-1, 4 in utf-8
2
>>> len(S.encode('utf-8'))
4



>>> B = b'\xc4\xe8'
>>> B
b'\xc4\xe8'
>>> len(B)                           # 2 raw bytes, 2 characters
2
>>> B.decode('latin-1')              # Decode to latin-1 text
'Äè'

>>> B = b'\xc3\x84\xc3\xa8'
>>> len(B)                           # 4 raw bytes
4
>>> B.decode('utf-8')
'Äè'
>>> len(B.decode('utf-8'))           # 2 Unicode characters
2



>>> S = 'A\u00c4B\U000000e8C'
>>> S                                # A, B, C, and 2 non-ASCII characters
'AÄBèC'
>>> len(S)                           # 5 characters long
5

>>> S.encode('latin-1')
b'A\xc4B\xe8C'
>>> len(S.encode('latin-1'))         # 5 bytes in latin-1
5

>>> S.encode('utf-8')
b'A\xc3\x84B\xc3\xa8C'
>>> len(S.encode('utf-8'))           # 7 bytes in utf-8
7



>>> S
'AÄBèC'
>>> S.encode('cp500')                # Two other Western European encodings
b'\xc1c\xc2T\xc3'
>>> S.encode('cp850')                # 5 bytes each
b'A\x8eB\x8aC'

>>> S = 'spam'                       # ASCII text is the same in most
>>> S.encode('latin-1')
b'spam'
>>> S.encode('utf-8')
b'spam'
>>> S.encode('cp500')                # But not in cp500: IBM EBCDIC!
b'\xa2\x97\x81\x94'
>>> S.encode('cp850')
b'spam'



>>> S = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'
>>> S
'AÄBèC'



>>> S = 'A\xC4B\xE8C'                # str recognizes hex and Unicode escapes
>>> S
'AÄBèC'

>>> S = 'A\u00C4B\U000000E8C'
>>> S
'AÄBèC'

>>> B = b'A\xC4B\xE8C'               # bytes recognizes hex but not Unicode
>>> B
b'A\xc4B\xe8C'

>>> B = b'A\u00C4B\U000000E8C'       # Escape sequences taken literally!
>>> B
b'A\\u00C4B\\U000000E8C'

>>> B = b'A\xC4B\xE8C'               # Use hex escapes for bytes
>>> B                                # Prints non-ASCII as hex 
b'A\xc4B\xe8C'
>>> print(B)
b'A\xc4B\xe8C'
>>> B.decode('latin-1')              # Decode as latin-1 to interpret as text 
'AÄBèC'



>>> S = 'AÄBèC'                      # Chars from UTF-8 if no encoding declaration 
>>> S
'AÄBèC'

>>> B = b'AÄBèC'
SyntaxError: bytes can only contain ASCII literal characters.

>>> B = b'A\xC4B\xE8C'               # Chars must be ASCII, or escapes
>>> B
b'A\xc4B\xe8C'
>>> B.decode('latin-1')
'AÄBèC'

>>> S.encode()                       # Source code encoded per UTF-8 by default 
b'A\xc3\x84B\xc3\xa8C'               # Uses system default to encode, unless passed
>>> S.encode('utf-8')
b'A\xc3\x84B\xc3\xa8C'

>>> B.decode()                       # Raw bytes do not correspond to utf-8
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 1-2: ...



>>> S = 'AÄBèC'
>>> S
'AÄBèC'
>>> S.encode()                       # Default utf-8 encoding
b'A\xc3\x84B\xc3\xa8C'

>>> T = S.encode('cp500')            # Convert to EBCDIC
>>> T
b'\xc1c\xc2T\xc3'

>>> U = T.decode('cp500')            # Convert back to Unicode
>>> U
'AÄBèC'

>>> U.encode()                       # Default utf-8 encoding again
b'A\xc3\x84B\xc3\xa8C'



C:\misc> c:\python26\python 
>>> import sys
>>> sys.version
'2.6 (r26:66721, Oct  2 2008, 11:35:03) [MSC v.1500 32 bit (Intel)]'

>>> S = 'A\xC4B\xE8C'                # String of 8-bit bytes
>>> print S                          # Some are non-ASCII
AÄBèC

>>> S.decode('latin-1')              # Decode byte to latin-1 Unicode
u'A\xc4B\xe8C'

>>> S.decode('utf-8')                # Not formatted as utf-8
UnicodeDecodeError: 'utf8' codec can't decode bytes in position 1-2: invalid data

>>> S.decode('ascii')                # Outside ASCII range
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 1: ordinal 
not in range(128)



>>> U = u'A\xC4B\xE8C'               # Make Unicode string, hex escapes
>>> U
u'A\xc4B\xe8C'
>>> print U
AÄBèC



>>> U.encode('latin-1')              # Encode per latin-1: 8-bit bytes
'A\xc4B\xe8C'
>>> U.encode('utf-8')                # Encode per utf-8: multibyte
'A\xc3\x84B\xc3\xa8C'



C:\misc> c:\python26\python 
>>> U = u'A\xC4B\xE8C'               # Hex escapes for non-ASCII
>>> U
u'A\xc4B\xe8C'
>>> print U
AÄBèC

>>> U = u'A\u00C4B\U000000E8C'       # Unicode escapes for non-ASCII
>>> U                                # u'' = 16 bits, U'' = 32 bits
u'A\xc4B\xe8C'
>>> print U
AÄBèC

>>> S = 'A\xC4B\xE8C'                # Hex escapes work
>>> S
'A\xc4B\xe8C'
>>> print S                          # But some print oddly, unless decoded
A-BFC
>>> print S.decode('latin-1')
AÄBèC

>>> S = 'A\u00C4B\U000000E8C'        # Not Unicode escapes: taken literally!
>>> S
'A\\u00C4B\\U000000E8C'
>>> print S
A\u00C4B\U000000E8C
>>> len(S)
19



>>> u'ab' + 'cd'                     # Can mix if compatible in 2.6
u'abcd'                              # 'ab' + b'cd' not allowed in 3.0



>>> str(u'spam')                     # Unicode to normal
'spam'
>>> unicode('spam')                  # Normal to Unicode
u'spam'



>>> S = 'A\xC4B\xE8C'                # Can't mix if incompatible
>>> U = u'A\xC4B\xE8C'
>>> S + U
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 1: ordinal
not in range(128)

>>> S.decode('latin-1') + U          # Manual conversion still required 
u'A\xc4B\xe8CA\xc4B\xe8C'

>>> print S.decode('latin-1') + U
AÄBèCAÄBèC



# -*- coding: latin-1 -*-


### file: text.py

# -*- coding: latin-1 -*-

# Any of the following string literal forms work in latin-1.
# Changing the encoding above to either ascii or utf-8 fails,
# because the 0xc4 and 0xe8 in myStr1 are not valid in either.

myStr1 = 'aÄBèC'

myStr2 = 'A\u00c4B\U000000e8C'

myStr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys
print('Default encoding:', sys.getdefaultencoding())

for aStr in myStr1, myStr2, myStr3:
    print('{0}, strlen={1}, '.format(aStr, len(aStr)), end='')

    bytes1 = aStr.encode()              # Per default utf-8: 2 bytes for non-ASCII
    bytes2 = aStr.encode('latin-1')     # One byte per char 
   #bytes3 = aStr.encode('ascii')       # ASCII fails: outside 0..127 range

    print('byteslen1={0}, byteslen2={1}'.format(len(bytes1), len(bytes2)))



C:\misc> c:\python30\python text.py
Default encoding: utf-8
aÄBèC, strlen=5, byteslen1=7, byteslen2=5
AÄBèC, strlen=5, byteslen1=7, byteslen2=5
AÄBèC, strlen=5, byteslen1=7, byteslen2=5



C:\misc> c:\python30\python

# Attributes unique to str

>>> set(dir('abc')) - set(dir(b'abc'))
{'isprintable', 'format', '__mod__', 'encode', 'isidentifier',
'_formatter_field_name_split', 'isnumeric', '__rmod__', 'isdecimal',
'_formatter_parser', 'maketrans'}

# Attributes unique to bytes

>>> set(dir(b'abc')) - set(dir('abc'))
{'decode', 'fromhex'}



>>> B = b'spam'                    # b'...' bytes literal
>>> B.find(b'pa')
1

>>> B.replace(b'pa', b'XY')        # bytes methods expect bytes arguments
b'sXYm'

>>> B.split(b'pa')
[b's', b'm']

>>> B
b'spam'

>>> B[0] = 'x'
TypeError: 'bytes' object does not support item assignment



>>> b'%s' % 99
TypeError: unsupported operand type(s) for %: 'bytes' and 'int'

>>> '%s' % 99
'99'

>>> b'{0}'.format(99)
AttributeError: 'bytes' object has no attribute 'format'

>>> '{0}'.format(99)
'99'



>>> B = b'spam'                  # A sequence of small ints
>>> B                            # Prints as ASCII characters
b'spam'

>>> B[0]                         # Indexing yields an int
115
>>> B[-1]
109

>>> chr(B[0])                    # Show character for int
's'
>>> list(B)                      # Show all the byte's int values
[115, 112, 97, 109]

>>> B[1:], B[:-1]
(b'pam', b'spa')
 
>>> len(B)
4

>>> B + b'lmn'
b'spamlmn'
>>> B * 4
b'spamspamspamspam'



>>> B = b'abc'
>>> B
b'abc'

>>> B = bytes('abc', 'ascii')
>>> B
b'abc'

>>> ord('a')
97
>>> B = bytes([97, 98, 99])
>>> B
b'abc'

>>> B = 'spam'.encode()          # Or bytes()
>>> B
b'spam'
>>>
>>> S = B.decode()               # Or str()
>>> S
'spam'



# Must pass expected types to function and method calls

>>> B = b'spam'

>>> B.replace('pa', 'XY')
TypeError: expected an object with the buffer interface

>>> B.replace(b'pa', b'XY')
b'sXYm'

>>> B = B'spam'
>>> B.replace(bytes('pa'), bytes('xy'))
TypeError: string argument without an encoding

>>> B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8'))
b'sxym'


# Must convert manually in mixed-type expressions

>>> b'ab' + 'cd'
TypeError: can't concat bytes to str

>>> b'ab'.decode() + 'cd'                   # bytes to str
'abcd'

>>> b'ab' + 'cd'.encode()                   # str to bytes
b'abcd'

>>> b'ab' + bytes('cd', 'ascii')            # str to bytes
b'abcd'



# Creation in 2.6: a mutable sequence of small (0..255) ints

>>> S = 'spam'
>>> C = bytearray(S)                      # A back-port from 3.0 in 2.6
>>> C                                     # b'..' == '..' in 2.6 (str)
bytearray(b'spam')



# Creation in 3.0: text/binary do not mix

>>> S = 'spam'
>>> C = bytearray(S)
TypeError: string argument without an encoding

>>> C = bytearray(S, 'latin1')            # A content-specific type in 3.0
>>> C
bytearray(b'spam')

>>> B = b'spam'                           # b'..' != '..' in 3.0 (bytes/str)
>>> C = bytearray(B)
>>> C
bytearray(b'spam')



# Mutable, but must assign ints, not strings

>>> C[0]
115

>>> C[0] = 'x'                              # This and the next work in 2.6
TypeError: an integer is required

>>> C[0] = b'x'
TypeError: an integer is required

>>> C[0] = ord('x')
>>> C
bytearray(b'xpam')

>>> C[1] = b'Y'[0]
>>> C
bytearray(b'xYam')



# Methods overlap with both str and bytes, but also has list's mutable methods

>>> set(dir(b'abc')) - set(dir(bytearray(b'abc')))
{'__getnewargs__'}

>>> set(dir(bytearray(b'abc'))) - set(dir(b'abc'))
{'insert', '__alloc__', 'reverse', 'extend', '__delitem__', 'pop', '__setitem__'
, '__iadd__', 'remove', 'append', '__imul__'}



# Mutable method calls

>>> C
bytearray(b'xYam')

>>> C.append(b'LMN')                        # 2.6 requires string of size 1
TypeError: an integer is required

>>> C.append(ord('L'))
>>> C
bytearray(b'xYamL')

>>> C.extend(b'MNO')
>>> C
bytearray(b'xYamLMNO')



# Sequence operations and string methods

>>> C + b'!#'
bytearray(b'xYamLMNO!#')

>>> C[0]
120

>>> C[1:]
bytearray(b'YamLMNO')

>>> len(C)
8

>>> C
bytearray(b'xYamLMNO')

>>> C.replace('xY', 'sp')                            # This works in 2.6
TypeError: Type str doesn't support the buffer API

>>> C.replace(b'xY', b'sp')
bytearray(b'spamLMNO')

>>> C
bytearray(b'xYamLMNO')

>>> C * 4
bytearray(b'xYamLMNOxYamLMNOxYamLMNOxYamLMNO')



# Binary versus text 

>>> B                                # B is same as S in 2.6
b'spam'
>>> list(B)
[115, 112, 97, 109]

>>> C
bytearray(b'xYamLMNO')
>>> list(C)
[120, 89, 97, 109, 76, 77, 78, 79]

>>> S
'spam'
>>> list(S)
['s', 'p', 'a', 'm']



C:\misc> c:\python30\python

# Basic text files (and strings) work the same as in 2.X

>>> file = open('temp', 'w')
>>> size = file.write('abc\n')       # Returns number of bytes written
>>> file.close()                     # Manual close to flush output buffer

>>> file = open('temp')              # Default mode is "r" (== "rt"): text input
>>> text = file.read()
>>> text
'abc\n'
>>> print(text)
abc



C:\misc> c:\python26\python
>>> open('temp', 'w').write('abd\n')         # Write in text mode: adds \r
>>> open('temp', 'r').read()                 # Read in text mode: drops \r
'abd\n'
>>> open('temp', 'rb').read()                # Read in binary mode: verbatim
'abd\r\n'

>>> open('temp', 'wb').write('abc\n')        # Write in binary mode
>>> open('temp', 'r').read()                 # \n not expanded to \r\n
'abc\n'
>>> open('temp', 'rb').read()
'abc\n'



C:\misc> c:\python30\python

# Write and read a text file

>>> open('temp', 'w').write('abc\n')         # Text mode output, provide a str
4

>>> open('temp', 'r').read()                 # Text mode input, returns a str
'abc\n'

>>> open('temp', 'rb').read()                # Binary mode input, returns a bytes
b'abc\r\n'



# Write and read a binary file

>>> open('temp', 'wb').write(b'abc\n')       # Binary mode output, provide a bytes
4

>>> open('temp', 'r').read()                 # Text mode input, returns a str
'abc\n'

>>> open('temp', 'rb').read()                # Binary mode input, returns a bytes
b'abc\n'



# Write and read truly binary data

>>> open('temp', 'wb').write(b'a\x00c')      # Provide a bytes
3

>>> open('temp', 'r').read()                 # Receive a str
'a\x00c'

>>> open('temp', 'rb').read()                # Receive a bytes
b'a\x00c'



# bytearrays work too

>>> BA = bytearray(b'\x01\x02\x03')

>>> open('temp', 'wb').write(BA)
3

>>> open('temp', 'r').read()
'\x01\x02\x03'

>>> open('temp', 'rb').read()
b'\x01\x02\x03'



# Types are not flexible for file content

>>> open('temp', 'w').write('abc\n')         # Text mode makes and requires str
4
>>> open('temp', 'w').write(b'abc\n')
TypeError: can't write bytes to text stream

>>> open('temp', 'wb').write(b'abc\n')       # Binary mode makes and requires bytes
4
>>> open('temp', 'wb').write('abc\n')
TypeError: can't write str to binary stream



# Can't read truly binary data in text mode

>>> chr(0xFF)                                   # FF is a valid char, FE is not
'ÿ'
>>> chr(0xFE)
UnicodeEncodeError: 'charmap' codec can't encode character '\xfe' in position 1...
 
>>> open('temp', 'w').write(b'\xFF\xFE\xFD')    # Can't use arbitrary bytes!
TypeError: can't write bytes to text stream

>>> open('temp', 'w').write('\xFF\xFE\xFD')     # Can write if embeddable in str
3
>>> open('temp', 'wb').write(b'\xFF\xFE\xFD')   # Can also write in binary mode
3

>>> open('temp', 'rb').read()                   # Can always read as binary bytes
b'\xff\xfe\xfd'

>>> open('temp', 'r').read()                    # Can't read text unless decodable!
UnicodeEncodeError: 'charmap' codec can't encode characters in position 2-3: ...



C:\misc> c:\python30\python
>>> S = 'A\xc4B\xe8C'           # 5-character string, non-ASCII
>>> S
'AÄBèC'
>>> len(S)
5



# Encode manually with methods

>>> L = S.encode('latin-1')     # 5 bytes when encoded as latin-1
>>> L
b'A\xc4B\xe8C'
>>> len(L)
5

>>> U = S.encode('utf-8')       # 7 bytes when encoded as utf-8
>>> U
b'A\xc3\x84B\xc3\xa8C'
>>> len(U)
7



# Encoding automatically when written

>>> open('latindata', 'w', encoding='latin-1').write(S)    # Write as latin-1
5
>>> open('utf8data', 'w', encoding='utf-8').write(S)       # Write as utf-8
5

>>> open('latindata', 'rb').read()                         # Read raw bytes
b'A\xc4B\xe8C'

>>> open('utf8data', 'rb').read()                          # Different in files
b'A\xc3\x84B\xc3\xa8C'



# Decoding automatically when read

>>> open('latindata', 'r', encoding='latin-1').read()      # Decoded on input
'AÄBèC'
>>> open('utf8data', 'r', encoding='utf-8').read()         # Per encoding type
'AÄBèC'

>>> X = open('latindata', 'rb').read()                     # Manual decoding:
>>> X.decode('latin-1')                                    # Not necessary
'AÄBèC'
>>> X = open('utf8data', 'rb').read()
>>> X.decode()                                             # UTF-8 is default 
'AÄBèC'



>>> file = open('python.exe', 'r')
>>> text = file.read()
UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 2: ...

>>> file = open('python.exe', 'rb')
>>> data = file.read()
>>> data[:20]
b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00'



c:\misc> C:\Python30\python               # File saved in Notepad
>>> import sys
>>> sys.getdefaultencoding()
'utf-8'
>>> open('spam.txt', 'rb').read()         # ASCII (UTF-8) text file
b'spam\r\nSPAM\r\n'
>>> open('spam.txt', 'r').read()          # Text mode translates line-end
'spam\nSPAM\n'
>>> open('spam.txt', 'r', encoding='utf-8').read()
'spam\nSPAM\n'



>>> open('spam.txt', 'rb').read()         # UTF-8 with 3-byte BOM
b'\xef\xbb\xbfspam\r\nSPAM\r\n'
>>> open('spam.txt', 'r').read()
'ï»¿spam\nSPAM\n'
>>> open('spam.txt', 'r', encoding='utf-8').read()
'\ufeffspam\nSPAM\n'
>>> open('spam.txt', 'r', encoding='utf-8-sig').read()
'spam\nSPAM\n'



>>> open('spam.txt', 'rb').read()
b'\xfe\xff\x00s\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n'
>>> open('spam.txt', 'r').read()
UnicodeEncodeError: 'charmap' codec can't encode character '\xfe' in position 1:…
>>> open('spam.txt', 'r', encoding='utf-16').read()
'spam\nSPAM\n'
>>> open('spam.txt', 'r', encoding='utf-16-be').read()
'\ufeffspam\nSPAM\n'



>>> open('temp.txt', 'w', encoding='utf-8').write('spam\nSPAM\n')
10
>>> open('temp.txt', 'rb').read()                         # No BOM
b'spam\r\nSPAM\r\n'

>>> open('temp.txt', 'w', encoding='utf-8-sig').write('spam\nSPAM\n')
10
>>> open('temp.txt', 'rb').read()                         # Wrote BOM
b'\xef\xbb\xbfspam\r\nSPAM\r\n'

>>> open('temp.txt', 'r').read()
'ï»¿spam\nSPAM\n'
>>> open('temp.txt', 'r', encoding='utf-8').read()        # Keeps BOM
'\ufeffspam\nSPAM\n'
>>> open('temp.txt', 'r', encoding='utf-8-sig').read()    # Skips BOM
'spam\nSPAM\n'



>>> open('temp.txt', 'w').write('spam\nSPAM\n')
10
>>> open('temp.txt', 'rb').read()                         # Data without BOM
b'spam\r\nSPAM\r\n'
>>> open('temp.txt', 'r').read()                          # Any utf-8 works
'spam\nSPAM\n'
>>> open('temp.txt', 'r', encoding='utf-8').read()
'spam\nSPAM\n'
>>> open('temp.txt', 'r', encoding='utf-8-sig').read()
'spam\nSPAM\n'



>>> sys.byteorder
'little'
>>> open('temp.txt', 'w', encoding='utf-16').write('spam\nSPAM\n')
10
>>> open('temp.txt', 'rb').read()
b'\xff\xfes\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n\x00'
>>> open('temp.txt', 'r', encoding='utf-16').read()
'spam\nSPAM\n'

>>> open('temp.txt', 'w', encoding='utf-16-be').write('\ufeffspam\nSPAM\n')
11
>>> open('spam.txt', 'rb').read()
b'\xfe\xff\x00s\x00p\x00a\x00m\x00\r\x00\n\x00S\x00P\x00A\x00M\x00\r\x00\n'
>>> open('temp.txt', 'r', encoding='utf-16').read()
'spam\nSPAM\n'
>>> open('temp.txt', 'r', encoding='utf-16-be').read()
'\ufeffspam\nSPAM\n'



>>> open('temp.txt', 'w', encoding='utf-16-le').write('SPAM')
4
>>> open('temp.txt', 'rb').read()             # OK if BOM not present or expected
b'S\x00P\x00A\x00M\x00'
>>> open('temp.txt', 'r', encoding='utf-16-le').read()
'SPAM'
>>> open('temp.txt', 'r', encoding='utf-16').read()
UnicodeError: UTF-16 stream does not start with BOM



C:\misc> c:\python26\python
>>> S = u'A\xc4B\xe8C'
>>> print S
AÄBèC
>>> len(S)
5
>>> S.encode('latin-1')
'A\xc4B\xe8C'
>>> S.encode('utf-8')
'A\xc3\x84B\xc3\xa8C'

>>> import codecs
>>> codecs.open('latindata', 'w', encoding='latin-1').write(S)
>>> codecs.open('utfdata', 'w', encoding='utf-8').write(S)

>>> open('latindata', 'rb').read()
'A\xc4B\xe8C'
>>> open('utfdata', 'rb').read()
'A\xc3\x84B\xc3\xa8C'


# NOTE: recall from prior examples that that you must use "print" 
# to display the non-ascii characters in the following in non-hex 
# form (repr shows hex, but str displays the characters)


>>> codecs.open('latindata', 'r', encoding='latin-1').read()
u'A\xc4B\xe8C'
>>> codecs.open('utfdata', 'r', encoding='utf-8').read()
u'A\xc4B\xe8C'



C:\misc> c:\python30\python
>>> import re
>>> S = 'Bugger all down here on earth!'               # Line of text
>>> B = b'Bugger all down here on earth!'              # Usually from a file

>>> re.match('(.*) down (.*) on (.*)', S).groups()     # Match line to pattern
('Bugger all', 'here', 'earth!')                       # Matched substrings

>>> re.match(b'(.*) down (.*) on (.*)', B).groups()    # bytes substrings
(b'Bugger all', b'here', b'earth!')



C:\misc> c:\python26\python
>>> import re
>>> S = 'Bugger all down here on earth!'               # Simple text and binary
>>> U = u'Bugger all down here on earth!'              # Unicode text

>>> re.match('(.*) down (.*) on (.*)', S).groups()
('Bugger all', 'here', 'earth!')

>>> re.match('(.*) down (.*) on (.*)', U).groups()
(u'Bugger all', u'here', u'earth!')



C:\misc> c:\python30\python
>>> import re
>>> S = 'Bugger all down here on earth!'
>>> B = b'Bugger all down here on earth!'

>>> re.match('(.*) down (.*) on (.*)', B).groups()
TypeError: can't use a string pattern on a bytes-like object

>>> re.match(b'(.*) down (.*) on (.*)', S).groups()
TypeError: can't use a bytes pattern on a string-like object

>>> re.match(b'(.*) down (.*) on (.*)', bytearray(B)).groups()
(bytearray(b'Bugger all'), bytearray(b'here'), bytearray(b'earth!'))

>>> re.match('(.*) down (.*) on (.*)', bytearray(B)).groups()
TypeError: can't use a string pattern on a bytes-like object



C:\misc> c:\python30\python
>>> from struct import pack
>>> pack('>i4sh', 7, 'spam', 8)         # bytes in 3.0 (8-bit string)
b'\x00\x00\x00\x07spam\x00\x08'

C:\misc> c:\python26\python
>>> from struct import pack
>>> pack('>i4sh', 7, 'spam', 8)         # str in 2.6 (8-bit string)
'\x00\x00\x00\x07spam\x00\x08'



C:\misc> c:\python30\python
>>> import struct
>>> B = struct.pack('>i4sh', 7, 'spam', 8)
>>> B
b'\x00\x00\x00\x07spam\x00\x08'

>>> vals = struct.unpack('>i4sh', B)
>>> vals
(7, b'spam', 8)

>>> vals = struct.unpack('>i4sh', B.decode())
TypeError: 'str' does not have the buffer interface



C:\misc> c:\python30\python

# Write values to a packed binary file

>>> F = open('data.bin', 'wb')                  # Open binary output file
>>> import struct
>>> data = struct.pack('>i4sh', 7, 'spam', 8)   # Create packed binary data
>>> data                                        # bytes in 3.0, not str
b'\x00\x00\x00\x07spam\x00\x08'
>>> F.write(data)                               # Write to the file
10
>>> F.close()

# Read values from a packed binary file

>>> F = open('data.bin', 'rb')                  # Open binary input file
>>> data = F.read()                             # Read bytes
>>> data
b'\x00\x00\x00\x07spam\x00\x08'
>>> values = struct.unpack('>i4sh', data)       # Extract packed binary data
>>> values                                      # Back to Python objects
(7, b'spam', 8)



>>> values                                      # Result of struct.unpack
(7, b'spam', 8)

# Accesssing bits of parsed integers

>>> bin(values[0])                              # Can get to bits in ints
'0b111'
>>> values[0] & 0x01                            # Test first (lowest) bit in int
1
>>> values[0] | 0b1010                          # Bitwise or: turn bits on 
15
>>> bin(values[0] | 0b1010)                     # 15 decimal is 1111 binary
'0b1111'
>>> bin(values[0] ^ 0b1010)                     # Bitwise xor: off if both true 
'0b1101'
>>> bool(values[0] & 0b100)                     # Test if bit 3 is on
True
>>> bool(values[0] & 0b1000)                    # Test if bit 4 is set
False



# Accesing bytes of parsed strings and bits within them

>>> values[1]
b'spam'
>>> values[1][0]                          # bytes string: sequence of ints 
115
>>> values[1][1:]                         # Prints as ASCII characters
b'pam'
>>> bin(values[1][0])                     # Can get to bits of bytes in strings
'0b1110011'
>>> bin(values[1][0] | 0b1100)            # Turn bits on
'0b1111111'
>>> values[1][0] | 0b1100
127



C:\misc> C:\Python30\python
>>> import pickle                          # dumps() returns pickle string

>>> pickle.dumps([1, 2, 3])                # Python 3.0 default protocol=3=binary
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'

>>> pickle.dumps([1, 2, 3], protocol=0)    # ASCII protocol 0, but still bytes!
b'(lp0\nL1L\naL2L\naL3L\na.'



>>> pickle.dump([1, 2, 3], open('temp', 'w'))    # Text files fail on bytes!
TypeError: can't write bytes to text stream      # Despite protocol value

>>> pickle.dump([1, 2, 3], open('temp', 'w'), protocol=0)
TypeError: can't write bytes to text stream

>>> pickle.dump([1, 2, 3], open('temp', 'wb'))   # Always use binary in 3.0

>>> open('temp', 'r').read()
UnicodeEncodeError: 'charmap' codec can't encode character '\u20ac' in ...



>>> pickle.dump([1, 2, 3], open('temp', 'wb'))
>>> pickle.load(open('temp', 'rb'))
[1, 2, 3]
>>> open('temp', 'rb').read()
b'\x80\x03]q\x00(K\x01K\x02K\x03e.'



C:\misc> c:\python26\python
>>> import pickle
>>> pickle.dumps([1, 2, 3])                      # Python 2.6 default=0=ASCII
'(lp0\nI1\naI2\naI3\na.'

>>> pickle.dumps([1, 2, 3], protocol=1)
']q\x00(K\x01K\x02K\x03e.'

>>> pickle.dump([1, 2, 3], open('temp', 'w'))    # Text mode works in 2.6
>>> pickle.load(open('temp'))
[1, 2, 3]
>>> open('temp').read()
'(lp0\nI1\naI2\naI3\na.'



>>> import pickle
>>> pickle.dump([1, 2, 3], open('temp', 'wb'))     # Version neutral
>>> pickle.load(open('temp', 'rb'))                # And required in 3.0
[1, 2, 3]



### file: mybooks.xml

<books>
    <date>2009</date>
    <title>Learning Python</title>
    <title>Programming Python</title>
    <title>Python Pocket Reference</title>
    <publisher>O'Reilly Media</publisher>
</books>



#### File: patternparse.py

import re
text  = open('mybooks.xml').read()
found = re.findall('<title>(.*)</title>', text)
for title in found: print(title)



### File: domparse.py

from xml.dom.minidom import parse, Node
xmltree = parse('mybooks.xml')
for node1 in xmltree.getElementsByTagName('title'):
    for node2 in node1.childNodes:
         if node2.nodeType == Node.TEXT_NODE:
             print(node2.data)



### File: saxparse.py

import xml.sax.handler
class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.inTitle = False
    def startElement(self, name, attributes):
        if name == 'title':
            self.inTitle = True
    def characters(self, data):
        if self.inTitle:
            print(data)
    def endElement(self, name):
        if name == 'title':
            self.inTitle = False

import xml.sax
parser = xml.sax.make_parser()
handler = BookHandler()
parser.setContentHandler(handler)
parser.parse('mybooks.xml')



### File: etreeparse.py

from xml.etree.ElementTree import parse
tree = parse('mybooks.xml') 
for E in tree.findall('title'):
    print(E.text)



C:\misc> c:\python26\python domparse.py
Learning Python
Programming Python
Python Pocket Reference

C:\misc> c:\python30\python domparse.py
Learning Python
Programming Python
Python Pocket Reference



C:\misc> c:\python30\python
>>> from xml.dom.minidom import parse, Node
>>> xmltree = parse('mybooks.xml')
>>> for node in xmltree.getElementsByTagName('title'):
...     for node2 in node.childNodes:
...         if node2.nodeType == Node.TEXT_NODE:
...             node2.data
...
'Learning Python'
'Programming Python'
'Python Pocket Reference'

C:\misc> c:\python26\python
>>> ...same code...
...
u'Learning Python'
u'Programming Python'
u'Python Pocket Reference'




