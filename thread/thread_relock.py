#-*- coding:utf8 -*-
__author__ = 'admin'

import logging
import threading

logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s')
lock = threading.Lock()
logging.debug('first try : %s' % lock.acquire())
logging.debug('second try: %s' % lock.acquire(0)) #正常来说对同一线程 不能锁多次  设置了获取锁超时


lock = threading.RLock() #重新上锁
logging.debug('first try : %s' % lock.acquire())
logging.debug('second try: %s' % lock.acquire(0)) #正常来说对同一线程 不能锁多次




