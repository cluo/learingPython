#-*- coding:utf8 -*-
__author__ = 'admin'
import sys
import os

def log(message, *args):
	message = message % args
	sys.stderr.write(message+'\n')
arg= (1,2,3,5)
log('hello %s %s %s %s',*arg)

#执行命令
os.system('ls -al')




