__author__ = 'admin'
import multiprocessing
def do_calculation(data):
	return data * 2
def start_process():
	print 'starting',multiprocessing.current_process().name
if __name__ == '__main__':
	inputs = list(range(10))
	print 'Input  :', inputs
	builtin_outs = map(do_calculation, inputs)
	print 'Built_in:',builtin_outs

	pool_size = multiprocessing.cpu_count()*2
	pool = multiprocessing.Pool(processes=pool_size,
								initializer=start_process,
								maxtasksperchild=2,)
	pool_outputs = pool.map(do_calculation, inputs)
	pool.close()
	pool.join()
	print 'pool :',pool_outputs

