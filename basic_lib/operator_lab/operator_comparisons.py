#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
比较操作符号
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

a = 1
b = 5.0

print 'a =', a
print 'b =', b
# a = 1
# b = 5.0

for func in (lt, le, eq, ne, ge, gt):
    print '%s(a, b):' % func.__name__, func(a, b)
# lt(a, b): True
# le(a, b): True
# eq(a, b): False
# ne(a, b): True
# ge(a, b): False
# gt(a, b): False