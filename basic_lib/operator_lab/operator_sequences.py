#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
序列操作
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

a = [ 1, 2, 3 ]
b = [ 'a', 'b', 'c' ]

print 'a =', a
print 'b =', b

print '\nConstructive:'
print '  concat(a, b):', concat(a, b)
print '  repeat(a, 3):', repeat(a, 3)
# Constructive:
#   concat(a, b): [1, 2, 3, 'a', 'b', 'c']
#   repeat(a, 3): [1, 2, 3, 1, 2, 3, 1, 2, 3]
#

print '\nSearching:'
print '  contains(a, 1)  :', contains(a, 1)
print '  contains(b, "d"):', contains(b, "d")
print '  countOf(a, 1)   :', countOf(a, 1)
print '  countOf(b, "d") :', countOf(b, "d")
print '  indexOf(a, 5)   :', indexOf(a, 1)

# Searching:
#   contains(a, 1)  : True
#   contains(b, "d"): False
#   countOf(a, 1)   : 1
#   countOf(b, "d") : 0
#   indexOf(a, 5)   : 0



print '\nAccess Items:'
print '  getitem(b, 1)            :', getitem(b, 1)
print '  getslice(a, 1, 3)        :', getslice(a, 1, 3)
print '  setitem(b, 1, "d")       :', setitem(b, 1, "d"),
print ', after b =', b
print '  setslice(a, 1, 3, [4, 5]):', setslice(a, 1, 3, [4, 5]),
print ', after a =', a

# Access Items:
#   getitem(b, 1)            : b
#   getslice(a, 1, 3)        : [2, 3]
#   setitem(b, 1, "d")       : None , after b = ['a', 'd', 'c']
#   setslice(a, 1, 3, [4, 5]): None , after a = [1, 4, 5]
#


print '\nDestructive:'
print '  delitem(b, 1)    :', delitem(b, 1), ', after b =', b
print '  delslice(a, 1, 3):', delslice(a, 1, 3), ', after a =', a
a = [1, 2, 3]
b = ['a', 'b', 'c']
# Destructive:
#   delitem(b, 1)    : None , after b = ['a', 'c']
#   delslice(a, 1, 3): None , after a = [1]
