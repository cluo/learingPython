#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-23
import gevent.monkey
gevent.monkey.patch_socket()
import gevent
import urllib2
import simplejson as json
def fetch(pid):
    response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)  #解析dict
    datetime = json_result['datetime']
    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']
def synchronous():
    for i in range(1,10):
        fetch(i)
def asynchronous():
    tasks = []
    for i in range(1,10):
        tasks.append(gevent.spawn(fetch, i))
        gevent.joinall(tasks)
print('Synchronous:')
synchronous()
print('Asynchronous:')
asynchronous()