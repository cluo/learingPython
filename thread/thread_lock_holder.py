_author__ = 'admin'
import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s')

def lock_holder(lock):
	logging.debug('starting')
	while True:
		lock.acquire()
		try:
			logging.debug('Holding')
			time.sleep(0.5)
		finally:
			logging.debug('not holding')
			lock.release()
		time.sleep(0.5)
	return

def worker(lock):
	logging.debug('Starting')
	num_tries = 0
	num_acquires = 0
	while num_acquires < 3:
		time.sleep(0.5)
		logging.debug('Trying to acquire')
		have_it = lock.acquire(0)  #查看另外一个进程是否请求锁 而不影响当前进程
                                   #如果lock重复acquire会导致死锁
                                   #设置了超时0 避免永久阻塞
		try:
			num_tries += 1
			if have_it:
				logging.debug('Iteration %d: Acquired',num_tries)
				num_acquires += 1
			else:
				logging.debug('Iteration %d: not acquired',num_tries)
		finally:
			if have_it:
				lock.release()
	logging.debug('Done after %d iterations',num_tries)

lock = threading.Lock()
holder = threading.Thread(target=lock_holder,args=(lock,),name='LockHolder')
holder.setDaemon(True) #守护线程,不阻塞主程序退出,主程序退出依然存在
holder.start()

worker = threading.Thread(target=worker,args=(lock,), name='Worker')
worker.start()





