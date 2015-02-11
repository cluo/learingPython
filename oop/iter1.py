__author__ = 'admin'
class Squares:
	def __init__(self, start, stop):
		self.value = start -1
		self.stop = stop
	def __iter__(self):
		return self
	def next(self):
		if self.value == self.stop:
			raise  StopIteration
		self.value += 1
		return self.value ** 2

for i in Squares(1, 5):
	print(i)

print [n for n in Squares(1,3)]
print list(Squares(1,3))


def gsquares(start, stop):
	for i in range(start, stop+1):
		yield i ** 2

for i in gsquares(1, 5):
	print(i)

print [x ** 2 for x in range(1,6)]