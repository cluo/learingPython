#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-11
import time
import zmq
__author__ = 'cluo'
# 生产者可以推个多个消费者
# 推送速度取决消费速度

def producer():
    context = zmq.Context()
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind("tcp://127.0.0.1:5557")
    # Start your result manager and workers before you start your producers
    for num in xrange(20000):
        work_message = { 'num' : num }
        print work_message
        zmq_socket.send_json(work_message)
        time.sleep(0.1)

if __name__ == '__main__':
    producer()
