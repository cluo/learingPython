
#-*- coding:utf8 -*-
__author__ = 'admin'
import re
pattern = re.compile(r"hello")
match = pattern.match('hello world')
if match:
	print match.group()

a  = re.compile(r"""
\d+ #interger
\.	#the decimal point
\d* #some facitonal
""",re.X);
b = re.compile(r"\d+\.\d*")




match = a.match('11.22')
if match:
	print match.group()

match = b.match('11.22')
if match:
	print match.group()

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)')
print p.pattern
print p.flags
print p.groups
print p.groupindex

#全匹配
m = re.match(p,'hello world!')

print m.string
print m.re
print m.pos
print m.endpos
print m.lastindex
print m.lastgroup
print m.group(1,2)
print m.groups()
print m.groupdict()
print m.start(2)
print m.end(2)
print m.span(2)
print m.expand(r'\2 \1 \3')
print m.expand(r'\0') #python 没有这种写法


pattern = re.compile(r'world')
match = pattern.search('hello world!')
if match:
	print match.group()


p = re.compile(r'\d+')
print p.split('one1two2tree3four4')
print p.findall('one1two2tree3four4')

for m in p.finditer('one1two2three3four4'):
	print m.group()

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'
print p.sub(r'\2 \1',s)
def func(m):
	return m.group(1).title() + ' ' + m.group(2).title()
print p.sub(func, s)
print p.subn(func, s)

