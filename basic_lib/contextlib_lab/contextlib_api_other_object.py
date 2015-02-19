#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Implementing the context manager API by hand.
   如果在with 语句的as子句指定名称 __enter__可以返回与这个名称相关联的任何对象
"""
#end_pymotw_header

class WithinContext(object):
    def __init__(self, context):
        print 'WithinContext.__init__(%s)' % context
    def do_something(self):
        print 'WithinContext.do_something()'
    def __del__(self):
        print 'WithinContext.__del__'

class Context(object):
    def __init__(self):
        print 'Context.__init__()'
    def __enter__(self):
        print 'Context.__enter__()'
        return WithinContext(self)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'Context.__exit__()'
    
with Context() as c:
    c.do_something()

# Context.__init__()
# Context.__enter__()
# WithinContext.__init__(<__main__.Context object at 0x1004fbc10>)
# WithinContext.do_something()
# Context.__exit__()
# WithinContext.__del__