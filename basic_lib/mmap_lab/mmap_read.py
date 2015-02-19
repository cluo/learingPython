#!/usr/bin/env python
#
# Copyright 2007 Doug Hellmann.
#
"""Reading from a memory mapped file.
    建立一个文件的内存映射将适用操作系统虚拟内存系统直接访问文件系统中的数据而不适用常规的I/O函数
    适用内存映射不会对每一个访问都有一个单独的系统调用 不需要再缓冲区之前复制数据 内核用户应用会直接访问内存

"""

#end_pymotw_header

import mmap
import contextlib

with open('lorem.txt', 'r') as f:
    with contextlib.closing(mmap.mmap(f.fileno(), 0,
                                      access=mmap.ACCESS_READ)
                            ) as m:
        print 'First 10 bytes via read :', m.read(10)
        print 'First 10 bytes via slice:', m[:10]
        print '2nd   10 bytes via read :', m.read(10)
