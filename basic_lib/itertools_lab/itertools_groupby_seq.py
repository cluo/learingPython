#!/usr/bin/env python
#-*- coding:utf8 -*-
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Grouping sequential values with groupby().
  先排序后分组

"""

__version__ = "$Id$"
#end_pymotw_header

from itertools import *
import operator
import pprint

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return '(%s, %s)' % (self.x, self.y)
    def __cmp__(self, other):
        return cmp((self.x, self.y), (other.x, other.y))

# Create a dataset of Point instances
data = list(imap(Point, 
                 cycle(islice(count(), 3)),   #循环生成0～2
                 islice(count(), 7),  #生成0~6
                 )
            )
print 'Data:'
pprint.pprint(data, width=69)
print
# Data:
# [(0, 0), (1, 1), (2, 2), (0, 3), (1, 4), (2, 5), (0, 6)]

# Try to group the unsorted data based on X values
print 'Grouped, unsorted:'
for k, g in groupby(data, operator.attrgetter('x')):
    print k, list(g)
print
#
# Grouped, unsorted:
# 0 [(0, 0)]
# 1 [(1, 1)]
# 2 [(2, 2)]
# 0 [(0, 3)]
# 1 [(1, 4)]
# 2 [(2, 5)]
# 0 [(0, 6)]
#


# Sort the data
data.sort() #默认按“key”排
print 'Sorted:'
pprint.pprint(data, width=69)
print

# Sorted:
# [(0, 0), (0, 3), (0, 6), (1, 1), (1, 4), (2, 2), (2, 5)]
#


# Group the sorted data based on X values
print 'Grouped, sorted:'
for k, g in groupby(data, operator.attrgetter('x')):
    print k, list(g)
print


# Grouped, sorted:
# 0 [(0, 0), (0, 3), (0, 6)]
# 1 [(1, 1), (1, 4)]
# 2 [(2, 2), (2, 5)]