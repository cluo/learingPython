__author__ = 'admin'
import random
import threading
import time
import logging

logging.basicConfig(
	level =logging.DEBUG,
	format ='(%(threadName)-10s) %(message)s'
)

def worker():
	t = threading.currentThread()
	parse = random.randint(1,5)
	logging.debug('sleeping %s',parse)
	time.sleep(parse)
	logging.debug('ending')
	return

for i in xrange(3):
	t = threading.Thread(target=worker)
	t.setDaemon(True)
	t.start()

main_thread = threading.currentThread()
print(threading.enumerate())
for t in threading.enumerate():
	if t is main_thread:
		continue
	logging.debug('joining %s', t.getName())
	t.join()


