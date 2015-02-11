__author__ = 'admin'
import multiprocessing
import time
import sys
def daemon():
	name = multiprocessing.current_process().name
	print 'starting:',name
	time.sleep(2)
	print 'Exting:',name

def non_daemon():
	name = multiprocessing.current_process().name
	print 'starting:',name
	print 'Exting:',name


if __name__ ==  '__main__':
	d = multiprocessing.Process(name='daemon',
								target=daemon)
	d.daemon = True

	n = multiprocessing.Process(name='non_daemon',
								target=non_daemon)
	n.daemon = False

	d.start()
	n.start()
	d.join(1) #block_timeout > daemon_processing_time so d.is_alive
	print 'd.is_alive()',d.is_alive()
	n.join()

