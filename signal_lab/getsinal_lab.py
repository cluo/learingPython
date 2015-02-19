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




# SIGHUP     ( 1): SIG_DFL
# SIGINT     ( 2): <built-in function default_int_handler>
# SIGQUIT    ( 3): SIG_DFL
# SIGILL     ( 4): SIG_DFL
# SIGTRAP    ( 5): SIG_DFL
# SIGIOT     ( 6): SIG_DFL
# SIGEMT     ( 7): SIG_DFL
# SIGFPE     ( 8): SIG_DFL
# SIGKILL    ( 9): None
# SIGBUS     (10): SIG_DFL
# SIGSEGV    (11): SIG_DFL
# SIGSYS     (12): SIG_DFL
# SIGPIPE    (13): SIG_IGN
# SIGALRM    (14): <function alarm_received at 0x1028252a8>
# SIGTERM    (15): SIG_DFL
# SIGURG     (16): SIG_DFL
# SIGSTOP    (17): None
# SIGTSTP    (18): SIG_DFL
# SIGCONT    (19): SIG_DFL
# SIGCHLD    (20): SIG_DFL
# SIGTTIN    (21): SIG_DFL
# SIGTTOU    (22): SIG_DFL
# SIGIO      (23): SIG_DFL
# SIGXCPU    (24): SIG_DFL
# SIGXFSZ    (25): SIG_IGN
# SIGVTALRM  (26): SIG_DFL
# SIGPROF    (27): SIG_DFL
# SIGWINCH   (28): SIG_DFL
# SIGINFO    (29): SIG_DFL
# SIGUSR1    (30): SIG_DFL
# SIGUSR2    (31): SIG_DFL