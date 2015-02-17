#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-16
#如果压缩和未压缩数据混合在一起
__author__ = 'cluo'
import zlib
lorem = open('./test','rt').read()
compressed = zlib.compress(lorem)
combined = compressed + lorem

decompressor = zlib.decompressobj()
decompressed = decompressor.decompress(combined)  #用解压对象解压,返回解压后的数据

decompressed_matches = decompressed == lorem
print 'Decompressed matches lorem:',decompressed_matches
unused_matches = decompressor.unused_data  == lorem   #decompressor.unused 返回未被压缩器使用的数据
print 'Unused data matches lorem:',unused_matches


#结果
# Decompressed matches lorem: True
# Unused data matches lorem: True





if __name__ == '__main__':
    pass
