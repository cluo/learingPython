__author__ = 'admin'
import gevent
from gevent import Timeout
time_to_wait = 5

class TooLong(Exception):
	pass

with Timeout(time_to_wait, TooLong):
	gevent.sleep(10)
