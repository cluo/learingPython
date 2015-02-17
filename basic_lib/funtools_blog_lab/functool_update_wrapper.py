#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-9
__author__ = 'cluo'


from functools import update_wrapper
def wrap(func):
	def call_it(*args, **kwargs):
		"""wrap func: call_it"""
		print 'before call'
		return func(*args, **kwargs)
	return call_it

@wrap
def hello():
	"""say hello"""
	print 'hello world'



# 默认partial对象没有__name__和__doc__, 这种情况下，对于装饰器函数非常难以debug.
# 使用update_wrapper(),从原始对象拷贝或加入现有partial对象
#
# 它可以把被封装函数的__name__、module、__doc__和 __dict__都复制到封装函数去
# (模块级别常量WRAPPER_ASSIGNMENTS, WRAPPER_UPDATES)


def wrap2(func):
	def call_it(*args, **kwargs):
		"""wrap func: call_it2"""
		print 'before call'
		return func(*args, **kwargs)
	return update_wrapper(call_it, func)

@wrap2
def hello2():
	"""test hello """
	print 'hello world2'

if __name__ == '__main__':
	hello()
	print hello.__name__
	print hello.__doc__

	hello2()
	print hello2.__name__
	print hello2.__doc__



