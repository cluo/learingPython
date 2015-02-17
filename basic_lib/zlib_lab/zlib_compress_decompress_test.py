#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-16
__author__ = 'cluo'

import zlib
import binascii #Convert between binary and ASCII


if __name__ == '__main__':
    original_data = 'this is the original text'
    fmt = '%15s %15s'
    print fmt % ('len(data', 'len(compressed)')
    print fmt % ('-'*15, '-'*15)
    for i in xrange(5):
        data = original_data * i
        compressed = zlib.compress(data)
        highlight = '*' if len(data) < len(compressed) else ''  #写法比较牛逼
        print fmt % (len(data), len(compressed)), highlight

#结果 *号表示压缩后反而变大了的
#        len(data len(compressed)
# --------------- ---------------
#               0               8 *
#              25              31 *
#              50              34
#              75              34
#             100              35


