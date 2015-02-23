#-*- coding:utf8 -*-
__author__ = 'admin'

# 队列是一个排序的数据集合，它有常见的put / get操作， 但是它是以在Greenlet之间可以安全操作的方式来实现的。
#
# 举例来说，如果一个Greenlet从队列中取出一项，此项就不会被 同时执行的其它Greenlet再取到了。
# 如果需要，队列也可以阻塞在put或get操作上。
#
# put和get操作都有非阻塞的版本，put_nowait和get_nowait不会阻塞，
# 然而在操作不能完成时抛出gevent.queue.Empty或gevent.queue.Full异常。
#
# 在下面例子中，我们让boss与多个worker同时运行，并限制了queue不能放入多于3个元素。
# 这个限制意味着，直到queue有空余空间之间，put操作会被阻塞。相反地，如果队列中 没有元素，
# get操作会被阻塞。它同时带一个timeout参数，允许在超时时间内如果
# 队列没有元素无法完成操作就抛出gevent.queue.Empty异常。
import gevent
from gevent.queue import Queue
tasks = Queue()
def worker(n):
	while not tasks.empty():
		task = tasks.get()
		print('Worker %s got task %s' % (n, task))
		gevent.sleep(0)
	print('Quitting time')
def boss():
	for i in xrange(1,25):
		tasks.put_nowait(i)
gevent.spawn(boss).join()
gevent.joinall([
	gevent.spawn(worker, 'steve'),
	gevent.spawn(worker, 'join'),
	gevent.spawn(worker, 'cluo')
])



# Worker steve got task 1
# Worker join got task 2
# Worker cluo got task 3
# Worker steve got task 4
# Worker join got task 5
# Worker cluo got task 6
# Worker steve got task 7
# Worker join got task 8
# Worker cluo got task 9
# Worker steve got task 10
# Worker join got task 11
# Worker cluo got task 12
# Worker steve got task 13
# Worker join got task 14
# Worker cluo got task 15
# Worker steve got task 16
# Worker join got task 17
# Worker cluo got task 18
# Worker steve got task 19
# Worker join got task 20
# Worker cluo got task 21
# Worker steve got task 22
# Worker join got task 23
# Worker cluo got task 24
# Quitting time
# Quitting time
# Quitting time