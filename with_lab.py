__author__ = 'admin'
import sys
class test:
	def __enter__(self):
		print('enter')
		return 1
	def __exit__(self,*args):
		print("exit")
		return True
with test() as t:
	print('t is not the result of test(),it is __enter__ returned')
	print("t is 1 yes,it is {0}".format(t))
	raise NameError('hi there')
	sys.exit()


