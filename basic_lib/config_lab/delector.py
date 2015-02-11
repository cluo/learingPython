__author__ = 'admin'
import time

def foo():
	start = time.clock()
	print 'in foo()'
	end = time.clock()
	print 'used',end - start
foo()


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
def foo3():
	print 'in foo3()'
foo3()
