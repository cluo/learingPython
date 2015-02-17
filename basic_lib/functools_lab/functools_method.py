#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
    wrapped_method2 = functools.partial(method2, 'wrapped c')
    functools.update_wrapper(wrapped_method2, method2)
"""

__version__ = "$Id$"
#end_pymotw_header

import functools

class MyClass(object):
    """Demonstration class for functools"""
    
    def method1(self, a, b=2):
        """Docstring for method1()."""
        print '  called method1 with:', (self, a, b)
        return
    
    def method2(self, c, d=5):
        """Docstring for method2"""
        print '  called method2 with:', (self, c, d)
        return
    wrapped_method2 = functools.partial(method2, 'wrapped c')
    functools.update_wrapper(wrapped_method2, method2)
    
    def __call__(self, e, f=6):
        """Docstring for MyClass.__call__"""
        print '  called object with:', (self, e, f)
        return

def show_details(name, f):
    """Show details of a callable object."""
    print '%s:' % name
    print '  object:', f
    print '  __name__:', 
    try:
        print f.__name__
    except AttributeError:
        print '(no __name__)'
    print '  __doc__', repr(f.__doc__)
    return
    
o = MyClass()

show_details('method1 straight', o.method1)
o.method1('no default for a', b=3)
print

# method1 straight:
#   object: <bound method MyClass.method1 of <__main__.MyClass object at 0x100604950>>
#   __name__: method1
#   __doc__ 'Docstring for method1().'
#   called method1 with: (<__main__.MyClass object at 0x100604950>, 'no default for a', 3)


p1 = functools.partial(o.method1, b=4)
functools.update_wrapper(p1, o.method1)
show_details('method1 wrapper', p1)
p1('a goes here')
print

# method1 wrapper:
#   object: <functools.partial object at 0x1004e0368>
#   __name__: method1
#   __doc__ 'Docstring for method1().'
#   called method1 with: (<__main__.MyClass object at 0x100604950>, 'a goes here', 4)


show_details('method2', o.method2)
o.method2('no default for c', d=6)
print
# method2:
#   object: <bound method MyClass.method2 of <__main__.MyClass object at 0x100604950>>
#   __name__: method2
#   __doc__ 'Docstring for method2'
#   called method2 with: (<__main__.MyClass object at 0x100604950>, 'no default for c', 6)



show_details('wrapped method2', o.wrapped_method2)
o.wrapped_method2('no default for c', d=6)
print
# wrapped method2:
#   object: <functools.partial object at 0x1004e02b8>
#   __name__: method2
#   __doc__ 'Docstring for method2'
#   called method2 with: ('wrapped c', 'no default for c', 6)

show_details('instance', o)
o('no default for e')
print
# instance:
#   object: <__main__.MyClass object at 0x100604950>
#   __name__: (no __name__)
#   __doc__ 'Demonstration class for functools'
#   called object with: (<__main__.MyClass object at 0x100604950>, 'no default for e', 6)
p2 = functools.partial(o, f=7)
show_details('instance wrapper', p2)
p2('e goes here')
# instance wrapper:
#   object: <functools.partial object at 0x1004e03c0>
#   __name__: (no __name__)
#   __doc__ 'partial(func, *args, **keywords) - new function with partial application\n    of the given arguments and keywords.\n'
#   called object with: (<__main__.MyClass object at 0x100604950>, 'e goes here', 7)
