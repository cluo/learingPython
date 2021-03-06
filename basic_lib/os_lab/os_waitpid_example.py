#!/usr/bin/env python
#-*- coding:utf8 -*-
# Copyright 2007 Doug Hellmann.
#
#
#                         All Rights Reserved
#
# Permission to use, copy, modify, and distribute this software and
# its documentation for any purpose and without fee is hereby
# granted, provided that the above copyright notice appear in all
# copies and that both that copyright notice and this permission
# notice appear in supporting documentation, and that the name of Doug
# Hellmann not be used in advertising or publicity pertaining to
# distribution of the software without specific, written prior
# permission.
#
# DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
# INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN
# NO EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
# CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#

"""Wait for a worker process.

"""

__module_id__ = "$Id$"
#end_pymotw_header

import os
import sys
import time

workers = []
for i in range(2):
    print 'PARENT %d: Forking %s' % (os.getpid(), i)
    worker_pid = os.fork()
    if not worker_pid:
        print 'WORKER %s: Starting' % i
        time.sleep(2 + i)
        print 'WORKER %s: Finishing' % i
        sys.exit(i) #退出进程
    workers.append(worker_pid)

print workers
for pid in workers:
    print 'PARENT: Waiting for %s' % pid
    done = os.waitpid(pid, 0) #等待特性的进程返回用waitpid(pid)
    print 'PARENT: Child done:', done


# PARENT 82017: Forking 0
# PARENT 82017: Forking 1
# WORKER 0: Starting
# [82018, 82019]
# WORKER 1: StartingPARENT: Waiting for 82018
#
# WORKER 0: Finishing
# PARENT: Child done: (82018, 0)
# PARENT: Waiting for 82019
# WORKER 1: Finishing
# PARENT: Child done: (82019, 256)