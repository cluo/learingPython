#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-16
#如果直接用compress 和 decompress 要求系统有足够的内存 能搞在内存中同时候驻留未压缩和压缩版本
#因此对于真实世界的用例并不实用
#另一种方法是用compress decompress 对象以增量的方式处理数据 这样就不需要将整个数据都放在内存中

__author__ = 'cluo'
import zlib
import binascii
import os.path
#压缩依赖校验和和最小块大小
#增量压缩对象
compressor = zlib.compressobj(1) #level 1
with open('./test') as input:
    while True:
        block = input.read(64)
        if not block:
            break
        compressed = compressor.compress(block)
        if compressed:
            print 'Compressed: %s' % binascii.hexlify(compressed)  #压缩器准备好一个完整压缩块才会返回数据
        else:
            print 'buffering..'   #压缩器没有准备好数据一个完整的压缩块 就会返回空字符
    remaining = compressor.flush()#会强制压缩结束最后一块,并返回余下压缩数据
    print 'Flushed: %s' %binascii.hexlify(remaining)






if __name__ == '__main__':
    pass
