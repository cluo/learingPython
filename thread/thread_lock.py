#-*- coding:utf8 -*-
__author__ = 'admin'

import logging
import random
import threading
import time
#python 内置数据结构(列表,字典)是线程安全,python 用原子字节码来管理这些数据结构的一个副作用更新过程不会释放GIL
#python 中的其他数据结构或者更简单的类型 整数和浮点数贼没有这个保护，要保证同时安全的访问对象可以使用Lock对象

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s')

class Counter():
	def __init__(self, start=0):
		self.lock = threading.Lock()
		self.value = start

	def increment(self):
		logging.debug('Waithing for lock')
		self.lock.acquire()
		try:
			logging.debug('Acquired lock')
			self.value = self.value  + 1
		finally:
			self.lock.release()

def worker(c):
	for i in range(2):
		pause = random.random()
		logging.debug('Sleeping %0.02f', pause)
		time.sleep(pause)
		c.increment()
	logging.debug('Done')

counter = Counter()
for i in range(2):
	t = threading.Thread(target=worker, args=(counter,))
	t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.currentThread()
for t in threading.enumerate():
		if t is not main_thread:  #跳过,主进程主塞会陷入死锁
				t.join()
logging.debug('Counter: %d', counter.value)




