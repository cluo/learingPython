__author__ = 'admin'
import gevent
from gevent.event import AsyncResult
a = AsyncResult()
def setter():
	gevent.sleep(3)
	a.set('hello')
def waiter():
	print(a.get())
gevent.joinall([
	gevent.spawn(setter),
	gevent.spawn(waiter)
])

