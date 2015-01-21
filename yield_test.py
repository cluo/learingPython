__author__ = 'admin'
def fab(max):
	n, a, b = 0, 0, 1
	L =[]
	while n < max:
		L.append(b)
		a,b = b, a + b
		n = n + 1
	return L
L = fab(5)
print L

class Fab(object):
	def __init__(self, max):
		self.max = max
		self.n, self.a, self.b = 0, 0, 1
	def __iter__(self):
		return self
	def next(self):
		if self.n < self.max:
			r = self.b
			self.a, self.b = self.b, self.a + self.b
			self.n = self.n + 1
			return r
		raise StopIteration()


for n in Fab(5):
	print n

def fab(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
for n in fab(5):
	print n
f = fab(5)
print f.next()
print f.next()
print f.next()


from inspect import isgeneratorfunction
print isgeneratorfunction(fab)
import types
print isinstance(fab, types.GeneratorType) #generator function
print isinstance(fab(5), types.GeneratorType)#generator

def read_file(fpath):
	BLOCK_SIZE = 1024
	with open(fpath, 'rb') as f:
		while True:
			block = f.read(BLOCK_SIZE)
			if block:
				yield block
			else:
				return
blocks = read_file('cluo')
for block in blocks:
	print block


def addlist(list):
	for i in list:
		yield i + 1
L = [1, 2, 3, 4]
for x in addlist(L):
	print x



def h():
	print 'To be brave'
	yield 5

t = h()
print t.next()


def hello():
	print 'hello'
	k = yield 5
	print 'hello1 %s' % k
t = hello()
print t.next()
print t.send('seeyou') #当前迭代
print t.next()
print t.next()

# def h1():
# 	print 'Wen chuan'
# 	m = yield 5
# 	print m
# 	d = yield 12
# 	print d
# 	print 'we are togeter!'
#
# h1_t = h1()
# print h1_t.next()
# h1_t.send('hello world')



