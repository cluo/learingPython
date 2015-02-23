#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-23
__author__ = 'cluo'

from gevent.pywsgi import WSGIServer
def application(environ, start_response):
    status = '200 OK'
    headers = [ ('Content-Type', 'text/html') ]
    start_response(status, headers)
    yield "<p>Hello"
    yield "World</p>"
WSGIServer(('', 8000), application).serve_forever()



# $ ab -n 10000 -c 100 http://127.0.0.1:8000/
# This is ApacheBench, Version 2.3 <$Revision: 655654 $>
# Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
# Licensed to The Apache Software Foundation, http://www.apache.org/
#
# Benchmarking 127.0.0.1 (be patient)
# Completed 1000 requests
# Completed 2000 requests
# Completed 3000 requests
# Completed 4000 requests
# Completed 5000 requests
# Completed 6000 requests
# Completed 7000 requests
# Completed 8000 requests
# Completed 9000 requests
# Completed 10000 requests
# Finished 10000 requests
#
#
# Server Software:
# Server Hostname:        127.0.0.1
# Server Port:            8000
#
# Document Path:          /
# Document Length:        17 bytes
#
# Concurrency Level:      100
# Time taken for tests:   2.884 seconds
# Complete requests:      10000
# Failed requests:        0
# Write errors:           0
# Total transferred:      1170000 bytes
# HTML transferred:       170000 bytes
# Requests per second:    3467.36 [#/sec] (mean)
# Time per request:       28.840 [ms] (mean)
# Time per request:       0.288 [ms] (mean, across all concurrent requests)
# Transfer rate:          396.17 [Kbytes/sec] received
#
# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        0    0   0.7      0       6
# Processing:     3   29  21.2     25     222
# Waiting:        3   28  21.1     25     222
# Total:          7   29  21.2     26     222
#
# Percentage of the requests served within a certain time (ms)
#   50%     26
#   66%     27
#   75%     28
#   80%     29
#   90%     32
#   95%     35
#   98%    110
#   99%    202
#  100%    222 (longest request)