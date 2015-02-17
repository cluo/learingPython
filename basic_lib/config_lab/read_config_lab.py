#-*- coding:utf8 -*-
__author__ = 'admin'
import os
import sys
from ConfigParser import ConfigParser,ParsingError
conf_path = 'server.conf'
section = 'main'
opts = {}

#读取根目录
def prog_dir():
	return os.path.dirname(os.path.abspath(__file__))

#获取根目录下的文件
def file_abs_path(rel_path):
	abs_path = ''
	if rel_path:
			abs_path = os.path.join(prog_dir(),rel_path)
	return abs_path


#ConfigParser 读取配置
def read_config_file(rel_path,section = 'main'):
	conf_path = file_abs_path(rel_path)
	if os.path.exists(conf_path):
		try:
			confparser = ConfigParser()
			confparser.read(conf_path)
			for k,v in confparser.items(section):
				opts[k] = v
		except ParsingError, e:
			print >> sys.stderr, 'Error reading config file %s' % e
			sys.exit(1)
	return opts





opts = read_config_file(conf_path, section = 'main')
print opts


opts = read_config_file(conf_path, section = 'db')
print opts

