#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
import signal
import os
import time
if __name__ == '__main__':
    def do_exit(sig, stack):
        raise SystemExit('Exiting')
    signal.signal(signal.SIGINT, signal.SIG_IGN) #ctrl + c SIGINT 中断程序   处理函数为 signal.SIG_IGN 时忽略信号
    signal.signal(signal.SIGUSR1, do_exit)   #退出程序
    print 'My PID:', os.getpid()
    signal.pause()

# My PID: 59155