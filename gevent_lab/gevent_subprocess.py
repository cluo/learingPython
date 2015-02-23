#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-23
import gevent
from gevent.subprocess import Popen, PIPE
__author__ = 'cluo'

# 自gevent 1.0起，gevent.subprocess，一个Python subprocess模块 的修补版本已经添加。它支持协作式的等待子进程。


def cron():
    while True:
        print("cron")
        gevent.sleep(0.2)

g = gevent.spawn(cron)
sub = Popen(['sleep 1; uname'], stdout=PIPE, shell=True)
out, err = sub.communicate()
g.kill()
print(out.rstrip())

# cron
# cron
# cron
# cron
# cron
# cron
# Darwin
