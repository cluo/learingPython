#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
$Id$
"""
#end_pymotw_header
import contextlib

class Door(object):
    def __init__(self):
        print '  __init__()'
    def close(self):        #为不支持上下文管理器的close 创建上下文管理器（退出时自动调用close）
        print '  close()'

print 'Normal Example:'
with contextlib.closing(Door()) as door:
    print '  inside with statement'
# Normal Example:
#   __init__()
#   inside with statement
#   close()
#

print '\nError handling example:'
try:
    with contextlib.closing(Door()) as door:  #用contextlib.closing() 为它创建一个上下文管理器
        print '  raising from inside with statement'
        raise RuntimeError('error message')
except Exception, err:
    print '  Had an error:', err


# Error handling example:
#   __init__()
#   raising from inside with statement
#   close()
#   Had an error: error message
