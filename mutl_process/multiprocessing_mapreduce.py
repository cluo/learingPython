__author__ = 'admin'
import collections
import itertools
import multiprocessing

class SimpleMapReduce(object):
	def __init__(self, map_func, reduce_func, num_workers=None):
		self.map_func = map_func
		self.reduce_func = reduce_func
		self.pool = multiprocessing.Pool(num_workers)

	def partition(self, mapped_values):
		partitioned_data = collections.defaultdict(list)
		for key, value in mapped_values:
			partitioned_data[key].append(value)
		return partitioned_data.items()

	def __call__(self, inputs, chunksize=1):
		map_response = self.pool.map(self.map_func,
									 inputs,
									 chunksize=chunksize)
		partitioned_data = self.partition(itertoools.chian(*ma))