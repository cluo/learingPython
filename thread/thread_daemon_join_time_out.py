#-*- coding:utf8 -*-
__author__ = 'admin'

import logging
import threading
import time
#等待守护进程完成要用join,防止无限阻塞用join(sec)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] %(message)s'
)

def daemon():
    logging.debug('Starting')
    time.sleep(3)
    logging.debug('Exting')#没有输出 因为非守护进程 和主程序已经退出
d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)

def non_daemon():
    logging.debug('Starting')
    logging.debug('Exiting')
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()
start = time.time()
d.join(2) #等待守护进程退出
t.join()
end = time.time()
print (end - start) #join所有线程


print 't.isAlive()', t.isAlive()
print 'd.isAlive()', d.isAlive() #阻塞等待程序退出



