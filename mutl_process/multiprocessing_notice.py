__author__ = 'admin'
import multiprocessing
class MyFancyClass(object):
	def __init__(self,name):
		self.name = name
	def do_something(self):
		proc_name = multiprocessing.current_process().name
		print 'Doing something fancy in %s for %s!' % (proc_name,self.name)
def worker(q):
	obj = q.get()
	obj.do_something()
if __name__ == 'main':
	queue = multiprocessing.Queue()
	p = multiprocessing.Process(target=worker,args=(queue,))
	p.start()

	queue.put(MyFancyClass('Fancy dan'))

	queue.close()
	queue.join_thread()
	p.join()

