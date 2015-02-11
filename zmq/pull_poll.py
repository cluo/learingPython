#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-11
__author__ = 'cluo'
import time
import zmq
import random
import pprint

def producer():
    context = zmq.Context
    zmq_socket = context.socket(zmq.PUSH)
    zmq_socket.bind('tcp://127.0.0.1:5557')
    for num in xrange(20000):
        work_message = { 'num' : num }
        zmq_socket.send_json(work_message)


def consummer():
    consumer_id = random.randrange(1,10005)
    print "I am consumer #%s" %(consumer_id)
    context = zmq.Context()
    # recieve work
    consumer_receiver = context.socket(zmq.PULL)
    consumer_receiver.connect("tcp://127.0.0.1:5557")
    # send work
    consumer_sender = context.socket(zmq.PUSH)
    consumer_sender.connect("tcp://127.0.0.1:5558")

    while True:
        work = consumer_receiver.recv_json()
        data = work['num']
        result = { 'consumer':consumer_id, 'num': data}
        if data%2 == 0:
            consumer_sender.send_json(result)


def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    collecter_data = {}
    for x in xrange(1000):
        result = results_receiver.recv_json()
        if collecter_data.has_key(result['consumer']):
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
        else:
            collecter_data[result['consumer']] = 1
        if x == 999:
            pprint.pprint(collecter_data)

if __name__ == '__main__':
    pass
