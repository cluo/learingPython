print 4.0e+2
print 021
print 0x1f
print abs(-77)
print pow(3,2)
print hex(13)
print oct(13)
print bin(13)

if 2 != 3:
    print 'not'
if 2 in (2, 3, 4, 6):
    print 'yes'
if 2 not in (2, 3, 4, 6):
    print 'no'
bCluo = bin(1010)
print bCluo
#print bCluo
#cluocluo = ~bCluo
#print cluocluo
print 3 ** 2
he = [1, 2, 3, 4, 5]
print he[1:3]
print int(3.14)
print float(3)
num = 1/0.333
print num
print '%e' % num

print '%4.2f' % num
print '{0:4.2f}'.format(num)


#floor div

print 10/4.0
print 10//4.0
import math
print math.floor(2.5)
print math.floor(-2.5)

print math.trunc(2.5)
print math.trunc(-2.5)


#int
print 012
print 0x11
print 0b0101
print int('0x40',16)
print int ('0b1101',2);
print int('0x2f',16)
print int ('032',8)

#format
print '{0:o},{1:x},{2:b}'.format(64,64,64)
print '%o, %x, %X' %(64, 255, 255)

#oct 00
print 0012
