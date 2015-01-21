__author__ = 'admin'
from contextlib import contextmanager
from __future__ import with_statement
@contextmanager
def context():
	print 'entering the zone'
	try:
		yield
	except Exception,e:
		print 'with an error %s ' % e
		raise e
	else:
		print 'with no error'
with context:
	print '--------in context call ----------'