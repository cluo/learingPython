#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-14
__author__ = 'cluo'
import threading
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s'
                    )
def worker_with(lock):
    with lock: #避免了 lock.acquire lock.release
        logging.debug('Lock acquired via with')
def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()



if __name__ == '__main__':
    lock = threading.Lock()
    w = threading.Thread(target = worker_with, args = (lock,))
    nw = threading.Thread(target = worker_no_with, args = (lock,))
    w.start()
    nw.start()

