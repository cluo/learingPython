#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-14
__author__ = 'cluo'
import logging
import random
import threading
import time
#线程池 线程池
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s (%(threadName)-2s) %(message)s'
)

class ActivePool(object):
    def __init__(self):
        super(ActivePool,self).__init__()
        self.active = []
        self.lock = threading.Lock()

    def makeActive(self, name):
        with self.lock:
            self.active.append(name)
            logging.debug('Running:%s', self.active)

    def makeInactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.debug('Running:%s', self.active)

def worker(s, pool):
    logging.debug('Waiting to join the pool')
    with s:
        name = threading.currentThread().getName()
        pool.makeActive(name)
        time.sleep(0.1)
        pool.makeInactive(name)


pool = ActivePool()
if __name__ == '__main__':
    s = threading.Semaphore(2)  # 线程池
    for i in range(4):
        t = threading.Thread(target = worker,
                             name = str(i),
                             args = (s, pool))
        t.start()
