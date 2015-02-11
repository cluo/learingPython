__author__ = 'admin'

import sys
import inspect

def foo(): pass
class Cat(object):
	def __init__(self, name='kitty'):
		self.name = name
	def sayHi(self):
		print self.name

cat = Cat()
cat.sayHi()

if hasattr(cat, 'name'):
	setattr(cat ,'name', 'trigger')
print getattr(cat, 'name')
getattr(cat,'sayHi')()
print dir(cat)

import fnmatch as m
print m.__doc__.splitlines()[0]
print m.__name__
print m.__file__
print m.__dict__.items()[0]


print Cat.__doc__
print Cat.__name__
print Cat.__module__
print Cat.__dict__


print cat.__dict__
print cat.__class__
print cat.__class__ == Cat