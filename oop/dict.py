#!/usr/bin/evn python
#-*- coding:utf-8 -*-
__author__ = 'admin'
class super1(object):
	def hello(self):
		self.data1 = 'spam'

class sub1(super1):
	def hola(self):
		self.data2 = 'egg'

x = sub1()
print x.__dict__ #非继承
print x.__class__
print sub1.__bases__
print super1.__bases__

x.hello()
print x.__dict__

x.hola()
print x.__dict__
print sub1.__dict__

class 	Number:
	def __init__(self, start):
		self.data = start
	def __sub__(self, other):
		return

