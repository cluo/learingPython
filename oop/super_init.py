#!/usr/bin/evn python
#-*- coding:utf-8 -*-
__author__ = 'admin'
#类静态变量
class Super:
	def __init__(self,x):
		self.key = x
class Sub(Super):
	def __init__(self,x,y):
		Super.__init__(self,x)
		self.value = y

super1 = Super('key')
print super1.key

sub = Sub('key','value')
print sub.key
print sub.value

#一定要带object
class A(object):
	def __init__(self,x=None):
		self.key = x

class B(A):
	def __init__(self,x,y):
		super(B, self).__init__(x)
		self.value = y

a = A('key')
b = B('key1','value1')

print a.key
print b.key,b.value
