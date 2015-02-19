#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2008 Doug Hellmann All rights reserved.
#
"""Daemon vs. non-daemon processes.
"""
#end_pymotw_header

import multiprocessing
import time
import sys
import logging
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOG_FILENAME = 'logging_example.out'
logging.basicConfig(filename=LOG_FILENAME,  #root logger  写日志
                    level=logging.DEBUG,
                    )

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    time.sleep(2)
    print 'Exiting :', p.name, p.pid
    logging.debug('daemon')
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid
    logging.debug('no_daemon')
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)  #所有子进程退出主进程之前 主进程不会退出
                                                               #守护进程（后台进程） 它可以一直运行不阻止主程序退出
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    time.sleep(1) #虽然睡了一秒钟，单主程序运行完后，守护进程会在主程序退出之前退出 避免留下孤儿进程
    n.start()


#
# Starting: daemon 50501
# Starting: non-daemon 50508
# Exiting : non-daemon 50508