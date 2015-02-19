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

for i in range(2):
    print 'PARENT %s: Forking %s' % (os.getpid(), i)
    worker_pid = os.fork()
    print "child_pid",worker_pid
    if not worker_pid:
        print 'WORKER %s: Starting' % i
        time.sleep(2 + i)
        print 'WORKER %s: Finishing' % i
        sys.exit(i)

for i in range(2):
    print 'PARENT: Waiting for %s' % i
    done = os.wait() #一旦有子进程退出,它就会返回
    print 'PARENT: Child done:', done  #返回进程退出的子进程ID 和退出状态



# PARENT 79583: Forking 0
# PARENT 79583: Forking 1
# WORKER 0: Starting
# PARENT: Waiting for 0
# WORKER 1: Starting
# WORKER 0: Finishing
# PARENT: Child done: (79584, 0)
# PARENT: Waiting for 1
# WORKER 1: Finishing
# PARENT: Child done: (79585, 256)