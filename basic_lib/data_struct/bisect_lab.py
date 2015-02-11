__author__ = 'admin'
#-*- coding:utf8 -*-
import bisect
import random

#正向插入排序
l = []
for i in range(1, 15):
	r = random.randint(1, 1000)
	position = bisect.bisect(l, r)
	bisect.insort(l,r)
	print '%3d %3d' %(r,position),l





def index(a, x):
	'Locate the leftmost value exactly equal to x'
	i = bisect.bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return i
	raise ValueError

def find_lt(a, x):
	'Find rightmost value less than x'
	i = bisect.bisect_left(a, x)
	if i:
		return a[i-1]
	raise ValueError

def find_le(a, x):
	'Find rightmost value less than or equal to x'
	i = bisect.bisect_right(a, x)
	if i:
		return a[i-1]
	raise ValueError

def find_gt(a, x):
	'Find leftmost value greater than x'
	i = bisect.bisect_right(a, x)
	if i != len(a):
		return a[i]
	raise ValueError

def find_ge(a, x):
	'Find leftmost item greater than or equal to x'
	i = bisect.bisect_left(a, x)
	if i != len(a):
		return a[i]
	raise ValueError

l = [2 ,3 ,4 ,5, 6,	7]
print index(l,3)

print find_lt(l,3)

print find_le(l,3)

print find_gt(l,3)

print find_ge(l,3)
