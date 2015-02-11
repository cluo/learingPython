#coding:utf-8

import logging
from logging.handlers import RotatingFileHandler
from util import app_abs_path, read_config

__all__ = ['Logger']

class Singleton(object):
    def __new__(type, *args, **kwargs):
        if not '_the_instance' in type.__dict__:
            type._the_instance = object.__new__(type, *args, **kwargs)
        return type._the_instance

class Logger(object):
    _no_handlers = True

    def __init__(self, config_file="etc/client.conf", logfile=""):
        self.config = read_config(app_abs_path(config_file))
        if not logfile:
            logfile = self.config['log_file']
        self.loglevel = logging._levelNames[self.config['log_level']]
        self._setup_logging()
        if self._no_handlers:
            self._setup_handlers(logfilepath=app_abs_path(logfile))

    def _setup_logging(self):
        self.logger = logging.getLogger()

    def _setup_handlers(self, logfilepath):
        handler = RotatingFileHandler(filename=logfilepath, maxBytes=10 * 1024 * 1024, backupCount=3)
        self.logger.setLevel(self.loglevel)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s.%(funcName)s Line:%(lineno)d %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        self._no_handlers = False
# log = Logger()