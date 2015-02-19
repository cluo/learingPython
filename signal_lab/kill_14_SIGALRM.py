#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'

import signal
import os



# Define signal handler function
def myHandler(signum, frame):
    print signum
    print os.getpid()
    print signal.SIGALRM  #14定时唤醒
    print("Now, it's the time")
    os.kill(os.getpid(),signal.SIGALRM)
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(2) #闹铃自己给自己发SIGALRM信号
signal.pause()
print('End of Signal Demo')



# 14
# 59393
# 14
# Now, it's the time
# 14
# 59393
# 14
# Now, it's the time


