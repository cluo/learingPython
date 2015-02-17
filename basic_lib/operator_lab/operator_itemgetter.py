#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
"""

__version__ = "$Id$"
#end_pymotw_header

from operator import *

l = [ dict(val=-1 * i) for i in xrange(4) ]
print 'Dictionaries:', l
# Dictionaries: [{'val': 0}, {'val': -1}, {'val': -2}, {'val': -3}]

g = itemgetter('val')   #字典操作
vals = [ g(i) for i in l ]
print '      values:', vals
print '      sorted:', sorted(l, key=g)
print
#       values: [0, -1, -2, -3]
#       sorted: [{'val': -3}, {'val': -2}, {'val': -1}, {'val': 0}]


l = [ (i, i*-2) for i in xrange(4) ]
print 'Tuples      :', l
# Tuples      : [(0, 0), (1, -2), (2, -4), (3, -6)]

g = itemgetter(1)   #元组操作
vals = [ g(i) for i in l ]
print '      values:', vals
print '      sorted:', sorted(l, key=g)


#       values: [0, -2, -4, -6]
#       sorted: [(3, -6), (2, -4), (1, -2), (0, 0)]