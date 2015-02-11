__author__ = 'admin'
import os
import sys
from ConfigParser import ConfigParser,ParsingError
conf_path = 'server.conf'
section = 'main'
opts = {}


def prog_dir():
	return os.path.dirname(os.path.abspath(__file__))

def file_abs_path(rel_path):
	abs_path = ''
	if rel_path:
			abs_path = os.path.join(prog_dir(),rel_path)
	return abs_path

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





opts = read_config_file(conf_path)
print opts


opts = read_config_file(conf_path, sestion = 'db')
print opts

