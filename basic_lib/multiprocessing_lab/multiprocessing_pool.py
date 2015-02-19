#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2009 Doug Hellmann All rights reserved.
#
"""
"""
#end_pymotw_header

import multiprocessing

def do_calculation(data):
    return data * 2

def start_process():
    print 'Starting', multiprocessing.current_process().name

if __name__ == '__main__':
    inputs = list(range(10))
    print 'Input   :', inputs
    
    builtin_outputs = map(do_calculation, inputs)
    print 'Built-in:', builtin_outputs
    
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=pool_size,
                                initializer=start_process,
                                )
    pool_outputs = pool.map(do_calculation, inputs)
    pool.close() # no more tasks
    pool.join()  # wrap up current tasks

    print 'Pool    :', pool_outputs
# Input   : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Built-in: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# Starting PoolWorker-1
# Starting PoolWorker-2
# Starting PoolWorker-3
# Starting PoolWorker-4
# Starting PoolWorker-5
# Starting PoolWorker-6
# Starting PoolWorker-7
# Starting PoolWorker-8
# Pool    : [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]