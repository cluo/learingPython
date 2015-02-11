__author__ = 'admin'
X = 11
def g1():
	print(X)
def g2():
	global X
	X = 22
def h1():
	X = 33
	def nested():
		print(X)
	nested()

g1()
g2()
print X
h1()