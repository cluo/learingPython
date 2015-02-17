#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue
import threading
import urllib2
import time
from BeautifulSoup import BeautifulSoup

# 对加入到第二个队列中的另一个线程池进行设置，然后对 Web 页面执行相应的处理。
# 这个示例中所进行的工作包括使用一个名为 Beautiful Soup 的第三方 Python 模块来解析 Web 页面。
# 使用这个模块，您只需要两行代码就可以提取所访问的每个页面的 title 标记，并将其打印输出。


queue = Queue.Queue()
out_queue = Queue.Queue()

class ThreadUrl(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, queue, out_queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while True:
            #grabs host from queue
            host = self.queue.get()

            #grabs urls of hosts and then grabs chunk of webpage
            url = urllib2.urlopen(host)
            chunk = url.read()   #读出内容

            #place chunk into out queue
            self.out_queue.put(chunk) #抛出内容

            #signals to queue job is done
            self.queue.task_done()

class DatamineThread(threading.Thread):
    """Threaded Url Grab"""
    def __init__(self, out_queue):
        threading.Thread.__init__(self)
        self.out_queue = out_queue

    def run(self):
        while True:
            #grabs host from queue
            chunk = self.out_queue.get()

            #parse the chunk
            soup = BeautifulSoup(chunk)
            print soup.findAll(['title']) #搜索标签名

            #signals to queue job is done
            self.out_queue.task_done()  #阻止阻塞

start = time.time()
hosts = ["http://yahoo.com", "http://amazon.com",
        "http://ibm.com", "http://apple.com"]




def main():

    #spawn a pool of threads, and pass them queue instance
    for i in range(5):
        t = ThreadUrl(queue, out_queue)
        t.setDaemon(True)
        t.start()

    #populate queue with data
    for host in hosts:
        queue.put(host)

    for i in range(5):
        dt = DatamineThread(out_queue)
        dt.setDaemon(True)
        dt.start()


    #wait on the queue until everything has been processed
    queue.join()
    out_queue.join()

main()
print "Elapsed Time: %s" % (time.time() - start)