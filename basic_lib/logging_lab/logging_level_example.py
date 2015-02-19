#!/usr/bin/env python
"""Simple logging to stderr using different levels.
"""
#end_pymotw_header

import logging
import sys

LEVELS = { 'debug':logging.DEBUG,
           'info':logging.INFO,
           'warning':logging.WARNING,
           'error':logging.ERROR,
           'critical':logging.CRITICAL,
           }

# NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL
print sys.argv
if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message') #默认是 warning
logging.error('This is an error message')
logging.critical('This is a critical error message')
