#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-14
__author__ = 'cluo'

import logging
import threading
import time
#consumer（）要设置Condition 才能继续
#producer() 负责设置条件 并通知其他进程可以继续‰
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s (%(threadName)-2s) %(message)s'
)

def consumer(cond):
    """wait fro condition and use the resource"""
    logging.debug('Starting consumer thread')
    t = threading.currentThread()
    with cond: #condition 使用一个Lock
        cond.wait()
        logging.debug('Resource is alailable to consumer')

def producer(cond):
    """set up the resource to be used by the consumer"""
    logging.debug('Starting producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

condition = threading.Condition()
c1 = threading.Thread(name = 'c1', target = consumer, args = (condition,))
c2 = threading.Thread(name = 'c2', target = consumer, args = (condition,))

p = threading.Thread(name = 'p', target = producer, args = (condition,))


if __name__ == '__main__':
    c1.start()
    time.sleep(2)
    c2.start()
    time.sleep(2)
    p.start()
