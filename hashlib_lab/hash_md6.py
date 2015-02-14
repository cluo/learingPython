#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 15-2-12
__author__ = 'cluo'

import hashlib
h = hashlib.md5()
h.update('cluo')
print h.hexdigest()  #字符
print h.digest() #二进制


h = hashlib.sha1()




