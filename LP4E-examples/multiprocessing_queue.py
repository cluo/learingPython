__author__ = 'admin'
import multiprocessing
import logging
class MyFancyClass(object):
	def __init__(self, name):
		self.name = name
	def do_something(self):
		proc_name =  multiprocessing.current_process().name
		print 'Doing something fancy in %s for %s ' % (proc_name, self.name)

def worker(q):
	obj = q.get() #get put
	obj.do_something()

if __name__ == '__main__':
	multiprocessing.log_to_stderr(logging.DEBUG)
	queue = multiprocessing.Queue()
	p = multiprocessing.Process(target=worker, args=(queue,))
	p.start()
	queue.put(MyFancyClass('Fancy Dan'))

    #wait for worker to finish
	queue.close()
	queue.join_thread()
	p.join()



