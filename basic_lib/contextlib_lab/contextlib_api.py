#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2010 Doug Hellmann.  All rights reserved.
#
"""Implementing the context manager API by hand.
    上下文管理器的_exit_总会执行即使产生异常
    上下文管理器与with语句 是try:finally的一种更紧凑的写法
"""
#end_pymotw_header

class Context(object):
    def __init__(self):
        print '__init__()'
    def __enter__(self):
        print '__enter__()'
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print '__exit__()'
        
with Context():
    print 'Doing work in the context'   #上下文管理器的_exit_总会执行即使产生异常


#
# __init__()
# __enter__()
# Doing work in the context
# __exit__()
