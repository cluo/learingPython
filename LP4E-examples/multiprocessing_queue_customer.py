__author__ = 'admin'
import multiprocessing
import time

class Consumer(multiprocessing.Process):
	def __init__(self, task_queue, result_queue):
		multiprocessing.Process.__init__(self)
		self.task_queue = task_queue
		self.result_queue = result_queue

	def run(self):
		proc_name = self.name
		while True:
			next_task = self.task_queue.get()
			if next_task is None:
				print '%s: Exiting' % proc_name
				self.task_queue.task_done()
				break
			print '%s:%s' % (proc_name, next_task)
			answer = next_task()
			self.task_queue.task_done()
			self.result_queue.put(answer)
		return


class Task(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def __call__(self):
		time.sleep(0.1)
		return '%s * %s = %s' % (self.a, self.b, self.a * self.b)
	def __str__(self):
		return '%s * %s' % (self.a, self.b)

if __name__ == '__main__':
	tasks = multiprocessing.JoinableQueue()
	results = multiprocessing.Queue()

	num_consumers = multiprocessing.cup_count() * 2
	print 'Creating %d consumers' % num_consumers

	consumers = [Consumer(tasks, results) for i in xrange(num_consumers)]
	for w in consumers:
		w.start()



