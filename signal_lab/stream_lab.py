#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
import signal
import os
# Define signal handler function
def myHandler(signum, frame):
    print('I received: ', signum)
    print signal.SIGTSTP
    print os.getpid()
    print 'end'
    os.kill(os.getpid(),signal.SIGTERM)

# register signal.SIGTSTP's handler
signal.signal(signal.SIGTSTP, myHandler)
while True:
    print('End of Signal Demo')

#通过按下CTRL+Z向该进程发送SIGTSTP信号