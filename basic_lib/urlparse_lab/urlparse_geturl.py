#!/usr/bin/env python
#-*- coding:utf8 -*-
"""Parsing URLs
"""
#end_pymotw_header

from urlparse import urlparse

original = 'http://netloc/path;param?query=arg#frag'
print 'ORIG  :', original
parsed = urlparse(original)  #只适用于urlparse urlsplit返回的对象
print 'PARSED:', parsed.geturl()
