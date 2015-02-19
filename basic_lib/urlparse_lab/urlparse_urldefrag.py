#!/usr/bin/env python
#-*- coding:utf8 -*-
"""Remove fragment portion of URL
"""
#end_pymotw_header

from urlparse import urldefrag

original = 'http://netloc/path;param?query=arg#frag'
print 'original:', original
url, fragment = urldefrag(original) #剥离片段标识符号
print 'url     :', url
print 'fragment:', fragment
