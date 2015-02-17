__author__ = 'admin'
import gevent
import random
import time
def task(pid):
    """
    some non-deterministic task
    """
    gevent.sleep(random.randint(0,2)*0.001)
    print ('Task %s done' % pid)
def syschronous():
    for i in range(1,10):
        task(i)
def asynchronous():
    threads =[gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)
start = time.time()
tic = lambda: 'at %1.4f seconds' % (time.time() - start)
print('Synchronous:')
syschronous()
print(tic())
print('asynchronous')
asynchronous()
print(tic())