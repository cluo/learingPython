#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
原地操作 +=
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

a = -1
b = 5.0
c = [ 1, 2, 3 ]
d = [ 'a', 'b', 'c']
print 'a =', a
print 'b =', b
print 'c =', c
print 'd =', d
print

# a = -1
# b = 5.0
# c = [1, 2, 3]
# d = ['a', 'b', 'c']
#

a = iadd(a, b)
print 'a = iadd(a, b) =>', a
print
# a = iadd(a, b) => 4.0
#

c = iconcat(c, d)
print 'c = iconcat(c, d) =>', c
# c = iconcat(c, d) => [1, 2, 3, 'a', 'b', 'c']