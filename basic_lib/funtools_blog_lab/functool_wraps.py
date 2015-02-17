#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-9
__author__ = 'cluo'
from functools import wraps
def wrap3(func):
	@wraps(func) #相当于update_wrapper(func,call_it)
	def  call_it(*args, **kwargs):
		"""wrap func:call_it2"""
		print 'before call'
		return func(*args, **kwargs)
	return call_it

@wrap3
def hello3():
	"""test hello 3"""
	print 'hello world3'



hello3()
print hello3.__name__
print hello3.__module__
print hello3.__doc__