#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import multiprocessing
import time

class Consumer(multiprocessing.Process):
    
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        proc_name = self.name
        while True:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print '%s: Exiting' % proc_name
                self.task_queue.task_done()  #遇到None退出循环
                break
            print '%s: %s' % (proc_name, next_task)
            answer = next_task()
            self.task_queue.task_done() #停止阻塞
            self.result_queue.put(answer)
        return


class Task(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self):
        time.sleep(0.1) # pretend to take some time to do the work
        return '%s * %s = %s' % (self.a, self.b, self.a * self.b)
    def __str__(self):
        return '%s * %s' % (self.a, self.b)


if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    
    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print 'Creating %d consumers' % num_consumers
    consumers = [ Consumer(tasks, results)
                  for i in xrange(num_consumers) ]
    for w in consumers:
        w.start()
    
    # Enqueue jobs
    num_jobs = 10
    for i in xrange(num_jobs):
        tasks.put(Task(i, i))
    
    # Add a poison pill for each consumer
    for i in xrange(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()
    
    # Start printing results
    while num_jobs:
        result = results.get()
        print 'Result:', result
        num_jobs -= 1
# Creating 8 consumers
# Consumer-2: 0 * 0
# Consumer-1: 1 * 1
# Consumer-3: 2 * 2
# Consumer-4: 3 * 3
# Consumer-5: 4 * 4
# Consumer-6: 5 * 5
# Consumer-7: 6 * 6
# Consumer-8: 7 * 7
# Consumer-1: 8 * 8Consumer-2: 9 * 9
#
# Consumer-4: Exiting
# Consumer-6: ExitingConsumer-3: Exiting
#
# Consumer-5: Exiting
# Consumer-7: Exiting
# Consumer-8: Exiting
# Consumer-2: Exiting
# Consumer-1: Exiting
# Result: 0 * 0 = 0
# Result: 1 * 1 = 1
# Result: 3 * 3 = 9
# Result: 5 * 5 = 25
# Result: 2 * 2 = 4
# Result: 4 * 4 = 16
# Result: 6 * 6 = 36
# Result: 7 * 7 = 49
# Result: 8 * 8 = 64
# Result: 9 * 9 = 81