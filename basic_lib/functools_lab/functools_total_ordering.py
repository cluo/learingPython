#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Use total_ordering decorator to fill in missing rich comparison methods.
   用total_ordering 为类补全 __lt__() __le__() __eq__() __ne__() __gt__() __ge__()
"""
#end_pymotw_header

import functools
import inspect
from pprint import pprint


@functools.total_ordering
class MyObject(object):
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        print '  testing __eq__(%s, %s)' % (self.val, other.val)
        return self.val == other.val
    def __gt__(self, other):
        print '  testing __gt__(%s, %s)' % (self.val, other.val)
        return self.val > other.val

print 'Methods:\n'
pprint(inspect.getmembers(MyObject, inspect.ismethod))
# Methods:
#
# [('__eq__', <unbound method MyObject.__eq__>),
#  ('__ge__', <unbound method MyObject.__ge__>),
#  ('__gt__', <unbound method MyObject.__gt__>),
#  ('__init__', <unbound method MyObject.__init__>),
#  ('__le__', <unbound method MyObject.__le__>),
#  ('__lt__', <unbound method MyObject.__lt__>)]
a = MyObject(1)
b = MyObject(2)

print '\nComparisons:'
for expr in [ 'a < b', 'a <= b', 'a == b', 'a >= b', 'a > b' ]:
    print '\n%-6s:' % expr
    result = eval(expr)
    print '  result of %s: %s' % (expr, result)
# Comparisons:
#
# a < b :
#   testing __gt__(1, 2)
#   testing __eq__(1, 2)
#   result of a < b: True
#
# a <= b:
#   testing __gt__(1, 2)
#   result of a <= b: True
#
# a == b:
#   testing __eq__(1, 2)
#   result of a == b: False
#
# a >= b:
#   testing __gt__(1, 2)
#   testing __eq__(1, 2)
#   result of a >= b: False
#
# a > b :
#   testing __gt__(1, 2)
#   result of a > b: False