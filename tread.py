__author__ = 'admin'
import threading
def worker():
	"""xxx"""
	print('workder')
	return

threads = []
for i in range(5):
	t = threading.Thread(target=worker)
	threads.append(t)
	t.start()

