#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
获取对象属性
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

class MyObj(object):
    """example class for attrgetter"""
    def __init__(self, arg):
        super(MyObj, self).__init__()
        self.arg = arg
    def __repr__(self):
        return 'MyObj(%s)' % self.arg

l = [ MyObj(i) for i in xrange(5) ]
print 'objects   :', l
# objects   : [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]

# Extract the 'arg' value from each object
g = attrgetter('arg')       #获取对象属性
vals = [ g(i) for i in l ]
print 'arg values:', vals
# arg values: [0, 1, 2, 3, 4]

# Sort using arg
l.reverse()
print 'reversed  :', l
print 'sorted    :', sorted(l, key=g)
# reversed  : [MyObj(4), MyObj(3), MyObj(2), MyObj(1), MyObj(0)]
# sorted    : [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]