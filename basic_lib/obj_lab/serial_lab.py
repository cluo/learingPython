#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-10
__author__ = 'cluo'
import msgpack

from payload import Serial





if __name__ == '__main__':
    serial = Serial()
    d = {'a':1, 'b':2, 'c':3 }

    ser_str = serial.dumps(d)
    d = serial.loads(ser_str)
    print ser_str
    print d




    d = (1,2,3,4)
    ser_str = serial.dumps(d)
    d = serial.loads(ser_str)
    print ser_str
    print d

    msg='aaaafdfd'
    handler = open('/Users/admin/gitSource/learingPython/basic_lib/obj_lab/a.txt','w')
    msg = serial.dump(msg,handler)

    handler = open('/Users/admin/gitSource/learingPython/basic_lib/obj_lab/a.txt','r')
    ser_str = serial.load(handler)
    print ser_str


