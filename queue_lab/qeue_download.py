#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'
# No, queue.get() pops the item off the queue. After you do that,
# you can do whatever you want with it, as long as the producer works like it should
# and doesn't touch it anymore. queue.task_done() is called only to notify ' \
#          'the queue that you are done with something (it doesn't even know about the specific item,
# it just counts unfinished items in the queue), so that queue.join() knows the work is finished.

# q.task_done()，每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法，以提示q.join()是否停止阻塞，让线程向前执行或者退出；
# q.join()，阻塞，直到queue中的数据均被删除或者处理。为队列中的每一项都调用一次。
#
# 对于生产者-消费者模型，这样做还是有问题的，因为如果queue初始为空，q.join()会直接停止阻塞，继而执行后续语句；
#
# 如果有多个消费者，没有生产者，且queue始初化为一定的数据量，则可以正常执行。


from Queue import Queue
from threading import Thread
import time
import urllib
import urlparse
import feedparser


num_fetch_threads = 2
enclosure_queue = Queue()
feed_urls = [ 'http://advocacy.python.org/podcasts/littlebit.rss' ]

def downloadEnclosures(i, q):
    while True:
        print '%s Looking for the next enclosure' % i
        url = q.get() #阻塞并且等待 直到队列返回某个结果
        parsed_url = urlparse.urlparse(url)
        print '%s: Downloading:' % i,parsed_url
        response = urllib.urlopen(url)
        data = response.read()
        outfile_name = url.rpartition('/')[-1]
        with open(outfile_name,'wb') as outfile:
            outfile.write(data)
        q.task_done() #停止阻塞

if __name__ == '__main__':
    for i in range(num_fetch_threads):
        worker = Thread(target=downloadEnclosures,
                        args=(i, enclosure_queue,))
        worker.setDaemon(True)
        worker.start()

    for url in feed_urls:
        response = feedparser.parser(url, agent='fetch_podcasts.py')
    for entry in response['entries'][-5]:
        for enclosure in entry.get('enclosures',[]):
            parsed_url = urlparse.urlparse(enclosure['url'])
            print 'Queuing:', parsed_url.path
            enclosure_queue.put(enclosure['url'])

    print '****Main thread waiting'
    enclosure_queue.join()
    print '***Done'
