#-*- coding:utf8 -*-
__author__ = 'admin'
import random
import threading
import time
import logging
#列举所有线程
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
for t in threading.enumerate():   #列出当前所有线程 包括主线程
	if t is main_thread: #等待当前线程完成 会引入死锁必须跳过
		continue
	logging.debug('joining %s', t.getName())
	t.join()


