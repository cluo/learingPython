#-*- coding:utf8 -*-
__author__ = 'admin'
import threading
import time
import logging
#用event同步线程
#事件对象是实现线程间通信的简单方法(多个线程同步操作时)
#Event管理一个内部标记 调用者可以用set() clear()方法控制这个标志
#其他线程可以用wait()暂停知道遇到这个标记,允许继续之前阻塞线程运行
# 事件运行时线程通信的埋点,主线程的变量可以看作是运行后的？
logging.basicConfig(level=logging.DEBUG,
					format='(%(threadN‰           ame)-10s) %(message)s')

def wait_for_event(e):
	logging.debug('wait_for_event starting')
	event_is_set = e.wait() #永久阻塞 知道设置标志位
	logging.debug('event set %s',event_is_set)

def wait_for_event_timeout(e, t):
	while not e.isSet():
		logging.debug('wait_for_event_timeout starting')
		event_is_set = e.wait(t) #定时阻塞
		logging.debug('event set: %s',event_is_set)
		if event_is_set:
			logging.debug('processing event')
		else:
			logging.debug('doing other work')

e = threading.Event()
t1 = threading.Thread(name='block',
					  target=wait_for_event,
					 args=(e,))
t1.start()
t2 = threading.Thread(name='nonblock',
					  target=wait_for_event_timeout,
					  args=(e,2))
t2.start()

logging.debug('Waiting before calling Event se‰t()')
time.sleep(3)
e.set()
logging.debug('Event is set')