#!/usr/bin/evn python
#-*- coding:utf-8 -*-

__author__ = 'admin'
class A:
	def method(self):
		print('in super.method')
class B(A):
	def method(self):
		print('starting sub.method')
		A.method(self)
		print('ending sub.method')

x = A()
y = B()
x.method()
y.method()



#一定要带object
class C(object):
	def method(self):
		print('in super.method')
class D(C):
	def method(self):
		print('starting sub.method')
		super(D,self).method()
		print('ending sub.method')

x = C()
y = D()
x.method()
y.method()



