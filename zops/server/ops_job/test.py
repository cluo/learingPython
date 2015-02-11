#!/usr/bin/env python
#-*- coding:utf8 -*-
__author__ = 'linzhonghong'

import multiprocessing
import time
import os
import signal

def clean_proc(proc, wait_for_kill=10):
    """
    @note:清理进程函数
    @proc:进程实例
    @return:None
    """
    if not proc:
        return
    print 'here'
    try:
        waited = 0
        while proc.is_alive():
            proc.terminate()
            waited += 1
            time.sleep(0.1)
            if proc.is_alive() and (waited >= wait_for_kill):
                os.kill(proc.pid,signal.SIGKILL)
    except (AssertionError, AttributeError):
        pass

class JobHandler(multiprocessing.Process):
    def __init__(self):
        super(JobHandler, self).__init__()


    def run(self):
        print 'in'
        time.sleep(5)

    def __del__(self):
        self.terminate()


class JobServer(object):
    def __init__(self):
        pass

    def run(self):
        while True:
            JobHandler().start()
            # job_handler = JobHandler().start()
            # job_handler.start()
            def sigterm_clean(signum, frame):
                # clean_proc(job_handler)
                try:
                    os.kill(os.getpid(),signal.SIGKILL)
                except OSError:
                    pass
            signal.signal(signal.SIGTERM, sigterm_clean)
            time.sleep(10)

if __name__ == '__main__':
    jobsvr = JobServer()
    jobsvr.run()

import threading
def foo(a, b):
    pass
def boo(a, b):
    pass
thread_list = []
a, b = 1, 2
thread_list.append(threading.Thread(target=foo, args=(a, b)))
thread_list.append(threading.Thread(target=boo, args=(a, b)))
for t in thread_list:
    t.start()
for t in thread_list:
    t.join()