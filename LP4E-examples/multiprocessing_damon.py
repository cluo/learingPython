__author__ = 'admin'
import multiprocessing
import time
import sys

def daemon():
	p = multiprocessing.current_process()
	print 'Starting:', p.name, p.pid
	sys.stdout.flush()
	time.sleep(2)
	print 'Exiting:',p.name, p.pid
	sys.stdout.flush()

def non_daemon():
	p = multiprocessing.current_process()
	print 'starting',p.name,p.pid
	sys.stdout.flush()
	print 'Exting:',p.name,p.pid
	sys.stdout.flush()


if __name__ == '__main__':
	d = multiprocessing.Process(name='daemon', target=daemon)
	d.daemon = True #no block the main process

	n = multiprocessing.Process(name='non_daemon', target=non_daemon)
	n.daemon = False #block the main process

	d.start()
	time.sleep(1)
	n.start()
