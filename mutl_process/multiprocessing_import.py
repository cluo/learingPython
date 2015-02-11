from mutl_process import multiprocessing_import_worker

__author__ = 'admin'
import multiprocessing

if __name__ == '__main__':
	jobs = []
	for i in range(5):
		p = multiprocessing.Process(
			target = multiprocessing_import_worker.worker,
		)
		jobs.append(p)
		p.start()
