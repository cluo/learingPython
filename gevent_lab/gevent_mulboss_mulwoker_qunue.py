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



# boss put 1
# boss put 1
# boss put 1
# Worker steve got task 1
# Worker cluo got task 2
# Worker bob got task 3
# boss put 1
# boss put 1
# boss put 1
# Worker steve got task 4
# Worker cluo got task 5
# Worker bob got task 6
# boss put 1
# boss put 1
# boss put 1
# Assigned all work in iteration 1
# Worker steve got task 7
# Worker cluo got task 8
# Worker bob got task 9
# boss put 2
# boss put 2
# boss put 2
# Worker steve got task 1
# Worker cluo got task 2
# Worker bob got task 3
# boss put 2
# boss put 2
# boss put 2
# Worker steve got task 4
# Worker cluo got task 5
# Worker bob got task 6
# boss put 2
# boss put 2
# boss put 2
# Worker steve got task 7
# Worker cluo got task 8
# Worker bob got task 9
# boss put 2
# boss put 2
# boss put 2
# Worker steve got task 10
# Worker cluo got task 11
# Worker bob got task 12
# boss put 2
# boss put 2
# boss put 2
# Worker steve got task 13
# Worker cluo got task 14
# Worker bob got task 15
# boss put 2
# boss put 2
# boss put 2
# Worker steve got task 16
# Worker cluo got task 17
# Worker bob got task 18
# boss put 2
# Assigned all work in iteration 2
# Worker steve got task 19
# Quitting time !
# Quitting time !
# Quitting time !
