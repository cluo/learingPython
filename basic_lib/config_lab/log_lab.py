__author__ = 'admin'
import sys
import os
import json

def log(message, *args):
	message = message % args
	sys.stderr.write(message+'\n')
arg= (1,2,3,5)
log('hello %s %s %s %s',*arg)
os.system('ls -al')




