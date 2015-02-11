#!/usr/bin/evn python
#-*- coding:utf-8 -*-
__author__ = 'admin'
class Indexer:
	def __getitem__(self, index):
		return index ** 2
X = Indexer()
print X[2]

for i in range(5):
	print(X[i])



class stepper:
	def __getitem__(self, i):
		return self.data[i]

X  = stepper()
X.data = 'spam'
for item in X:
	print(item)

print 'p' in X

print [c for c in X]

print ''.join(X)
print list(X)
print tuple(X)
