import threading
import logging
import time
logging.basicConfig(
	level=logging.DEBUG,
	format = '(%(threadName)-10s) %(message)s'
	)

def consumer(cond):
	logging.debug('Starting consumer thread')
	t = threading.currentThread()
	with cond:
		cond.wait()
		logging.debug('Resource is available to consumer')
def producer(cond):
	logging.debug('Starting producer thread')
	with cond:
		logging.debug('Making resource avaiable')
		cond.notifyAll()


condition = threading.Condition()
c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
p = threading.Thread(name='c3', target=producer, args=(condition,))

c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()

