#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
step1:
def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print '  decorated:', (a, b)
        print '  ',
        f(a, b=b)
        return
    return decorated

step2:
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return
"""

__version__ = "$Id$"
#end_pymotw_header

import functools

def show_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '  object:', f
    print '  __name__:',  #不换行
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '  __doc__', repr(f.__doc__)
    print
    return

def simple_decorator(f):
    @functools.wraps(f)
    def decorated(a='decorated defaults', b=1):
        print '  decorated:', (a, b)
        print '  ',
        f(a, b=b)
        return
    return decorated

def myfunc(a, b=2):
    "myfunc() is not complicated"
    print '  myfunc:', (a,b)
    return

# The raw function
show_details('myfunc', myfunc)
# myfunc:
#   object: <function myfunc at 0x100500c08>
#   __name__: myfunc
#   __doc__ 'myfunc() is not complicated'

myfunc('unwrapped, default b')
myfunc('unwrapped, passing b', 3)
print
#
#   myfunc: ('unwrapped, default b', 2)
#   myfunc: ('unwrapped, passing b', 3)


# Wrap explicitly
wrapped_myfunc = simple_decorator(myfunc)
show_details('wrapped_myfunc', wrapped_myfunc)
# wrapped_myfunc:
#   object: <function myfunc at 0x100500c80>
#   __name__: myfunc
#   __doc__ 'myfunc() is not complicated'
#
wrapped_myfunc()
#   decorated: ('decorated defaults', 1)
#      myfunc: ('decorated defaults', 1)
wrapped_myfunc('args to wrapped', 4)
#   decorated: ('args to wrapped', 4)
#      myfunc: ('args to wrapped', 4)
print




# Wrap with decorator syntax
@simple_decorator
def decorated_myfunc(a, b):
    myfunc(a, b)
    return

show_details('decorated_myfunc', decorated_myfunc)
# decorated_myfunc:
#   object: <function decorated_myfunc at 0x100500d70>
#   __name__: decorated_myfunc
#   __doc__ None
decorated_myfunc()
#   decorated: ('decorated defaults', 1)
#      myfunc: ('decorated defaults', 1)
decorated_myfunc('args to decorated', 4)
#   decorated: ('args to decorated', 4)
#      myfunc: ('args to decorated', 4)