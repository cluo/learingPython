#-*- coding:utf8 -*-
__author__ = 'admin'



from gevent.wsgi import WSGIServer
def application(environ, start_response):
	status = '200 ok'
	body = "<p>hello</p>"
	headers = [
		('Content-Type', 'text/html')
	]
	start_response(status,headers)
	return body
WSGIServer(('',8001),application).serve_forever()



# WSGI Servers
#
# Gevent为HTTP内容服务提供了两种WSGI server。从今以后就称为 wsgi和pywsgi：
#
# gevent.wsgi.WSGIServer
# gevent.pywsgi.WSGIServer
# 在1.0.x之前更早期的版本里，gevent使用libevent而不是libev。 Libevent包含了一个快速HTTP server，
# 它被用在gevent的wsgi server。
#
# 在gevent 1.0.x版本，没有包括http server了。作为替代，gevent.wsgi 现在是纯Python server gevent.pywsgi的一个别名。
#
# 流式server
#
# 这个章节不适用于gevent 1.0.x版本
#
# 熟悉流式HTTP服务(streaming HTTP service)的人知道，它的核心思想 就是在头部(header)不指定内容的长度。
# 反而，我们让连接保持打开， 在每块数据前加一个16进制字节来指示数据块的长度，并将数据刷入pipe中。
# 当发出一个0长度数据块时，流会被关闭。
#
#
# HTTP/1.1 200 OK
# Content-Type: text/plain
# Transfer-Encoding: chunked
#
# 8
# <p>Hello
#
# 9
# World</p>
#
# 0
#
# 上述的HTTP连接不能在wsgi中创建，因为它不支持流式。 请求只有被缓冲(buffered)下来。


# $ ab -n 10000 -c 100 http://127.0.0.1:8001/
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
# Server Port:            8001
#
# Document Path:          /
# Document Length:        12 bytes
#
# Concurrency Level:      100
# Time taken for tests:   4.411 seconds
# Complete requests:      10000
# Failed requests:        0
# Write errors:           0
# Total transferred:      1320000 bytes
# HTML transferred:       120000 bytes
# Requests per second:    2267.16 [#/sec] (mean)
# Time per request:       44.108 [ms] (mean)
# Time per request:       0.441 [ms] (mean, across all concurrent requests)
# Transfer rate:          292.25 [Kbytes/sec] received
#
# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        0    0   0.5      0       9
# Processing:     2   44   9.1     43      87
# Waiting:        2   44   9.0     43      87
# Total:          6   44   9.0     43      87
#
# Percentage of the requests served within a certain time (ms)
#   50%     43
#   66%     46
#   75%     49
#   80%     50
#   90%     55
#   95%     60
#   98%     67
#   99%     72
#  100%     87 (longest request)
