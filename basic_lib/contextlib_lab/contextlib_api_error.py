#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Implementing the context manager API by hand.
   如果想啥文管理器可以处理这个异常
    __exit__() 应当返回一个true值 来指示不需要传播这个异常
   如果返回一个false 会导致__exit__()返回重新抛出这个异常
"""
#end_pymotw_header

class Context(object):
    def __init__(self, handle_error):
        print '__init__(%s)' % handle_error
        self.handle_error = handle_error
    def __enter__(self):
        print '__enter__()'
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__()'
        print '  exc_type =', exc_type
        print '  exc_val  =', exc_val
        print '  exc_tb   =', exc_tb
        return self.handle_error
        
with Context(True):
    raise RuntimeError('error message handled')  #__exit__ 返回true 不抛出异常

print

with Context(False):
    raise RuntimeError('error message propagated')#__exit__ 返回false抛出异常
