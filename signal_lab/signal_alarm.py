#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
import signal
import time
#定时触发信号
__author__ = 'cluo'
def receive_alarm(signum, stack):
    print 'Alarm :',time.ctime()
signal.signal(signal.SIGALRM, receive_alarm)
signal.alarm(2)
print 'Before:',time.ctime()
time.sleep(4)
print 'After :',time.ctime()



