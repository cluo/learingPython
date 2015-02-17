#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'

# 对于这个示例，有更多的代码需要说明，但与第一个线程示例相比，它并没有复杂多少
# ，这正是因为使用了队列模块。在 Python 中使用线程时，这个模式是一种很常见的并且推荐使用的方式。具体工作步骤描述如下：
# 创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
# 将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
# 生成守护线程池。
# 每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
# 在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
# 对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。
# 在使用这个模式时需要注意一点：通过将守护线程设置为 true，
# 将允许主线程或者程序仅在守护线程处于活动状态时才能够退出。
# 这种方式创建了一种简单的方式以控制程序流程，因为在退出之前，
# 您可以对队列执行 join 操作、或者等到队列为空。队列模块文档详细说明了实际的处理过程，请参见参考资料：
# join()
# 保持阻塞状态，直到处理了队列中的所有项目为止。在将一个项目添加到该队列时，
# 未完成的任务的总数就会增加。当使用者线程调用 task_done() 以表示检索了该项目、
# 并完成了所有的工作时，那么未完成的任务的总数就会减少。当未完成的任务的总数减少到零时，join() 就会结束阻塞状态。
import Queue
import threading
import urllib2
import time

hosts = ["http://yahoo.com", "http://amazon.com",
  "http://ibm.com", "http://apple.com"]

queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue):
      threading.Thread.__init__(self)
      self.queue = queue

    def run(self):
      while True:
        #grabs host from queue
        host = self.queue.get() #阻塞等待

        #grabs urls of hosts and prints first 1024 bytes of page
        url = urllib2.urlopen(host)
        print url.read(1024)

        #signals to queue job is done
        self.queue.task_done() #通知往下走

start = time.time()
def main():
    #spawn a pool of threads, and pass them queue instance
    for i in range(5):
      t = ThreadUrl(queue)
      t.setDaemon(True)
      t.start()
    #populate queue with data
      for host in hosts:
        queue.put(host)
    #wait on the queue until everything has been processed
    queue.join() #阻塞直到队列为空，如果一开始队列为空 会永久阻塞住

main()
print "Elapsed Time: %s" % (time.time() - start)