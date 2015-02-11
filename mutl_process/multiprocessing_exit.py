__author__ = 'admin'
import multiprocessing
import sys
import time
def exit_error():
	sys.exit(1)

def exit_ok():
	return 0

def return_value():
	return 0

def raises():
	raise  RuntimeError('There was na error!') #except error code 1

def terminated():
	time.sleep(2)

if __name__ == '__main__':
	jobs = []
	for f in [exit_error, exit_ok, return_value,raises,terminated]:
		print 'Starting process for', f.func_name
		j = multiprocessing.Process(target =f, name =f.func_name)
		jobs.append(j)
		j.start()

	jobs[-1].terminate()

	for j in jobs:
		j.join()
		print '%15s.exitcode = %s' % (j.name, j.exitcode)






