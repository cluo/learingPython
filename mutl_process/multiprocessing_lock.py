__author__ = 'admin'
import multiprocessing
import sys

def worker_with(lock, stream):
	with lock:
		stream.write('Lock acquired var with\n')

def worker_no_with(lock, stream):
	lock.acquire()
	try:
		stream.write('Lock acquire directly\n')
	finally:
		lock.release()

lock = multiprocessing.Lock()
w = multiprocessing.Process(target=worker_with,
							args=(lock, sys.stdout))
nw = multiprocessing.Process(target=worker_no_with,
							args=(lock, sys.stdout))
w.start()
nw.start()

w.join()
nw.join()
