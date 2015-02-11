#!/usr/bin/evn python
#-*- coding:utf-8 -*-
__author__ = 'admin'
#类静态变量
class ShareData:
	spam = 3

x = ShareData()
y = ShareData()

print x.spam
print y.spam
print ShareData.spam

ShareData.spam = 24

print x.spam
print y.spam
print ShareData.spam



class ShareData:
	data = "spam"
	def __init__(self, value):
		self.data = value #this
	def display(self):
		print(self.data, ShareData.data)

x1 = ShareData(1)
x2 = ShareData(2)

print x1.display()
print x2.display()






