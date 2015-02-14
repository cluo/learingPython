__author__ = 'admin'
import threading
import logging
logging.basicConfig(level=logging.DEBUG,
          format='(%(threadName)-10s) %(message)s')
class MyThread(threading.Thread):
  def __init__(self, group=None, target=None, name=None,args=(), kwargs=None, verbose=None):
    threading.Thread.__init__(self,group=group,
                  target=target,
                  name=name,
                  verbose=verbose)
         
    self.args = args
    self.kwargs = kwargs
    print target


  def run(self):
    logging.debug('running %s and %s',
            self.args,
            self.kwargs)
    return

def handler():
    # print 'args: %s, %s' %(args, kwargs)
    print 'hello world'

for i in range(5):
    thread_name = 'thread_name: %s' % (i)
    t = MyThread(args=(i,), kwargs={'a':'A', 'b':'B'}, target=handler, name=thread_name)
    t.start()
