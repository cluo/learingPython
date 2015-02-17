#-*- coding:utf8 -*-
__author__ = 'admin'
import hashlib
m = hashlib.md5()
m.update("Nobody")
print m.digest()     #二进制
print m.hexdigest()  #字符串

m = hashlib.sha1()
m.update("Nobody")
print m.digest()
print m.hexdigest()