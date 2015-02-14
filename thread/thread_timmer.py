__author__ = 'admin'
import threading
import time
import logging
#延时一定的时候后开始工作，可以再这个延时期间内的任意时刻取消
#非守护线程 主程序完成时,线程会隐式退出
logging.basicConfig(level=logging.DEBUG,
					format='(%(threadName)-10s) %(message)s')
def delayed():
	logging.debug('worker running')
	return
t1= threading.Timer(3,delayed)
t1.setName('t1')
t2 = threading.Timer(3,delayed)
t2.setName('t2')

logging.debug('starting timmers')
t1.start()
t2.start()

logging.debug('warting before canceling %s ',t2.getName())
time.sleep(2)
logging.debug('canceling %s',t2.getName())
t2.cancel()
logging.debug('done')



