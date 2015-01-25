__author__ = 'admin'
import multiprocessing
def worker():
	print 'Worker'
	return
if __name__ == '__main__':
	jobs = []
	for i in range(5):
		p = multiprocessing.Process(target=worker)
		jobs.append(p)
		p.start()
