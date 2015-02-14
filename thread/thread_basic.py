#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'

#程序可以由同一个线程空间并发运行多个进程
import threading
def worker():
    """thread worker function """
    print 'Worker'
    print threading.currentThread().getName()
    return
threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

print threads