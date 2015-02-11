#-*- coding:utf8 -*-
__author__ = 'admin'

import logging
import threading
import time
logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s] %(message)s'
)

def daemon():
	logging.debug('Starting')
	time.sleep(3)
	logging.debug('Exting')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
	logging.debug('Starting')
	logging.debug('Exiting')
	time.sleep(5)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
start = time.time()
d.join(1.1)
t.join(1.1)
end = time.time()
print (end - start) #join所有线程

print 'd.isAlive()', d.isAlive()
print 't.isAlive()', t.isAlive()



