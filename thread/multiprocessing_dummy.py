#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'
# 在 Python 中有个两个库包含了 map 函数： multiprocessing 和它鲜为人知的子库 multiprocessing.dummy.
#
# 这里多扯两句： multiprocessing.dummy？ mltiprocessing 库的线程版克隆？这是虾米？
# 即便在 multiprocessing 库的官方文档里关于这一子库也只有一句相关描述。
# 而这句描述译成人话基本就是说:”嘛，有这么个东西，你知道就成.”相信我，这个库被严重低估了！
#
# dummy 是 multiprocessing 模块的完整克隆，唯一的不同在于 multiprocessing 作用于进程，
# 而 dummy 模块作用于线程（因此也包括了 Python 所有常见的多线程限制）。
# 所以替换使用这两个库异常容易。你可以针对 IO 密集型任务和 CPU 密集型任务来选择不同的库。2
#

# Pool 对象有一些参数，这里我所需要关注的只是它的第一个参数：processes. 这一参数用于设定线程池中的线程数
# 其默认值为当前机器 CPU 的核数。

# 一般来说，执行 CPU 密集型任务时，调用越多的核速度就越快。但是当处理网络密集型任务时，
# 事情有有些难以预计了，通过实验来确定线程池的大小才是明智的。

# pool = ThreadPool(4) # Sets the pool size to 4
# 线程数过多时，切换线程所消耗的时间甚至会超过实际工作时间。对于不同的工作，通过尝试来找到线程池大小的最优值是个不错的主意。
# 动手尝试

# 虽然只改动了几行代码，我们却明显提高了程序的执行速度。
# 在生产环境中，我们可以为 CPU 密集型任务和 IO 密集型任务分别选择多进程和多线程库来进一步提高执行速度
# ——这也是解决死锁问题的良方。
# 此外，由于 map 函数并不支持手动线程管理，反而使得相关的 debug 工作也变得异常简单。
# 到这里，我们就实现了（基本）通过一行 Python 实现并行化。

from multiprocessing.dummy import Pool as ThreadPool #io密集型
import urllib2
import time
import logging
from timeit import Timer

#日志
logging.basicConfig(
 level=logging.DEBUG,
 format='[%(asctime)s](%(threadName)-10s) %(message)s'
)

if __name__ == '__main__':
    def test():
        urls = [
            'http://www.163.com',
            'http://www.baidu.com',
            ]

        # Make the Pool of workers
        pool = ThreadPool(4)  #调整线程池 选出最短耗时
        # Open the urls in their own threads
        # and return the results
        # start_time = time.time()
        results = pool.map(urllib2.urlopen, urls)
        #close the pool and wait for the work to finish
        pool.close()
        pool.join()
        # cost = time.time() - start_time
        # logging.debug("cost_time %s", cost)
    def test1():
        i = 3
        while i > 0:
            i -= 1
    t1 = Timer("test1()", 'from __main__ import test1')
    print t1.timeit(1) #运行时间

    t = Timer("test()", 'from __main__ import test')
    print t.timeit(1) #运行时间


