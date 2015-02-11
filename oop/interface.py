__author__ = 'admin'

class Super1(object):
	def method(self):
		print('in super method')
	def delegate(self):
		self.action()

class Inheritor(Super1):
	pass

class  Replacer(Super1):
	def method(self):
		print('in replacer.method')

class Extender(Super1):
	def method(self):
		print('starting extender method')
		super(Extender,self).method()
		print('ending extender method')

class Provider(Super1):
	def action(self):
		print('in Provider.action')

# inheritor = Inheritor()
# replace = Replacer()
# extender = Extender()
# if __name__ == '__main__':
# 	for klass in (inheritor,replace,extender):
# 		# print('\n' + klass.__name__ +'...')
# 		klass.method()
#
#
# 	for klass in (Inheritor, Replacer, Extender):
# 		print('\n' + klass.__name__ +'...')
# 		klass.method()