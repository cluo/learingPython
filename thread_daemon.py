__author__ = 'admin'
import logging
import threading
import time
logging.basicConfig(
	level=logging.DEBUG,
	format='[%(levelname)s](%(threadName)-10s) %(message)s'
)

def daemon():
	logging.debug('Starting')
	time.sleep(2)
	logging.debug('Exting')
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
	logging.debug('Starting')
	logging.debug('Exiting')
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

d.join(2.1)
print 'd.isAlive()', d.isAlive()
t.join()


