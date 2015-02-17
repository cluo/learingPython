#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-11
__author__ = 'cluo'
import zmq
import random



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
        print work
        data = work['num']
        result = { 'consumer':consumer_id, 'num': data}
        if data%2 == 0:
            consumer_sender.send_json(result)


if __name__ == '__main__':
    consummer()