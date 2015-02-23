__author__ = 'admin'
import gevent
from multiprocessing import Process, Pipe
from gevent.socket import wait_read, wait_write
# To Process
a, b = Pipe() #a send b recv

# From Process
c, d = Pipe() #c send d recv

def relay():
    for i in xrange(10):
        msg = b.recv()
        c.send(msg + " in " + str(i))

def put_msg():
    for i in xrange(10):
        wait_write(a.fileno())
        a.send('hi')

def get_msg():
    for i in xrange(10):
        wait_read(d.fileno())
        print(d.recv())

if __name__ == '__main__':
    proc = Process(target=relay)
    proc.start()

    g1 = gevent.spawn(get_msg)
    g2 = gevent.spawn(put_msg)
    gevent.joinall([g1, g2], timeout=1)



# hi in 0
# hi in 1
# hi in 2
# hi in 3
# hi in 4
# hi in 5
# hi in 6
# hi in 7
# hi in 8
# hi in 9
