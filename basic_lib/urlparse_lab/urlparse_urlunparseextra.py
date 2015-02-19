#!/usr/bin/env python
"""Parsing URLs
"""
#end_pymotw_header

from urlparse import urlparse, urlunparse

original = 'http://netloc/path;?#'
print 'ORIG  :', original
# ORIG  : http://netloc/path;?#

parsed = urlparse(original)
print 'PARSED:', type(parsed), parsed
# PARSED: <class 'urlparse.ParseResult'> ParseResult(scheme='http', netloc='netloc', path='/path', params='', query='', fragment='')

t = parsed[:]
print 'TUPLE :', type(t), t
print 'NEW   :', urlunparse(t)

# TUPLE : <type 'tuple'> ('http', 'netloc', '/path', '', '', '')
# NEW   : http://netloc/path