__author__ = 'admin'
import Queue
q = Queue.Queue()
for i in range(5):
	q.put(i)
while not q.empty():
	print q.get()


q = Queue.LifoQueue()
for i in range(5):
	q.put(i)
while not q.empty():
	print q.get()
