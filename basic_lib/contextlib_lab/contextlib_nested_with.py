#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
$Id$
 ，号分割  嵌套上下文 正确事项有关错误处理的边界情况
"""
#end_pymotw_header
import contextlib

@contextlib.contextmanager
def make_context(name):
    print 'entering:', name
    yield name
    print 'exiting :', name

with make_context('A') as A, make_context('B') as B:
    print 'inside with statement:', A, B

# entering: A
# entering: B
# inside with statement: A B
# exiting : B
# exiting : A