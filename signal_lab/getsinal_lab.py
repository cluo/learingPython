#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
#获取注册程序
#每个进程都用一张表来 保存信号量
#注册函数为SIG_IGN 忽略
#注册函数为SIG_DEF 默认行为
#信号是进程间通信 模拟硬件通信的行为

import signal

def alarm_received(n, stack):
    return

signal.signal(signal.SIGALRM, alarm_received)

signals_to_names = dict(
    (getattr(signal, n), n)
    for n in dir(signal)
    if n.startswith('SIG') and '_' not in n
)

for s, name in sorted(signals_to_names.items()):
    handler = signal.getsignal(s) #获取注册信号的函数
    if handler is signal.SIG_DFL:
        handler = 'SIG_DFL'
    elif handler is signal.SIG_IGN:
        handler = 'SIG_IGN'
    print '%-10s (%2d):' % (name, s), handler

# if __name__ == '__main__':
#     print signals_to_names
#     print dir(signal)
