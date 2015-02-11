__author__ = 'admin'
import threading
import time
def worker():
	print threading.currentThread().getName(),'Starting'
	time.sleep(2)
	print threading.currentThread().getName(), 'Exting'
def my_service():
	print threading.currentThread().getName(),'Starting'
	time.sleep(2)
	print threading.currentThread().getName(), 'Exting'

t = threading.Thread(name='my_service', target=my_service)
w = threading.Thread(name='worker', target=worker)
w2 = threading.Thread(target=worker)

t.start()
w.start()
w2.start()



