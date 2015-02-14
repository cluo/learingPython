#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
#尽管线程中能设置闹铃 但总是主线程接受
import signal
import time
import threading

def signal_handler(num, stack):
    print time.ctime(),'Alarm in ', threading.currentThread().name
signal.signal(signal.SIGALRM, signal_handler)

def use_alarm():
    t_name = threading.currentThread().name
    print time.ctime(), 'Setting alarm in ',t_name
    signal.alarm(1) #子线程的闹铃,只主线程接收
                    #不会中断3秒的延迟时
    print time.ctime(),'Sleeping in',t_name
    time.sleep(3)
    print time.ctime(),'Done with sleep in',t_name

alarm_thread = threading.Thread(target=use_alarm,name='alarm_thread')
alarm_thread.start()
time.sleep(0.1)
print time.ctime(),'Waiting for',alarm_thread.name
alarm_thread.join()
print time.ctime(),'Exting normally'
