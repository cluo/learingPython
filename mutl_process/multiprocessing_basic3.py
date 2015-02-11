__author__ = 'admin'
import multiprocessing
def worker(num):
	print 'worker:',num
	return
if __name__ == '__main__':
	jobs = []
	for i in range(5):
		p = multiprocessing.Process(target=worker, args=(i,))
		jobs.append(p)
		p.start()
