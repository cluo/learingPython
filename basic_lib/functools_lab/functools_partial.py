#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
functools.partial 重设必填默认值
p1 = functools.partial(myfunc, b=4) #重设必填默认值
"""

__version__ = "$Id$"
#end_pymotw_header

import functools



def myfunc(a, b=2):
    """Docstring for myfunc()."""
    print '  called myfunc with:', (a, b)
    return

def show_details(name, f, is_partial=False):
    """Show details of a callable object."""
    print '%s:' % name
    print '  object:', f
    if not is_partial:
        print '  __name__:', f.__name__
    if is_partial:
        print '  func:', f.func
        print '  args:', f.args
        print '  keywords:', f.keywords
    return

show_details('myfunc', myfunc)
myfunc('a', 3)
# myfunc:
#   object: <function myfunc at 0x1006026e0>
#   __name__: myfunc
#   called myfunc with: ('a', 3)

print  #换行打印

# Set a different default value for 'b', but require
# the caller to provide 'a'.
p1 = functools.partial(myfunc, b=4) #重设必填默认值
show_details('partial with named default', p1, True)
# partial with named default:
#   object: <functools.partial object at 0x1005e02b8>
#   func: <function myfunc at 0x1006026e0>
#   args: ()
#   keywords: {'b': 4}

p1('passing a')
p1('override b', b=5)
#   called myfunc with: ('passing a', 4)
#   called myfunc with: ('override b', 5)
print



# Set default values for both 'a' and 'b'.
p2 = functools.partial(myfunc, 'default a', b=99)   #a,b都设置了必填的默认值
show_details('partial with defaults', p2, True)
# partial with defaults:
#   object: <functools.partial object at 0x1005e0310>
#   func: <function myfunc at 0x1006026e0>
#   args: ('default a',)
#   keywords: {'b': 99}

p2()
p2(b='override b')
#   called myfunc with: ('default a', 99)
#   called myfunc with: ('default a', 'override b')
print

print 'Insufficient arguments:'
p1()  #报错 漏传 a
