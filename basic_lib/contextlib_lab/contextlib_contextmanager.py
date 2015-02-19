#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""
$Id$
contextmanager()修饰符将一个生成器函数转换成上下文管理器
"""
#end_pymotw_header
import contextlib

@contextlib.contextmanager
def make_context():
    print '  entering'
    try:
        yield {}   #生成器初始化上下文 用yield 生成一次值,然后清理上下文,所生成的值 绑定到with  语句 as 的变量
                   #with 中的异常会在生成器中重新抛出,使之在生成器中得到处理
    except RuntimeError, err:   #这里只捕获 RuntimeError错误
        print '  ERROR:', err
    finally:
        print '  exiting'



print 'Normal:'
with make_context() as value:
    print '  inside with statement:', value


# Normal:
#   entering
#   inside with statement: {}
#   exiting
#



print '\nHandled error:'
with make_context() as value:
    raise RuntimeError('showing example of handling an error')

# Handled error:
#   entering
#   ERROR: showing example of handling an error
#   exiting

print '\nUnhandled error:'
with make_context() as value:
    raise ValueError('this exception is not handled')

# Unhandled error:
#   entering
#   exiting

