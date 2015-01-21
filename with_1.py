#-*- coding:utf8 -*-
__author__ = 'admin'
with open('cluo') as f:
	print f.readlines()

class A:
	def __enter__(self):
		print 'in enter'
	def __exit__(self, e_t, e_v, e_b):
		print 'in exit'
with A() as a:
	print 'in_with'
