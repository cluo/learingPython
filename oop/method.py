#!/usr/bin/evn python
#-*- coding:utf-8 -*-
__author__ = 'admin'
#类静态变量
class NextClass:
	def printer(self,text):
		self.message = text
		print(self.message)

x = NextClass()
x.printer('instance call')

NextClass.printer(x,'class call')







