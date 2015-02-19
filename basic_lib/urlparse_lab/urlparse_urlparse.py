#!/usr/bin/env python
#-*- coding:utf8 -*-
"""Parsing URLs
"""
#end_pymotw_header

from urlparse import urlparse

url = 'http://netloc/path;param?query=arg#frag'
parsed = urlparse(url) #返回相当于6个元素的tuple
print parsed
# ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')