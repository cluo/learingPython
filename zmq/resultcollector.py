#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-11
import time
import zmq
import pprint
__author__ = 'cluo'



def result_collector():
    context = zmq.Context()
    results_receiver = context.socket(zmq.PULL)
    results_receiver.bind("tcp://127.0.0.1:5558")
    collecter_data = {}
    for x in xrange(99):
        result = results_receiver.recv_json()
        if collecter_data.has_key(result['consumer']):
            collecter_data[result['consumer']] = collecter_data[result['consumer']] + 1
        else:
            collecter_data[result['consumer']] = 1
        if x == 98:
            pprint.pprint(collecter_data)




if __name__ == '__main__':
    result_collector()
