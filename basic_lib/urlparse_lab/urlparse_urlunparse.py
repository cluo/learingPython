#!/usr/bin/env python
#-*- coding:utf8 -*-
"""Parsing URLs
"""
#end_pymotw_header

from urlparse import urlparse, urlunparse

original = 'http://netloc/path;param?query=arg#frag'
print 'ORIG  :', original
# ORIG  : http://netloc/path;param?query=arg#frag

parsed = urlparse(original)
print 'PARSED:', type(parsed), parsed
# PARSED: <class 'urlparse.ParseResult'> ParseResult(scheme='http', netloc='netloc', path='/path', params='param', query='query=arg', fragment='frag')

t = parsed[:]
print 'TUPLE :', type(t), t
print 'NEW   :', urlunparse(t) #普通原组 生成URL
# TUPLE : <type 'tuple'> ('http', 'netloc', '/path', 'param', 'query=arg', 'frag')
# NEW   : http://netloc/path;param?query=arg#frag



