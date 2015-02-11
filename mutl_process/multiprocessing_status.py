__author__ = 'admin'
import multiprocessing
import time
def slow_worder():
	print 'Starting worker',
	time.sleep(0.1)
	print 'Finished worker'

if __name__ == '__main__':
	p = multiprocessing.Process(target=slow_worder)
	print 'BEFORE',p,p.is_alive()

	p.start()
	print 'DURING',p,p.is_alive()

	p.terminate() #end the child process SIGTERM
	print 'TERMINATED',p,p.is_alive()

	p.join()
	print 'JOINED',p,p.is_alive()
