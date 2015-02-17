#!/usr/bin/env python
#
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

"""Using groupby()

"""

__version__ = "$Id$"
#end_pymotw_header

from itertools import *
from operator import itemgetter

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
print d
#{'a': 1, 'c': 1, 'b': 2, 'e': 1, 'd': 2, 'g': 3, 'f': 2}

di = sorted(d.iteritems(), key=itemgetter(1))
print di
#[('a', 1), ('c', 1), ('e', 1), ('b', 2), ('d', 2), ('f', 2), ('g', 3)]

for k, g in groupby(di, key=itemgetter(1)):
    print k, map(itemgetter(0), g)

# 1 ['a', 'c', 'e']
# 2 ['b', 'd', 'f']
# 3 ['g']

for g in groupby(di, key=itemgetter(1)):
    print g
# (1, <itertools._grouper object at 0x100609290>)
# (2, <itertools._grouper object at 0x1006091d0>)
# (3, <itertools._grouper object at 0x100609290>)
