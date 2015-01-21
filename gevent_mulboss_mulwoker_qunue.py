__author__ = 'admin'
import gevent
from gevent.queue import Queue, Empty

tasks = Queue(maxsize=3)
def worker(n):
	try:
		while True:
			task = tasks.get(timeout=1)
			print('Worker %s got task %s' % (n, task))
			gevent.sleep(0)
	except Empty:
		print('Quitting time !')
def boss():
	for i in xrange(1,10):
		tasks.put(i)
		print('boss put 1')
	print('Assigned all work in iteration 1')
	for i in xrange(1,20):
		tasks.put(i)
		print('boss put 2')
	print('Assigned all work in iteration 2')

gevent.joinall([
	gevent.spawn(boss),
	gevent.spawn(worker,'steve'),
	gevent.spawn(worker, 'cluo'),
	gevent.spawn(worker, 'bob')
])