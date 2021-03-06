#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import multiprocessing
import logging
import sys

def worker():
    print 'Doing some work'
    sys.stdout.flush()

if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG) #日志
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    


# Doing some work
# [INFO/Process-1] child process calling self.run()
# [INFO/Process-1] process shutting down
# [DEBUG/Process-1] running all "atexit" finalizers with priority >= 0
# [DEBUG/Process-1] running the remaining "atexit" finalizers
# [INFO/Process-1] process exiting with exitcode 0
# [INFO/MainProcess] process shutting down
# [DEBUG/MainProcess] running all "atexit" finalizers with priority >= 0
# [DEBUG/MainProcess] running the remaining "atexit" finalizers