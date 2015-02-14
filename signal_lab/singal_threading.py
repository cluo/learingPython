#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
import signal
import threading
import os
import time

#信号一般是线程级别的通信，
#子线程是接不了信号的,子线程pause, 子线程将永远不会退出
#只有主线程才能接受闹铃

if __name__ == '__main__':
    #主线程
    def signal_handler(num, stack):
        print 'Received signal %d in %s' %(num, threading.currentThread().name)
    signal.signal(signal.SIGUSR1, signal_handler) #python 中的信号处理函数


    def signal_handler_1(num, stack):
        print 'Received signal %d in %s' %(num, threading.currentThread().name)
    signal.signal(signal.SIGTERM, signal_handler_1) #python 中的信号处理函数




    #收信号线程
    def wait_for_signal():
        print 'Waiting for signal in',threading.currentThread().name
        signal.pause()  #线程 接受不了任何信号
        print 'Done waiting'

    receiver = threading.Thread(target=wait_for_signal,name='receiver')
    receiver.start()
    time.sleep(0.1)

    #发信号线程
    def send_signal():
        print 'Sending signal in',threading.currentThread().name
        os.kill(os.getpid(), signal.SIGUSR1)
        os.kill(os.getpid(), signal.SIGTERM)

    sender = threading.Thread(target=send_signal,name='sender')
    start = time.time()
    sender.start()
    sender.join()

    print 'Waiting for',receiver.name
    signal.alarm(2) #2秒后自己送送SIGALRM 终止程序(防止阻塞)
    print os.getpid()
    receiver.join()
    end = time.time()
    interval = end - start
    print interval

