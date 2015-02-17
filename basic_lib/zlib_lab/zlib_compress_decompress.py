#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-16
__author__ = 'cluo'

import zlib  #zlib 把所有要压缩 或将要解压缩 的数据放在内存中
import binascii #Convert between binary and ASCII


if __name__ == '__main__':
    original_data = 'this is the original text'
    print 'Original :',len(original_data), original_data
    compressed = zlib.compress(original_data)
    print 'Compressed :',len(compressed),binascii.hexlify(compressed) #二进制转16进制
    decompressed = zlib.decompress(compressed)
    print 'Decompressed:',len(decompressed),decompressed

# Original : 25 this is the original text
# Compressed : 31 789c2bc9c82c5600a2928c5485fca2ccf4ccbcc41c8592d48a120078d10970  数据小的时候压缩反2⃣️变大了
# Decompressed: 25 this is the original text