#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'
import os
import signal
#handler为signal.SIG_IGN时，信号被无视(ignore)
#当handler为singal.SIG_DFL，进程采取默认操作(default)。
# 当handler为一个函数名时，进程采取函数中定义的操作。
#我们首先使用signal.signal()函数来预设信号处理函数。
# 然后我们执行signal.pause()来让该进程暂停以等待信号，
#以等待信号。当信号SIGUSR1被传递给该进程时，进程从暂停中
#并根据预设，执行SIGTSTP的信号处理函数myHandler()。
#myHandler的两个参数一个用来识别信号(signum)，
#另一个用来获得信号发生时，进程栈的状况(stack frame)。
#这两个参数都是由signal.singnal()函数来传递的。

# 通过按下CTRL+Z向该进程发送SIGTSTP信号。
# 我们可以看到，进程执行了myHandle()函数,
# 随后返回主程序，继续执行。(当然，也可以用$ps查询process ID, 再使用$kill来发出信号。)
# (进程并不一定要使用signal.pause()暂停以等待信号，
# 它也可以在进行工作中接受信号，
# 比如将上面的signal.pause()改为一个需要长时间工作的循环。
# while true
#   doing
#
# )


def sigterm_clean(signum, frame):
        try:
            print 'alive'
            print 'over'
            print signal.SIGTERM #15 等待15信号
            os.kill(os.getpid(),15) #相当于  kill -15 pid
        except OSError:
            print 'error'
            pass

signal.signal(signal.SIGTERM, sigterm_clean)
print os.getpid()

signal.pause()
