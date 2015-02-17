#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'
import Queue
import threading

#优先队列
class Job(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New job:',description
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)  #优先队列排序依据

q = Queue.PriorityQueue()
q.put(Job(3, 'Mid-level job'))
q.put(Job(10, 'Low-level job'))
q.put(Job(1, 'Important job'))   #1最优先

def process_job(q):
    while True:
        next_job = q.get()
        print 'Process job:', next_job.description
        q.task_done()
workers = [ threading.Thread(target=process_job, args=(q,)),
            threading.Thread(target=process_job, args=(q,))
            ]
for w in workers:
    w.setDaemon(True)
    w.start()

q.join()
