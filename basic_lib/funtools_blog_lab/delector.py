#-*- coding:utf8 -*-
__author__ = 'admin'
"""装饰器"""

import time

def foo():
	start = time.clock()
	print 'in foo()'
	end = time.clock()
	print 'used',end - start
foo()


#装饰器 在保持函数 接口（输入输出）不变的情况下 扩展函数
def foo1():
	print 'in foo1'
def timeit(func):
	start = time.clock()
	func()
	end = time.clock()
	print 'used:', end - start

timeit(foo1)


def foo2():
	print 'in foo2()'

#函数返回 扩展后的函数
def timeit(func):
	def wrapper():
		start = time.clock()
		func()
		end = time.clock()
		print 'used:',end - start
	return wrapper

foo2 = timeit(foo2)
foo2()




def timeit(func):
	def wrapper():
		start = time.clock()
		func()
		end = time.clock()
		print 'used:',end - start
	return wrapper

@timeit
def foo3(): #相当于  foo3 = timit(foo3)
	print 'in foo3()'

foo3()
