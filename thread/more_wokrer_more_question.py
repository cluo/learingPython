#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-14
__author__ = 'cluo'

#Example2.py
'''
A more realistic thread pool example
'''
# 这段代码能正确的运行，但仔细看看我们需要做些什么：构造不同的方法、追踪一系列的线程，
# 还有为了解决恼人的死锁问题，我们需要进行一系列的 join 操作。这还只是开始……
#
# 至此我们回顾了经典的多线程教程，多少有些空洞不是吗？样板化而且易出错，
# 这样事倍功半的风格显然不那么适合日常使用，好在我们还有更好的方法。
import time
import threading
import Queue
import urllib2
import logging

#日志
logging.basicConfig(
 level=logging.DEBUG,
 format='[%(asctime)s](%(threadName)-10s) %(message)s'
)

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            content = self._queue.get()
            if isinstance(content, str) and content == 'quit':
                break
            logging.debug(content)
            response = urllib2.urlopen(content)
            print response



def Producer():
    urls = [
        'http://www.yahoo.com',
        'http://www.baidu.com',
        'http://www.163.com',
        'http://www.python.org',
    ]
    queue = Queue.Queue()
    worker_threads = build_worker_pool(queue, 4)
    start_time = time.time()

    # Add the urls to process
    for url in urls:
        queue.put(url)
    for worker in worker_threads:     # Add the poison pillv
        queue.put('quit')
    for worker in worker_threads:
        worker.join()

    print 'Done! Time taken: {}'.format(time.time() - start_time)

def build_worker_pool(queue, size):
    workers = []
    for _ in range(size):
        worker = Consumer(queue)
        worker.start()
        workers.append(worker)
    return workers

if __name__ == '__main__':
    Producer()
