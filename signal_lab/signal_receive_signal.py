#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
import signal
import os
import time

#信号(signal)是Linux进程间通信的一种机制，全称为软中断信号，也被称为软中断。信号本质上是在软件层次上对硬件中断机制的一种模拟。
def receive_signal(signum, stack):
    print '==============================received:',signum
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

#kill -USR1 $pid
#kill -USR1 $pid
#kill -INT $pid   ctrl + c
#kill -QUIT $pid  crtl + d


if __name__ == '__main__':
    print 'my pid is :', os.getpid()
    while True:
        print 'Waiting...'
        print os.getpid()
        print 'usr1:',signal.SIGUSR1
        print 'usr2:',signal.SIGUSR2
        time.sleep(20)
