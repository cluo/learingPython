#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'

#程序可以由同一个线程空间并发运行多个进程
import threading
def worker(num,mark):
    """thread worker function """
    print 'Worker %s mark %s' % (num,mark)
    print threading.currentThread().getName()
    return
threads = []
for i in range(5):
    name = 'cluo' + str(i)
    t = threading.Thread(target = worker, name = name, args = (i,name))
    threads.append(t)
    t.start()

print threads