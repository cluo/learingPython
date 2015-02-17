#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
    boolen测试 ，逻辑测试
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

a = -1
b = 5

print 'a =', a
print 'b =', b
print

print 'not_(a)     :', not_(a)
print 'truth(a)    :', truth(a)
print 'is_(a, b)   :', is_(a,b)
print 'is_not(a, b):', is_not(a,b)


# a = -1
# b = 5
#
# not_(a)     : False
# truth(a)    : True
# is_(a, b)   : False
# is_not(a, b): True