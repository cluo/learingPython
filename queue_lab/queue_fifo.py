#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-15
__author__ = 'cluo'
import Queue
q = Queue.Queue()
for i in range(5):
    q.put(i)

while not q.empty():
    print q.get()



