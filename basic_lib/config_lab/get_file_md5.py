#-*- coding:utf8 -*-
__author__ = 'admin'
import hashlib
import os.path

def generate_file_sha1(rootdir, filename, blocksize=2**20):
    """生成文件的SHA1值"""
    m = hashlib.md5()
    with open(os.path.join(rootdir, filename) , "rb" ) as f:
        while True:
            buf = f.read(blocksize)
            if not buf:
                break
            m.update( buf )
    return m.hexdigest()

rootdir = os.path.abspath('./')
print generate_file_sha1(rootdir,'test')