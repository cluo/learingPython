__author__ = 'admin'
import gevent
from gevent import Greenlet
def foo(message, n):
	gevent.sleep(n)
	print message
thread1 =  Greenlet.spawn(foo,'hello', 1)
thread2 = gevent.spawn(foo,'I live', 2)
thread3 = gevent.spawn(lambda x: (x+1), 2)

threads = [thread1, thread2, thread3]
gevent.joinall(threads)

import gevent
from gevent import Greenlet
class MyGreenlet(Greenlet):
	def __init__(self, message, n):
		Greenlet.__init__(self)
		self.message = message
		self.n = n
	def _run(self):
		print(self.message)
		gevent.sleep(self.n)
g = MyGreenlet('hi there!',3)
g.start()
g.join()