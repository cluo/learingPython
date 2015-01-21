#-*- coding:utf8 -*-
__author__ = 'admin'
from contextlib import contextmanager
@contextmanager
def tag(name):
	print "<%s>" % name
	yield
	print "<%s>" % name
with tag("h1"):
	print "foo"
